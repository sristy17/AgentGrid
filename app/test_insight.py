from app.agents.data_agent import DataAgent
from app.agents.analytics_agent import AnalyticsAgent
from app.agents.insight_agent import InsightAgent

data_agent = DataAgent()
analytics_agent = AnalyticsAgent()
insight_agent = InsightAgent()

data = data_agent.run({})
analytics = analytics_agent.run(data)
insights = insight_agent.run(analytics)

print("ANALYTICS:", analytics)
print("INSIGHTS:", insights)