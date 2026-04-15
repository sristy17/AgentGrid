from app.core.agent_interface import Agent
from app.services.llm_service import LLMService

class StrategyAgent(Agent):
    def __init__(self):
        self.llm = LLMService()

    def run(self, insights, analytics):
        # Scale awareness prevents suggesting millions for small businesses
        rev = analytics.get('revenue', 0)
        prof = analytics.get('profit', 0)

        prompt = f"""
You are a Business Strategy Consultant.
Company Scale: Revenue ${rev}, Profit ${prof}.

INSIGHTS TO ADDRESS:
{insights}

STRICT RULES:
1. Impact estimates MUST be proportional to ${rev}. 
2. DO NOT suggest savings or growth in the millions if revenue is in thousands.
3. Use percentages for impact (e.g., "Expected 5% revenue increase").
4. If profit is low, prioritize immediate cost-cutting.

Return ONLY JSON:
{{
  "pricing": [{{"strategy": "", "description": "", "impact": ""}}],
  "growth": [{{"strategy": "", "description": "", "impact": ""}}],
  "cost_cutting": [{{"strategy": "", "description": "", "impact": ""}}]
}}
"""
        return self.llm.generate_json(prompt)