class Agent:
    def __init__(self, code_name: str, clearance_level: int):
        self.code_name = code_name
        self.clearance_level = clearance_level

    def report(self ):
        print(f"agent {self.code_name}. clearance level {self.clearance_level}")