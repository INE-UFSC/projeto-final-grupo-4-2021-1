from skill.DamageEffect import DamageEffect
from skill.Skill import Skill
from skill.EffectTarget import  EffectTarget
from skill.DamageType import DamageType
from fighter.Fighter import Fighter
from fighter.Stats import Stats
from fighter.Resource import Resource
from .OpponentInfo import OpponentInfo
from .Behavior import Behavior
from item.Equipment import Equipment

#buffs: dict[bufftarget, dict[DamageType, multiplier]]
class Opponent(Fighter):
    def __init__(self, stats: Stats, hp: Resource, ap: Resource, equipment: Equipment, info: OpponentInfo, behavior: Behavior, skills: list = []):
        self.__info = info
        self.__behavior = behavior
        super().__init__(stats, hp, ap, equipment, skills)

    @staticmethod
    def generate_test_opponent():
        return Opponent(Stats(10, 10, 10, 10), Resource(10, 10), Resource(1, 1), None, None, None, [Skill([DamageEffect({DamageType.SLASHING: 1}, 100, 0, EffectTarget.ENEMY)], "teste")])

    @property
    def info(self):
        return self.__info

    @property
    def behavior(self):
        return self.__behavior

    #def use_skill(self):
        #super().use_skill(self.__behavior.choose_skill)

