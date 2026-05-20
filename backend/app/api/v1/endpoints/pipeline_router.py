from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from backend.app.database.session import get_db
from backend.app.models.models import Pipeline, Failure
from backend.app.api.v1.schemas.pipeline_schema import FailureCreate, FailureResponse, PipelineHistory
from backend.app.agents.agents import run_healing_workflow
from typing import List

router = APIRouter()

@router.post("/failure", response_model=FailureResponse, status_code=status.HTTP_201_CREATED)
async def report_failure(failure_in: FailureCreate, background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    # Check if pipeline exists or create one
    result = await db.execute(select(Pipeline).where(Pipeline.repository == failure_in.repository, Pipeline.branch == failure_in.branch))
    pipeline = result.scalars().first()
    
    if not pipeline:
        pipeline = Pipeline(repository=failure_in.repository, branch=failure_in.branch, status="failure")
        db.add(pipeline)
        await db.commit()
        await db.refresh(pipeline)

    new_failure = Failure(
        pipeline_id=pipeline.id,
        error_log=failure_in.error_log
    )
    db.add(new_failure)
    await db.commit()
    await db.refresh(new_failure)
    
    # Trigger ADK agents in background
    background_tasks.add_task(run_healing_workflow, new_failure.id, new_failure.error_log, db)
    
    return {
        "id": new_failure.id,
        "pipeline_id": str(pipeline.id),
        "repository": pipeline.repository,
        "branch": pipeline.branch,
        "error_log": new_failure.error_log,
        "created_at": new_failure.created_at,
        "root_cause": new_failure.root_cause,
        "ai_analysis": new_failure.ai_analysis
    }

@router.get("/history", response_model=List[PipelineHistory])
async def get_history(db: AsyncSession = Depends(get_db)):
    # Use selectinload to eagerly load the failures relationship to prevent lazy loading errors
    result = await db.execute(select(Pipeline).options(selectinload(Pipeline.failures)))
    pipelines = result.scalars().all()
    return pipelines

