from app.agents.data_agent import DataAgent
from app.agents.analytics_agent import AnalyticsAgent
from app.agents.insight_agent import InsightAgent
from app.agents.strategy_agent import StrategyAgent


class Orchestrator:

    def __init__(self):
        self.data_agent = DataAgent()
        self.analytics_agent = AnalyticsAgent()
        self.insight_agent = InsightAgent()
        self.strategy_agent = StrategyAgent()

    def run(self, input_data):
        # Step 1: Data
        data = self.data_agent.run(input_data)

        # Step 2: Analytics
        analytics = self.analytics_agent.run(data)

        # Step 3: Insights
        insights = self.insight_agent.run(analytics)

        # Step 4: Strategy
        strategy = self.strategy_agent.run(insights)

        return {
            "data": data,
            "analytics": analytics,
            "insights": insights,
            "strategy": strategy
        }