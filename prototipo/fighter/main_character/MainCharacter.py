from fighter.Fighter import Fighter, CombatStatus
from fighter.Stats import Stats
from fighter.Resource import Resource
from item.Inventory import Inventory
from item.Equipment import Equipment
from skill.EffectTarget import EffectTarget
from skill.DamageEffect import DamageEffect
from skill.HealingEffect import HealingEffect
from skill.DamageType import DamageType
from skill.Skill import Skill
from skill.BuffTarget import BuffTarget
from skill.BuffEffect import BuffEffect
#importar inventário e equipamento

ATRIBUTE_POINTS_PER_LEVEL = 2

#buffs: dict[bufftarget, dict[DamageType, multiplier]]
class MainCharacter(Fighter):
    def __init__(self, stats: Stats, hp: Resource, ap: Resource, equipment: Equipment, buffs: dict, inventory: Inventory, exp: int, skills: list = [], combat_status = {}):
        self.__inventory = inventory
        self.__exp = exp
        super().__init__(stats, hp, ap, equipment, skills, combat_status)

    @staticmethod
    def generate_test_character():
        main_char = MainCharacter(Stats(10, 10, 10, 10), Resource(100, 100), Resource(5, 0), None, None, None, 0, [
            Skill([DamageEffect(10, DamageType.SLASHING, 100, 0, EffectTarget.ENEMY)], 1,"teste", "prototipo/assets/fire_icon.png"),
            Skill([DamageEffect(100, DamageType.FIRE, 100, 0, EffectTarget.ENEMY), CombatStatus(1, EffectTarget.ENEMY, 2, Skill([DamageEffect(10, DamageType.FIRE, 100, 1, EffectTarget.ENEMY)], 0, "BURNING DAMAGE", None))], 1,"BURNING", "prototipo/assets/fire_icon.png"),
            Skill([HealingEffect(2, EffectTarget.SELF)], 1,"teste", "prototipo/assets/fire_icon.png")            
            ])

        #main_char.add_buff(BuffEffect({BuffTarget.DAMAGE: {DamageType.SLASHING: 0.1, DamageType.FIRE: 0.5}}, EffectTarget.BOTH))
        main_char.add_buff(BuffEffect(BuffTarget.DAMAGE, DamageType.FIRE, 0.5, EffectTarget.BOTH))
        return main_char
    
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