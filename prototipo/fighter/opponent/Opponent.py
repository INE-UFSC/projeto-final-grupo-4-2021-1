from skill.Buff import Buff
from display.components.OpponentSprite import OpponentSprite
from skill.DamageEffect import DamageEffect
from skill.Skill import Skill
from skill.EffectTarget import  EffectTarget
from skill.DamageType import DamageType
from skill.BuffTarget import BuffTarget
from fighter.Fighter import Fighter
from fighter.Stats import Stats
from fighter.Resource import Resource
from .OpponentInfo import OpponentInfo
from .Behavior import Behavior
from item.Equipment import Equipment
from helpers.SingletonMeta import ABCSingletonMeta


#buffs: dict[bufftarget, dict[DamageType, multiplier]]
class Opponent(Fighter, metaclass=ABCSingletonMeta):
    def __init__(self, stats: Stats, hp: Resource, ap: Resource, equipment: Equipment, sprite: OpponentSprite, behavior: Behavior, skills: list = []):
        self.__behavior = behavior
        self.__sprite = sprite
        super().__init__(stats, hp, ap, equipment, skills)

    @staticmethod
    def generate_test_opponent():
        stats = Stats(10, 10, 10, 10)
        hp = Resource(1000, 1000)
        ap = Resource(3, 3)
        sprite = OpponentSprite("prototipo/assets/enemy_sprites/slime3.png")
        basic_attack = Skill([DamageEffect(15, DamageType.PIERCING, 100, 0, EffectTarget.ENEMY)], 1,"teste", "prototipo/assets/fire_icon.png")
        opponent = Opponent(stats, hp, ap, Equipment.default_equipment(), sprite, None, [basic_attack])
        opponent.add_buff(Buff(0.5, BuffTarget.RESISTANCE, DamageType.FIRE))

    @property
    def info(self):
        return self.__info

    @property
    def behavior(self):
        return self.__behavior

    @property
    def sprite(self):
        return self.__sprite

    def draw(self, surface):
        self.__sprite.draw(surface)

    #def use_skill(self):
        #super().use_skill(self.__behavior.choose_skill)

