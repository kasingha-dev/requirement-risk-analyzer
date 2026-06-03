import os

from openai import OpenAI


class LLMService:

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def ask(self, prompt: str):

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            response_format={"type": "json_object"},
            temperature=0
        )

        content = response.choices[0].message.content

        if not content:
            raise Exception("LLM returned empty response")

        return content