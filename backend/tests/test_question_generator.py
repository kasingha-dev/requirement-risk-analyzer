import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv

load_dotenv()

from services.question_generator import QuestionGenerator

requirements = {
    "features": [
        "Subscription purchase",
        "Admin user management"
    ],
    "actors": [
        "Users",
        "Admins"
    ],
    "integrations": [
        "Stripe"
    ],
    "constraints": []
}

missing_requirements = [
    "refund process",
    "renewal flow",
    "role permissions"
]

risks = {
    "high": [
        "Payment failure and refund handling are not defined"
    ],
    "medium": [
        "Authorization and permission model is unclear"
    ],
    "low": []
}

questions = QuestionGenerator.generate(
    requirements,
    missing_requirements,
    risks
)

print(questions)