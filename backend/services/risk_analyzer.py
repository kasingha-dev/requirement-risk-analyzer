class RiskAnalyzer:

    @classmethod
    def analyze(cls, requirements):

        risks = {
            "high": [],
            "medium": [],
            "low": []
        }

        features = requirements.get("features", [])
        actors = requirements.get("actors", [])
        integrations = requirements.get("integrations", [])
        constraints = requirements.get("constraints", [])

        search_space = (
            features
            + actors
            + integrations
            + constraints
        )

        requirement_text = " ".join(search_space).lower()

        # Payment Risks

        payment_detected = any(
            word in requirement_text
            for word in [
                "payment",
                "payments",
                "stripe",
                "razorpay",
                "billing",
                "checkout"
            ]
        )

        payment_handling_defined = any(
            phrase in requirement_text
            for phrase in [
                "payment failure",
                "failed payment",
                "retry payment",
                "refund",
                "refunds",
                "chargeback"
            ]
        )

        if payment_detected and not payment_handling_defined:
            risks["high"].append(
                "Payment failure and refund handling are not defined"
            )

        # Admin Risks

        if (
            "admin" in requirement_text
            and "permission" not in requirement_text
        ):

            risks["medium"].append(
                "Authorization and permission model is unclear"
            )

        # File Upload Risks

        if any(
            word in requirement_text
            for word in [
                "upload",
                "file",
                "document",
                "image",
                "video"
            ]
        ):
            risks["medium"].append(
                "Storage requirements are not defined"
            )

        # Notification Risks

        if "notification" in requirement_text:

            risks["low"].append(
                "Notification delivery strategy not specified"
            )

        return risks