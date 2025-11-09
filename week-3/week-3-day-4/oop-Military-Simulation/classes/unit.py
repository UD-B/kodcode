from classes.soldier import Soldier

class Unit:
    def __init__(self, unit_name: str, commander: Soldier, soldiers: list[Soldier]):
        self.unit_name = unit_name
        self.commander = commander
        self.soldiers = soldiers
        

    def briefing(self):
        print({"unit name": self.unit_name, "commander's details": self.commander.report()})