from typing import Dict
from Effect import Effect
from EffectTarget import EffectTarget
from DamageType import DamageType

class DamageEffect(Effect):
    def __init__(self, damage: Dict[DamageType, int], accuracy: int, crit_chance: int, target: EffectTarget):
        super().init(target)
        self.__damage = damage
        self.__accuracy = accuracy
        self.__crit_chance = crit_chance

    @property
    def damage(self):
        return self.__damage
    
    @property
    def accuracy(self):
        return self.__accuracy

    @property
    def crit_chance(self):
        return self.__crit_chance