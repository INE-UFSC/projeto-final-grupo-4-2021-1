from helpers.SingletonMeta import SingletonMeta
from fighter.opponent.Opponent import Opponent

from skill.EffectTarget import EffectTarget
from skill.DamageEffect import DamageEffect
from skill.HealingEffect import HealingEffect
from skill.DamageType import DamageType
from skill.Skill import Skill
from skill.BuffTarget import BuffTarget
from skill.BuffEffect import BuffEffect
from skill.PosionEffect import PoisonEffect
from skill.Buff import Buff

from display.components.LinearAnimation import LinearAnimation
from display.components.OpponentSprite import OpponentSprite
from item.Equipment import Equipment

from fighter.Stats import Stats
from fighter.Resource import Resource

class OpponentCreator:
    current: Opponent = None

    @staticmethod
    def create_dummy():
        stats = Stats()
        hp = Resource(1, 1)
        ap = Resource(1, 1)
        sprite = OpponentSprite("prototipo/assets/enemy_sprites/shrek.png")
        return Opponent(stats, hp, ap, Equipment.default_equipment(), sprite, None, None)


    @staticmethod
    def generate_test_opponent():
        stats = Stats(10, 10, 10, 10)
        hp = Resource(1000, 1000)
        ap = Resource(3, 3)
        sprite = OpponentSprite("prototipo/assets/enemy_sprites/slime3.png")
        basic_attack = Skill([DamageEffect(15, DamageType.PIERCING, 100, 0, EffectTarget.ENEMY)], 1,"teste", "prototipo/assets/fire_icon.png")
        OpponentCreator.current = Opponent(stats, hp, ap, Equipment.default_equipment(), sprite, None, [basic_attack])
        OpponentCreator.current.add_buff(Buff(0.5, BuffTarget.RESISTANCE, DamageType.FIRE))

    