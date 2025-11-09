from classes.weapon_option import Tank, Drone

class Weapon:
    def __init__(self, name: str, ammo: int):
        self.name = name
        self.ammo = ammo
        self.total_weapons = 0

    def __str__(self):
        return self.name, self.ammo