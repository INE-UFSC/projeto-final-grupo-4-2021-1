from .Effect import Effect
from display.Animation import Animation
from typing import List

class Skill:
    def __init__(self, effects: List["Effect"], cost: int, category: str, icon_path: str, main_char_animation: Animation = None, opponent_animation: Animation = None):
        self.__effects = effects
        self.__cost = cost
        self.__category = category
        self.__icon_path = icon_path

        self.__main_char_animation = main_char_animation
        self.__opponent_animation = opponent_animation

    @property
    def effects(self):
        return self.__effects

    @property
    def cost(self):
        return self.__cost

    @property
    def category(self):
        return self.__category

    @property
    def icon_path(self):
        return self.__icon_path

    @property
    def main_char_animation(self):
        return self.__main_char_animation

    @property
    def opponent_animation(self):
        return self.__opponent_animation