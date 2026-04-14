from app.agents.data_agent import DataAgent
from app.agents.analytics_agent import AnalyticsAgent
from app.agents.insight_agent import InsightAgent
from app.agents.strategy_agent import StrategyAgent
from app.models.response_schema import AnalyzeResponse
from app.core.logger import log


class Orchestrator:

    def __init__(self):
        self.data_agent = DataAgent()
        self.analytics_agent = AnalyticsAgent()
        self.insight_agent = InsightAgent()
        self.strategy_agent = StrategyAgent()

    def run(self, input_data):
        try:
            # Step 1: Data
            log("Running Data Agent")
            data = self.data_agent.run(input_data)

            # Step 2: Analytics
            log("Running Analytics Agent", data)
            analytics = self.analytics_agent.run(data)

            # EDGE CASE: No activity
            if analytics["revenue"] == 0 and analytics["cost"] == 0:
                log("No business activity detected")

                response = {
                    "data": data,
                    "analytics": analytics,
                    "insights": {
                        "problems": [
                            {
                                "type": "No Activity",
                                "description": "No revenue or cost data available"
                            }
                        ],
                        "reasons": [
                            {
                                "problem": "No Activity",
                                "reason": "Business has not recorded any transactions"
                            }
                        ]
                    },
                    "strategy": {
                        "pricing": [],
                        "growth": [],
                        "cost_cutting": []
                    }
                }

                return AnalyzeResponse(**response).model_dump()

            # Step 3: Insights
            log("Running Insight Agent", analytics)
            insights = self.insight_agent.run(analytics)

            # GUARDRAIL: Skip strategy if no revenue or profit
            if analytics["revenue"] <= 0 or analytics["profit"] <= 0:
                log("Skipping Strategy Agent due to insufficient data")

                response = {
                    "data": data,
                    "analytics": analytics,
                    "insights": insights,
                    "strategy": {
                        "pricing": [],
                        "growth": [],
                        "cost_cutting": []
                    }
                }

                return AnalyzeResponse(**response).model_dump()

            # Step 4: Strategy
            log("Running Strategy Agent", insights)
            strategy = self.strategy_agent.run(insights)

            # Final Response
            response = {
                "data": data,
                "analytics": analytics,
                "insights": insights,
                "strategy": strategy
            }

            # Validate response
            return AnalyzeResponse(**response).model_dump()

        except Exception as e:
            log("ERROR", str(e))
            raise Exception("Pipeline failed")