class Agent:
    def __init__(self, code_name: str, clearance_level: int):
        self.code_name = code_name
        self.clearance_level = clearance_level

    def report(self ):
        print(f"agent {self.code_name}. clearance level {self.clearance_level}")

class Mission:
    def __init__(self, mission_name: str, target_location: str):
        self.mission_name = mission_name
        self.target_location = target_location

    def assin_agent(self, assined_agent: Agent):
        self.assined_agent = assined_agent

    def brief(self):
        print(f"mission: {self.mission_name}, target: {self.target_location}, agent: {self.assined_agent}")

