import json

from services.llm_service import LLMService


class ArchitectureAnalyzer:

    @classmethod
    def analyze(cls, requirements):

        prompt = f"""
            You are a senior software architect.

            Review the software requirements and identify
            architecture concerns that should be considered
            before development begins.

            Focus on:

            - Scalability concerns
            - Security concerns
            - Infrastructure concerns
            - Integration concerns

            Rules:
            - Generate 5 to 10 concerns.
            - Keep each concern concise.
            - Focus on architectural implications.
            - Do NOT recommend specific technologies.
            - Do NOT explain the concern.

            Requirements:
            {json.dumps(requirements, indent=2)}

            Return ONLY valid JSON.

            Format:

            {{
                "high_priority": [],
                "medium_priority": []
            }}
        """

        llm = LLMService()

        result = llm.ask(prompt)

        parsed_result = json.loads(result)

        return {
            "high_priority": parsed_result.get("high_priority", []),
            "medium_priority": parsed_result.get("medium_priority", [])
        }