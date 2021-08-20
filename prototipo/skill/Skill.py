from Effect import Effect
from typing import List

class Skill:
    def __init__(self, effects: List["Effect"], category: str):
        self.__effects = effects
        self.__category = category

    @property
    def effects(self):
        return self.__effects

    @property
    def category(self):
        return self.__category

    def use_skill(self, character: Fighter, enemy: Fighter):
        for effect in self.__effects:
            effect.apply_effect(character, enemy)
