from app.core.agent_interface import Agent

class AnalyticsAgent(Agent):

    def run(self, data):
        revenue = sum(d["revenue"] for d in data)
        cost = sum(d["cost"] for d in data)

        return {
            "revenue": revenue,
            "cost": cost,
            "profit": revenue - cost
        }