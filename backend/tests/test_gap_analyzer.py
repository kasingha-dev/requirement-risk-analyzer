import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.gap_analyzer import GapAnalyzer

requirements = {
    "features": [
        "Premium membership plans",
        "User registration",
        "Stripe payments",
        "Admin dashboard"
    ]
}

result = GapAnalyzer.analyze(requirements)

print(result)