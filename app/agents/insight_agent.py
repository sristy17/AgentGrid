from app.core.agent_interface import Agent
from app.services.llm_service import LLMService


class InsightAgent(Agent):

    def __init__(self):
        self.llm = LLMService()

    def run(self, analytics):
       prompt = f"""
You are a business analyst.

Data:
{analytics}

Facts (DO NOT CHANGE):
- revenue = {analytics["revenue"]}
- cost = {analytics["cost"]}
- profit = {analytics["profit"]}
- profit = revenue - cost (already validated)

Do NOT question calculations.

Focus ONLY on:
- inefficiencies
- risks
- improvement areas

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