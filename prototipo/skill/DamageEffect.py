from typing import Dict
from .Effect import Effect
from .EffectTarget import EffectTarget
from .DamageType import DamageType

class DamageEffect(Effect):
    def __init__(self, value: float, type: DamageType, accuracy: int, crit_chance: int, target: EffectTarget):
        super().__init__(target)
        self.__value = value
        self.__type = type
        self.__accuracy = accuracy
        self.__crit_chance = crit_chance

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
    
    @property
    def accuracy(self):
        return self.__accuracy

    @accuracy.setter
    def accuracy(self, accuracy):
        self.__accuracy = accuracy

    @property
    def crit_chance(self):
        return self.__crit_chance

    @property
    def type(self):
        return self.__type