from dotenv import load_dotenv
import os

load_dotenv()

print("API Key Found:", bool(os.getenv("OPENAI_API_KEY")))