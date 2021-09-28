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
        super().__init__(level, stats, hp, ap, equipment, skills, xp)

    @property
    def sprite(self):
        return self.__sprite

    def choose_skill(self):
        skill = list(filter(lambda skill: skill.cost <= self.ap.current and not skill.active_cooldown, self.skills))
        if skill:
            return choice(skill)
        return None

    def draw(self, surface):
        self.__sprite.draw(surface)

    # def use_skill(self):
    # super().use_skill(self.__behavior.choose_skill)
