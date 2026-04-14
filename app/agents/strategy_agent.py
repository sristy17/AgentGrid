from app.core.agent_interface import Agent
from app.services.llm_service import LLMService


class StrategyAgent(Agent):

    def __init__(self):
        self.llm = LLMService()

    def run(self, insights):
        prompt = f"""
You are a business strategist.

Given insights:
{insights}

Rules:
- Strategies must be SPECIFIC and ACTIONABLE
- Avoid vague terms like "improve" or "adjust"
- Each strategy must include:
  - strategy (short title)
  - description (clear explanation)
  - impact (expected outcome)

Bad example:
"price adjustment" 

Good example:
"Increase prices by 5% for high-demand products to improve margins" 

Return ONLY JSON:
{{
  "pricing": [
    {{"strategy": "", "description": "", "impact": ""}}
  ],
  "growth": [
    {{"strategy": "", "description": "", "impact": ""}}
  ],
  "cost_cutting": [
    {{"strategy": "", "description": "", "impact": ""}}
  ]
}}
"""
        return self.llm.generate_json(prompt)