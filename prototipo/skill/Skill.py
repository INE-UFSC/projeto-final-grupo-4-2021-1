from .Effect import Effect
from typing import List

class Skill:
    def __init__(self, effects: List["Effect"], cost: int,category: str):
        self.__effects = effects
        self.__cost = cost
        self.__category = category

    @property
    def effects(self):
        return self.__effects

    @property
    def cost(self):
        return self.__cost

    @property
    def category(self):
        return self.__category