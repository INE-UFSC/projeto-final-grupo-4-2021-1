from fighter.Fighter import Fighter
from fighter.Stats import Stats
from fighter.Resource import Resource
from item.Inventory import Inventory
from item.Equipment import Equipment
from skill.EffectTarget import EffectTarget
from skill.DamageEffect import DamageEffect
from skill.HealingEffect import HealingEffect
from skill.DamageType import DamageType
from skill.Skill import Skill
#importar inventário e equipamento

ATRIBUTE_POINTS_PER_LEVEL = 2

#buffs: dict[bufftarget, dict[DamageType, multiplier]]
class MainCharacter(Fighter):
    def __init__(self, stats: Stats, hp: Resource, ap: Resource, equipment: Equipment, buffs: dict, inventory: Inventory, exp: int, skills: list = []):
        self.__inventory = inventory
        self.__exp = exp
        super().__init__(stats, hp, ap, equipment, skills)

    @staticmethod
    def generate_test_character():
        return MainCharacter(Stats(10, 10, 10, 10), Resource(10, 10), Resource(2, 2), None, None, None, 0, [
            Skill([DamageEffect({DamageType.SLASHING: 2}, 100, 0, EffectTarget.ENEMY)], 1,"teste"),
            Skill([HealingEffect(2, EffectTarget.SELF)], 1,"teste")
            ])
    
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