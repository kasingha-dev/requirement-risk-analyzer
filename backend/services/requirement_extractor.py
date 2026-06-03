import json

from services.llm_service import LLMService


class RequirementExtractor:

    @staticmethod
    def extract_requirements(text):

        prompt = f"""
        Extract software requirements from the text.

        Return a JSON object with EXACTLY these keys:

        {{
            "features": [],
            "actors": [],
            "integrations": [],
            "constraints": []
        }}

        Text:
        {text}
        """

        llm = LLMService()

        result = llm.ask(prompt)

        try:
            return json.loads(result)
        except json.JSONDecodeError:
            raise Exception(
                f"Invalid JSON returned by LLM: {result}"
            )