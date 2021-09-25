from abc import ABC, abstractmethod
from copy import deepcopy
from .EffectTarget import EffectTarget
from .Effect import Effect


class LingeringEffect(Effect, ABC):
    def __init__(self, duration: int, target: EffectTarget):
        super().__init__(target)
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value

    @abstractmethod
    def apply_effect(self, user, enemy):
        pass

    @abstractmethod
    def update(self, attached_to):
        return not self.__duration == 0

    def attach(self, user, enemy):
        if self.target == EffectTarget.SELF:
            user.add_lingering_effect(deepcopy(self))
        elif self.target == EffectTarget.ENEMY:
            enemy.add_lingering_effect(deepcopy(self))
        else:
            user.add_lingering_effect(deepcopy(self))
            enemy.add_lingering_effect(deepcopy(self))
