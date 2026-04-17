from app.core.agent_interface import Agent
from app.services.llm_service import LLMService

class StrategyAgent(Agent):
    def __init__(self):
        self.llm = LLMService()

    def run(self, insights, analytics):
        rev = analytics.get('revenue', 0)
        prof = analytics.get('profit', 0)
        cost = analytics.get('cost', 0)

        prompt = f"""
You are a Senior Business Strategy Consultant.
Target Company Metrics: 
- Total Revenue: ${rev}
- Total Cost: ${cost}
- Total Profit: ${prof}

INSIGHTS TO ADDRESS:
{insights}

STRICT OPERATIONAL RULES:
1. SCALE ADAPTATION: All impact estimates must be proportional to the current revenue of ${rev}[cite: 22].
2. NO HALLUCINATIONS: Do not suggest million-dollar growth for a company making thousands[cite: 23].
3. MICRO-BUSINESS SAFETY: If Total Cost is under $2,000, DO NOT suggest layoffs or headcount reduction. Focus on vendor renegotiation or subscription audits instead.
4. IMPACT FORMATTING: The "impact" field must be a string (e.g., "+$15.00" or "5% increase").
5. SURVIVAL MODE: If profit is negative, prioritize immediate cost-cutting over long-term growth.

Return ONLY JSON in this format:
{{
  "pricing": [{{"strategy": "string", "description": "string", "impact": "string"}}],
  "growth": [{{"strategy": "string", "description": "string", "impact": "string"}}],
  "cost_cutting": [{{"strategy": "string", "description": "string", "impact": "string"}}]
}}
"""
        return self.llm.generate_json(prompt)