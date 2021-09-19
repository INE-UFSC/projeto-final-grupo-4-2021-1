from abc import ABC, abstractmethod
from .EffectTarget import EffectTarget

class Effect(ABC):
    def __init__(self, target: EffectTarget):
        self.__target = target

    @property
    def target(self):
        return self.__target

    @abstractmethod
    def apply_effect(self, user, enemy):
        pass