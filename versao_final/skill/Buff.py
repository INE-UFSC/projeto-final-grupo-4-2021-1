from .BuffTarget import BuffTarget
from .DamageType import DamageType

class Buff:
    def __init__(self, multiplier: float, target: BuffTarget, type: DamageType):
        self.__multiplier = multiplier
        self.__target = target
        self.__type = type

    def __eq__(self, other):
        if not isinstance(other, Buff):
            return NotImplemented

        return self.multiplier == other.multiplier and self.target == other.target and self.type == other.type

    @property
    def multiplier(self):
        return self.__multiplier

    @property
    def target(self):
        return self.__target

    @property
    def type(self):
        return self.__type