from random import choice
from display.components.OpponentSprite import OpponentSprite
from fighter.Fighter import Fighter
from fighter.Stats import Stats
from fighter.Resource import Resource
from item.Equipment import Equipment


# buffs: dict[bufftarget, dict[DamageType, multiplier]]
class Opponent(Fighter):
    def __init__(self, level, xp, stats: Stats, hp: Resource, ap: Resource, equipment: Equipment,
                 sprite: OpponentSprite, skills: list = []):
        self.__sprite = sprite
        self.__xp = xp
        super().__init__(level, stats, hp, ap, equipment, skills)

    @property
    def info(self):
        return self.__info

    @property
    def xp(self):
        return self.__xp

    @property
    def behavior(self):
        return self.__behavior

    @property
    def sprite(self):
        return self.__sprite

    def choose_skill(self):
        skill = list(filter(lambda skill: skill.cost <= self.ap.current, self.skills))
        if skill:
            return choice(skill)
        return None

    def use_skill(self, skill, target):
        skill.use(self, target)

    def draw(self, surface):
        self.__sprite.draw(surface)

    # def use_skill(self):
    # super().use_skill(self.__behavior.choose_skill)
