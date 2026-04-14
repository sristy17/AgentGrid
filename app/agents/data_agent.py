from app.core.agent_interface import Agent


class DataAgent(Agent):

    def run(self, input_data):
        if input_data and "data" in input_data:
            return input_data["data"]

        return [
            {"revenue": 100, "cost": 60},
            {"revenue": 200, "cost": 120},
            {"revenue": 150, "cost": 90}
        ]