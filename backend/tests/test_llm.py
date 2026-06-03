import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv

load_dotenv()

from services.llm_service import LLMService

llm = LLMService()

response = llm.ask("""
Return a JSON object with one key called hello.
""")

print(response)