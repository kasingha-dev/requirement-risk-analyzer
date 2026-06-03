import json

from services.llm_service import LLMService


class QuestionGenerator:

    @classmethod
    def generate(
        cls,
        requirements,
        missing_requirements,
        risks
    ):


        prompt = f"""
            You are a senior product manager and software architect.

            Generate the MOST IMPORTANT questions that must be answered before development begins.

            Rules:
            - Generate 2-4 CRITICAL questions.
            - Generate 3-5 IMPORTANT questions.
            - Critical questions are blockers that impact scope, architecture, cost, security, or major functionality.
            - Important questions improve implementation clarity but are not project blockers.
            - Avoid duplicates.
            - Keep questions concise.

            Requirements:
            {json.dumps(requirements, indent=2)}

            Missing Requirements:
            {json.dumps(missing_requirements, indent=2)}

            Risks:
            {json.dumps(risks, indent=2)}

            Return ONLY valid JSON.

            Format:

            {{
                "critical": [],
                "important": []
            }}

        """

        llm = LLMService()

        result = llm.ask(prompt)

        parsed_result = json.loads(result)

        return {
            "critical": parsed_result.get("critical", []),
            "important": parsed_result.get("important", [])
        }