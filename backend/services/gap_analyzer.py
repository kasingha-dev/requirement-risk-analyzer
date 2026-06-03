class GapAnalyzer:
    """
    Identifies missing requirement areas using
    deterministic feature checklists.
    """

    FEATURE_RULES = {
        "subscription": {
            "aliases": [
                "subscription",
                "membership",
                "plan",
                "premium",
                "recurring"
            ],
            "required": [
                "renewal flow",
                "cancellation flow",
                "refund process"
            ]
        },

        "authentication": {
            "aliases": [
                "authentication",
                "login",
                "register",
                "signup",
                "sign up",
                "user account"
            ],
            "required": [
                "password reset",
                "email verification"
            ]
        },

        "payment": {
            "aliases": [
                "payment",
                "stripe",
                "razorpay",
                "checkout",
                "billing"
            ],
            "required": [
                "payment failure handling",
                "refund process"
            ]
        },

        "admin": {
            "aliases": [
                "admin",
                "administrator",
                "backoffice",
                "management portal"
            ],
            "required": [
                "role permissions",
                "audit logs"
            ]
        },

        "reporting": {
            "aliases": [
                "report",
                "reporting",
                "dashboard",
                "analytics"
            ],
            "required": [
                "export functionality",
                "access control"
            ]
        }
    }

    @classmethod
    def analyze(cls, requirements):

        missing = set()

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

        for rule in cls.FEATURE_RULES.values():

            aliases = rule["aliases"]
            required_items = rule["required"]

            rule_detected = any(
                alias in requirement_text
                for alias in aliases
            )

            if not rule_detected:
                continue

            for item in required_items:

                if item.lower() not in requirement_text:
                    missing.add(item)

        return sorted(list(missing))