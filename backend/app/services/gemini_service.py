from google import genai
import json
from backend.app.core.config import settings


class GeminiService:
    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GOOGLE_API_KEY
        )

    async def analyze_log(self, error_log: str):
        prompt = f"""
        Analyze the following CI/CD pipeline error log and identify the root cause.

        Return the result in JSON format with:
        - issue
        - root_cause
        - suggested_fix
        - category

        Categories:
        dependency, syntax, docker, test, env, other

        Error Log:
        {error_log}
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        try:
            text = response.text

            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()

            elif "```" in text:
                text = text.split("```")[1].split("```")[0].strip()

            return json.loads(text)

        except Exception as e:
            return {
                "issue": "Analysis failed",
                "root_cause": str(e),
                "suggested_fix": "Manual review required",
                "category": "other"
            }


gemini_service = GeminiService()