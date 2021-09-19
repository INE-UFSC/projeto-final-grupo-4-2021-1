from .BuffTarget import BuffTarget
from .DamageType import DamageType

class Buff:
    def __init__(self, multiplier: float, target: BuffTarget, type: DamageType):
        self.__multiplier = multiplier
        self.__target = target
        self.__type = type

    @property
    def multiplier(self):
        return self.__multiplier

    @property
    def target(self):
        return self.__target

    @property
    def type(self):
        return self.__type