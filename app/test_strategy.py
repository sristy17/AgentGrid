from app.agents.data_agent import DataAgent
from app.agents.analytics_agent import AnalyticsAgent
from app.agents.insight_agent import InsightAgent
from app.agents.strategy_agent import StrategyAgent

data_agent = DataAgent()
analytics_agent = AnalyticsAgent()
insight_agent = InsightAgent()
strategy_agent = StrategyAgent()

data = data_agent.run({})
analytics = analytics_agent.run(data)
insights = insight_agent.run(analytics)
strategy = strategy_agent.run(insights)

print("INSIGHTS:", insights)
print("STRATEGY:", strategy)
