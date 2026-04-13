from app.core.agent_interface import Agent
from app.services.llm_service import LLMService


class StrategyAgent(Agent):

    def __init__(self):
        self.llm = LLMService()

    def run(self, insights):
        prompt = f"""
You are a business strategist.

Given these insights:
{insights}

Suggest actionable strategies.

Return ONLY JSON:
{{
  "pricing": [],
  "growth": [],
  "cost_cutting": []
}}
"""

        return self.llm.generate_json(prompt)