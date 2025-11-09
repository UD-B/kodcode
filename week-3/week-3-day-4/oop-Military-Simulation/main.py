from classes.weapon_option import Tank, Drone
from classes.weapon import Weapon
from classes.soldier import Soldier
from classes.unit import Unit


drone_0 = Drone("ud drone", 10000)
tank_0 = Tank("ud tank", 100)

m16 = Weapon('m16', 29)
soldier = Soldier("ud", "commander", m16)
soldier1 = Soldier("1", "turay", m16)
soldier2 = Soldier("2", "turay", m16)
soldier3 = Soldier("3", "turay", m16)
unit_7160 = Unit('7160', soldier,[soldier1, soldier2, soldier3] )
print(unit_7160.briefing())