import os, random

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
from .SkillCreator import SkillCreator

from display.components.LinearAnimation import LinearAnimation
from display.components.OpponentSprite import OpponentSprite
from item.Equipment import Equipment

from fighter.Stats import Stats
from fighter.Resource import Resource

class OpponentCreator:
    current: Opponent = None

    def generate_enemy(self):
        OpponentCreator.current = self.__generate_rare_enemy()

    @staticmethod
    def create_dummy():
        level = 1
        xp = 600
        stats = Stats(0,0,0,0)
        hp = Resource(1000)
        ap = Resource(2)
        sprite_path = "prototipo/assets/enemy_sprites/common/" + random.choice(os.listdir("prototipo/assets/enemy_sprites/common/"))
        sprite = OpponentSprite(sprite_path)
        skills = random.sample(SkillCreator.create_skills(), 1)
        
        Skill(
            [DamageEffect(random.randrange(8, 18), random.choice(list(DamageType)), random.randrange(80, 100), random.randrange(10), EffectTarget.ENEMY)],
            1, 0, "Basic attack", None)
        return Opponent(level, xp, stats, hp, ap, Equipment.default_equipment(), sprite, None, skills)
        
    @staticmethod
    def __generate_common_enemy():
        level = 1
        xp = 600
        stats = Stats(*[random.randrange(5, 15) for i in range(4)])
        hp = Resource(random.randrange(800, 1200))
        ap = Resource(2)
        sprite_path = "prototipo/assets/enemy_sprites/common/" + random.choice(os.listdir("prototipo/assets/enemy_sprites/common/"))
        sprite = OpponentSprite(sprite_path)

        skills = random.sample(SkillCreator.create_skills(), 2)

        # basic_skill = Skill(
        #     [DamageEffect(random.randrange(8, 18), random.choice(list(DamageType)), random.randrange(80, 100), random.randrange(10), EffectTarget.ENEMY)],
        #     1, 0, "Basic attack", None)
        return Opponent(level, xp, stats, hp, ap, Equipment.default_equipment(), sprite, None, skills)

    @staticmethod
    def __generate_rare_enemy():
        level = 2
        xp = 1000
        stats = Stats(*[random.randrange(10, 20) for i in range(4)])
        hp = Resource(random.randrange(1200, 1500))
        ap = Resource(2)
        sprite_path = "prototipo/assets/enemy_sprites/rare/" + random.choice(os.listdir("prototipo/assets/enemy_sprites/rare/"))
        sprite = OpponentSprite(sprite_path)
        skills = random.sample(SkillCreator.create_skills(), 4)


        # basic_skill = Skill(
        #     [DamageEffect(random.randrange(10, 20), random.choice(list(DamageType)), random.randrange(80, 100), random.randrange(10), EffectTarget.ENEMY)],
        #     1, 0, "Basic attack", None)
        # special_skill = Skill(
        #     [DamageEffect(random.randrange(15, 30), random.choice(list(DamageType)), random.randrange(80, 100), random.randrange(10), EffectTarget.ENEMY)],
        #     2, 2, "Special attack", None)
        # healing_skill = Skill(
        #     [HealingEffect(30, EffectTarget.SELF)], 
        #     1, 2, "Healing effect", None
        # )
        return Opponent(level, xp, stats, hp, ap, Equipment.default_equipment(), sprite, None, skills)

    @staticmethod
    def __generate_mythic_enemy():
        level = 1
        xp = 800
        stats = Stats(*[random.randrange(15, 30) for i in range(4)])
        hp = Resource(random.randrange(1500, 2000))
        ap = Resource(2)
        sprite_path = "prototipo/assets/enemy_sprites/mythic/" + random.choice(os.listdir("prototipo/assets/enemy_sprites/mythic/"))
        sprite = OpponentSprite(sprite_path)
        skills = skills = random.sample(SkillCreator.create_skills(), 5)



        # basic_skill = Skill(
        #     [DamageEffect(random.randrange(15, 30), random.choice(list(DamageType)), random.randrange(80, 100), random.randrange(10), EffectTarget.ENEMY)],
        #     1, 0, "Basic attack", None)
        # special_skill = Skill(
        #     [DamageEffect(random.randrange(20, 40), random.choice(list(DamageType)), random.randrange(80, 100), random.randrange(10), EffectTarget.ENEMY)],
        #     2, 2, "Special attack", None)
        # healing_skill = Skill(
        #     [HealingEffect(40, EffectTarget.SELF)], 
        #     1, 2, "Healing effect", None
        # )
        # buff_skill = Skill(
        #     [BuffEffect(Buff(0.2, BuffTarget.DAMAGE, DamageType.ALL))],
        #     1, 3, "Damage buff", None
        # )
        return Opponent(level, xp, stats, hp, ap, Equipment.default_equipment(), sprite, None, skills)
