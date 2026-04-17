from app.agents.data_agent import DataAgent
from app.agents.analytics_agent import AnalyticsAgent
from app.agents.insight_agent import InsightAgent
from app.agents.strategy_agent import StrategyAgent
from app.models.response_schema import AnalyzeResponse
from app.core.logger import log
from app.db.database import SessionLocal
from app.db.models import AnalysisRun

class Orchestrator:

    def __init__(self):
        self.data_agent = DataAgent()
        self.analytics_agent = AnalyticsAgent()
        self.insight_agent = InsightAgent()
        self.strategy_agent = StrategyAgent()

    def _calculate_trend(self, current, previous):
        """Helper to calculate changes and percentages safely in Python."""
        def get_pct(curr, prev):
            if prev == 0:
                return 0
            return round(((curr - prev) / prev) * 100, 2)

        return {
            "revenue_change": current["revenue"] - previous["revenue"],
            "revenue_pct": get_pct(current["revenue"], previous["revenue"]),
            "cost_change": current["cost"] - previous["cost"],
            "cost_pct": get_pct(current["cost"], previous["cost"]),
            "profit_change": current["profit"] - previous["profit"],
            "profit_pct": get_pct(current["profit"], previous["profit"])
        }

    def run(self, input_data):
        try:
            # 1. Data Ingestion
            log("Running Data Agent")
            data = self.data_agent.run(input_data)

            # 2. Analytics Calculation
            log("Running Analytics Agent", data)
            analytics = self.analytics_agent.run(data)

            # Early Exit: No Activity
            if analytics["revenue"] == 0 and analytics["cost"] == 0:
                return self._format_empty_response(data, analytics)

            # 3. Database & Trend Logic
            trend = None
            with SessionLocal() as db:
                last_run = db.query(AnalysisRun)\
                    .order_by(AnalysisRun.id.desc())\
                    .first()
                
                if last_run and last_run.analytics:
                    trend = self._calculate_trend(analytics, last_run.analytics)

            # 4. Insights Generation
            log("Running Insight Agent", analytics)
            insights = self.insight_agent.run(analytics, trend)

            if analytics["revenue"] <= 0 or analytics["profit"] <= 0:
                response = {
                    "data": data,
                    "analytics": analytics,
                    "insights": insights,
                    "strategy": {"pricing": [], "growth": [], "cost_cutting": []}
                }
                return AnalyzeResponse(**response).model_dump()

            # 5. Strategy Generation
            log("Running Strategy Agent", insights)
            strategy = self.strategy_agent.run(insights, analytics) 

            # 6. Final Construction
            response = {
                "data": data,
                "analytics": analytics,
                "insights": insights,
                "strategy": strategy
            }

            return AnalyzeResponse(**response).model_dump()

        except Exception as e:
            log("ERROR", str(e))
            raise Exception(f"Pipeline failed: {str(e)}")

    def _format_empty_response(self, data, analytics):
        """Standardizes the response for cases with no transaction data."""
        response = {
            "data": data,
            "analytics": analytics,
            "insights": {
                "problems": [{"type": "No Activity", "description": "No revenue or cost data available"}],
                "reasons": [{"problem": "No Activity", "reason": "Business has not recorded any transactions"}]
            },
            "strategy": {"pricing": [], "growth": [], "cost_cutting": []}
        }
        return AnalyzeResponse(**response).model_dump()