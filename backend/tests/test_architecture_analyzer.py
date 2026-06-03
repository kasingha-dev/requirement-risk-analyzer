import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv

load_dotenv()

from services.architecture_analyzer import ArchitectureAnalyzer

requirements = {
    "features": [
        "Subscription purchase",
        "User registration",
        "Admin user management",
        "File uploads"
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

result = ArchitectureAnalyzer.analyze(
    requirements
)

print(result)