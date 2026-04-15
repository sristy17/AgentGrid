from app.core.agent_interface import Agent
from app.services.llm_service import LLMService

class InsightAgent(Agent):
    def __init__(self):
        self.llm = LLMService()

    def run(self, analytics, trend=None):
        trend_context = "No previous trend data available."

        if trend:
            # Cast values to strings first to prevent f-string parser errors
            rev_c = str(trend.get('revenue_change', 0))
            rev_p = str(trend.get('revenue_pct', 0))
            cost_c = str(trend.get('cost_change', 0))
            cost_p = str(trend.get('cost_pct', 0))
            prof_c = str(trend.get('profit_change', 0))
            prof_p = str(trend.get('profit_pct', 0))

            trend_context = (
                "Trend Data Analysis:\n"
                f"- Revenue: {rev_c} ({rev_p}% change)\n"
                f"- Cost: {cost_c} ({cost_p}% change)\n"
                f"- Profit: {prof_c} ({prof_p}% change)"
            )

        prompt = f"""
You are a strict business analyst. 
Current Data:
- Revenue: {analytics.get('revenue', 0)}
- Cost: {analytics.get('cost', 0)}
- Profit: {analytics.get('profit', 0)}

{trend_context}

Task: Identify business problems and reasons using ONLY the provided numbers. 
Rules: Do not invent timeframes or future dates. Return ONLY JSON.

Return ONLY JSON:
{{
  "problems": [{{"type": "string", "description": "string"}}],
  "reasons": [{{"problem": "string", "reason": "string"}}]
}}
"""
        return self.llm.generate_json(prompt)