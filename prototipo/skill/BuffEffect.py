from typing import Dict
from Effect import Effect
from EffectTarget import EffectTarget
from BuffTarget import BuffTarget
from DamageType import DamageType

class BuffEffect(Effect):
    def __init__(self, buff: Dict[BuffTarget, Dict[DamageType, float]], target: EffectTarget):
        super().init(target)
        self.__buff = buff

    @property
    def buff(self):
        return self.__buff