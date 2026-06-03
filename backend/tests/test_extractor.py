import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv

load_dotenv()

from services.requirement_extractor import RequirementExtractor

sample_text = """
Users can register.

Users can subscribe to plans.

Payments handled through Stripe.

Admins can view reports.
"""

result = RequirementExtractor.extract_requirements(
    sample_text
)

print(result)