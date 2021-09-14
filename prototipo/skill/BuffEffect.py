from typing import Dict
from .Effect import Effect
from .EffectTarget import EffectTarget
from .BuffTarget import BuffTarget
from .DamageType import DamageType

class BuffEffect(Effect):
    def __init__(self, buffTarget: BuffTarget, damageType: DamageType, multiplier: float, target: EffectTarget):
        super().__init__(target)
        self.__buffTarget = buffTarget
        self.__damageType = damageType
        self.__multiplier = multiplier

    @property
    def buff(self):
        return self.__buff

    @property
    def buffTarget(self):
        return self.__buffTarget

    @property
    def damageType(self):
        return self.__damageType

    @property
    def multiplier(self):
        return self.__multiplier