from fighter.Fighter import Fighter
from fighter.Stats import Stats
from fighter.Resource import Resource
from item.Inventory import Inventory
from item.Equipment import Equipment
#importar inventário e equipamento

ATRIBUTE_POINTS_PER_LEVEL = 2

#buffs: dict[bufftarget, dict[DamageType, multiplier]]
class MainCharacter(Fighter):
    def __init__(self, stats: Stats, hp: Resource, ap: Resource, equipment: Equipment, buffs: dict, inventory: Inventory, exp: int, skills: list = []):
        self.__inventory = inventory
        self.__exp = exp
        super().__init__(stats, hp, ap, equipment, buffs, skills)
    
    @property
    def inventory(self):
        return self.__inventory

    @property
    def exp(self):
        return self.__exp

    #@inventory.setter
    #def inventory(self, inventory):
    #    self.__inventory = inventory


    def increase_exp(self, amount):
        "Increases the current EXP by the specified amount"
        self.__exp += amount

    #Implementar mensagem de level up 
    def level_up(self):
        self.stats.add_availablePoints(ATRIBUTE_POINTS_PER_LEVEL)