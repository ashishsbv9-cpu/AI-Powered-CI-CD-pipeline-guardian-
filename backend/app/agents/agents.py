from google.adk import Agent
from backend.app.services.gemini_service import gemini_service
from backend.app.validators.validation_engine import validation_engine
from backend.app.services.fix_engine import auto_fix_engine
from backend.app.models.models import Failure, Fix, Validation
from sqlalchemy.ext.asyncio import AsyncSession
import os

# Define Agents
class MonitorAgent(Agent):
    name: str = "Monitor Agent"
    description: str = "Detects failure events and starts the recovery workflow."

class AnalyzerAgent(Agent):
    name: str = "AnalyzerAgent"
    description: str = "Analyzes logs using Gemini to find root cause."
    
    async def run(self, error_log: str):
        return await gemini_service.analyze_log(error_log)

class FixGeneratorAgent(Agent):
    name: str = "FixGeneratorAgent"
    description: str = "Generates patches and configuration changes based on analysis."
    
    async def run(self, analysis: dict):
        if analysis.get("category") == "dependency":
            # Extract package from root_cause or issue
            # Simplified for demo
            package = analysis.get("root_cause", "").split(" ")[0].replace("package", "").strip()
            success = auto_fix_engine.apply_dependency_fix(package)
            return {
                "patch": f"Added {package} to requirements.txt" if success else "Fix already applied",
                "description": analysis.get("suggested_fix")
            }
        return {
            "patch": f"Suggested Change: {analysis.get('suggested_fix')}",
            "description": analysis.get('suggested_fix')
        }

class ValidatorAgent(Agent):
    name: str = "ValidatorAgent"
    description: str = "Runs tests and security scans on the proposed fix."
    
    async def run(self, fix: dict):
        results = validation_engine.validate_all()
        return results

class DecisionAgent(Agent):
    name: str = "DecisionAgent"
    description: str = "Decides if the fix should be applied and the pipeline re-run."
    
    async def run(self, validation_results: dict):
        if (validation_results["test_status"] == "passed" and 
            validation_results["security_status"] == "passed"):
            return "approved"
        return "rejected"

# Workflow Orchestration
async def run_healing_workflow(failure_id: int, error_log: str, db: AsyncSession):
    analyzer = AnalyzerAgent()
    fixer = FixGeneratorAgent()
    validator = ValidatorAgent()
    decider = DecisionAgent()

    # Step 1: Analyze
    analysis = await analyzer.run(error_log)
    
    # Store analysis in DB
    result = await db.get(Failure, failure_id)
    if result:
        result.root_cause = analysis.get("issue")
        result.ai_analysis = analysis
        await db.commit()

    # Step 2: Generate Fix
    fix_suggestion = await fixer.run(analysis)
    
    description = fix_suggestion.get("description")
    if isinstance(description, list):
        description = "\n".join(str(item) for item in description)
    elif description is None:
        description = "No suggestion provided"
    else:
        description = str(description)

    new_fix = Fix(
        failure_id=failure_id,
        fix_description=description,
        validation_status="pending"
    )
    db.add(new_fix)
    await db.commit()
    await db.refresh(new_fix)

    # Step 3: Validate
    validation_results = await validator.run(fix_suggestion)
    new_val = Validation(
        fix_id=new_fix.id,
        **validation_results
    )
    db.add(new_val)
    
    # Step 4: Decide
    decision = await decider.run(validation_results)
    new_fix.validation_status = "passed" if decision == "approved" else "failed"
    
    await db.commit()
    return {"status": decision, "fix_id": new_fix.id}
