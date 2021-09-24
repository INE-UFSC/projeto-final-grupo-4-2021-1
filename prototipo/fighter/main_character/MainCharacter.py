from helpers.SingletonMeta import ABCSingletonMeta
from fighter.Fighter import Fighter
from fighter.Stats import Stats
from fighter.Resource import Resource
from item.Inventory import Inventory
from item.Equipment import Equipment

ATRIBUTE_POINTS_PER_LEVEL = 2

class MainCharacter(Fighter, metaclass=ABCSingletonMeta):
    def __init__(self, stats: Stats, hp: Resource, ap: Resource, equipment: Equipment, inventory: Inventory, exp: int, skills: list = []):
        self.__inventory = inventory
        self.__equipment = equipment
        self.__exp = exp
        super().__init__(stats, hp, ap, equipment, skills)

    
    @property
    def inventory(self):
        return self.__inventory

    @property
    def equipment(self):
        return self.__equipment

    @property
    def exp(self):
        return self.__exp

    def increase_exp(self, amount):
        "Increases the current EXP by the specified amount"
        self.__exp += amount

    def level_up(self):
        for stat in self.stats.stats.keys():
            self.stats.upgrade_stat(stat)
