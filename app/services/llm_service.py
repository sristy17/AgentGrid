import requests
import json
import re


class LLMService:

    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "llama3"

    def extract_json(self, text: str):
        try:
            match = re.search(r"\{.*\}", text, re.DOTALL)
            if match:
                return json.loads(match.group())
        except Exception:
            pass
        return None

    def generate_json(self, prompt: str, retries=2):
        try:
            full_prompt = f"""
You MUST return ONLY valid JSON.
No explanation. No text outside JSON.

{prompt}
"""

            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": full_prompt,
                    "stream": False
                }
            )

            data = response.json()
            output = data["response"]

            parsed = self.extract_json(output)

            if parsed:
                return parsed

            raise Exception("Invalid JSON format")

        except Exception as e:
            if retries > 0:
                return self.generate_json(prompt, retries - 1)

            raise Exception(f"JSON parsing failed: {e}")