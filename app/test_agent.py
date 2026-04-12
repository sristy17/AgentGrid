from app.agents.data_agent import DataAgent
from app.agents.analytics_agent import AnalyticsAgent

data_agent = DataAgent()
analytics_agent = AnalyticsAgent()

data = data_agent.run({})
analytics = analytics_agent.run(data)

print("DATA:", data)
print("ANALYTICS:", analytics)