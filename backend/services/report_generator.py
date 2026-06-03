class ReportGenerator:

    @classmethod
    def generate(
        cls,
        requirements,
        missing_requirements,
        risks,
        questions,
        architecture_concerns
    ):

        report = {
            "summary": {
                "feature_count": len(
                    requirements.get("features", [])
                ),

                "actor_count": len(
                    requirements.get("actors", [])
                ),

                "integration_count": len(
                    requirements.get("integrations", [])
                ),

                "missing_requirement_count": len(
                    missing_requirements
                ),

                "high_risk_count": len(
                    risks.get("high", [])
                )
            },

            "requirements": requirements,

            "missing_requirements": missing_requirements,

            "risks": risks,

            "questions": questions,

            "architecture_concerns": architecture_concerns
        }

        return report