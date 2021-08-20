from abc import ABC, abstractmethod
from .BehaviorType import BehaviorType


class Behavior(ABC):
    def __init__(self, behaviorType: BehaviorType):
        self.__behavior = behaviorType

    @property
    def behavior(self):
        return self.__behavior

    @abstractmethod
    def choose_skill():
        pass

    @abstractmethod
    def plan_action():
        pass