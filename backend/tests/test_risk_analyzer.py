import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.risk_analyzer import RiskAnalyzer

requirements = {
    "features": [
        "File uploads",
        "Admin dashboard"
    ],

    "actors": [
        "Admin"
    ],

    "integrations": [
        "Stripe"
    ],

    "constraints": []
}

result = RiskAnalyzer.analyze(
    requirements
)

print(result)