from app.core.agent_interface import Agent
from app.services.llm_service import LLMService


class InsightAgent(Agent):

    def __init__(self):
        self.llm = LLMService()

    def run(self, analytics):
        prompt = f"""
You are a strict business analyst.

Data:
{analytics}

Rules:
- ONLY use provided data
- NO assumptions
- NO empty fields
- Each problem must include a clear description
- Each reason must explain WHY (not repeat numbers)

Bad example:
"profit: 150" 

Good example:
"Profit margin is low because costs consume a large portion of revenue" 

Return ONLY JSON:
{{
  "problems": [
    {{"type": "", "description": ""}}
  ],
  "reasons": [
    {{"problem": "", "reason": ""}}
  ]
}}
"""
        return self.llm.generate_json(prompt)