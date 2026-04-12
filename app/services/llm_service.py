import requests
import json


class LLMService:

    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "llama3"

    def generate_text(self, prompt: str):
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()
        return data["response"]

    def generate_json(self, prompt: str, retries=2):
        try:
            full_prompt = f"""
You must return ONLY valid JSON. No explanation.

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

            return json.loads(output)

        except Exception as e:
            if retries > 0:
                return self.generate_json(prompt, retries - 1)

            raise Exception(f"JSON parsing failed: {e}")