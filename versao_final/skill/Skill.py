from display.components.Animation import Animation
from typing import List


class Skill:
    def __init__(self, effects: list, cost: int, cooldown: int, category: str, icon_path: str,
                 main_char_animation: Animation = None, opponent_animation: Animation = None):
        self.__effects = effects
        self.__cost = cost
        self.__category = category
        self.__icon_path = icon_path
        self.__cooldown = cooldown
        self.__main_char_animation = main_char_animation
        self.__opponent_animation = opponent_animation
        self.__active_cooldown = 0

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
    def cooldown(self):
        return self.__cooldown

    @property
    def main_char_animation(self):
        return self.__main_char_animation

    @property
    def opponent_animation(self):
        return self.__opponent_animation

    @property
    def active_cooldown(self):
        return self.__active_cooldown

    def use(self, user, enemy):
        if not self.__active_cooldown:
            self.__active_cooldown = self.__cooldown
            for effect in self.__effects:
                effect.apply_effect(user, enemy)

    def cooldown_reset(self):
        self.__active_cooldown = 0

    def update_cooldown(self):
        if self.__active_cooldown == 0:
            return True

        self.__active_cooldown -= 1
