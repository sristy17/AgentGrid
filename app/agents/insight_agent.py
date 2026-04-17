from app.core.agent_interface import Agent
from app.services.llm_service import LLMService

class InsightAgent(Agent):
    def __init__(self):
        self.llm = LLMService()

    def run(self, analytics, trend=None):
        rev = analytics.get('revenue', 0)
        cost = analytics.get('cost', 0)
        prof = analytics.get('profit', 0)
        
        trend_context = "No previous trend data available."

        if trend:
            rev_p = trend.get('revenue_pct', 0)
            cost_p = trend.get('cost_pct', 0)
            prof_p = trend.get('profit_pct', 0)

            trend_context = (
                "Trend Data Analysis:\n"
                f"- Revenue Change: {rev_p}%\n"
                f"- Cost Change: {cost_p}%\n"
                f"- Profit Change: {prof_p}%"
            )

        prompt = f"""
You are a Financial Data Analyst. 
METRICS:
- Revenue: ${rev}
- Cost: ${cost}
- Profit: ${prof}

{trend_context}

STRICT LOGIC RULES:
1. REVENUE/PROFIT: If a percentage change is POSITIVE (e.g., 100%), it is GROWTH. Do NOT list it as a 'Problem'.
2. COST: If Cost change is POSITIVE, it is an 'Expense Increase' and IS a problem.
3. PROFITABILITY: If Profit is positive, do NOT say 'Cost is higher than revenue'.
4. NO GHOST DATA: Do not mention specific dates or external market factors not provided in the numbers.

Return ONLY JSON:
{{
  "problems": [{{"type": "string", "description": "string"}}],
  "reasons": [{{"problem": "string", "reason": "string"}}]
}}
"""
        return self.llm.generate_json(prompt)