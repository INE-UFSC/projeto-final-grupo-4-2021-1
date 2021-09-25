import os, random
from fighter.opponent.Opponent import Opponent
from fighter.main_character.MainCharacter import MainCharacter
from skill.EffectTarget import EffectTarget
from skill.DamageEffect import DamageEffect
from skill.DamageType import DamageType
from skill.Skill import Skill
from .SkillCreator import SkillCreator
from display.components.LinearAnimation import LinearAnimation
from display.components.OpponentSprite import OpponentSprite
from item.Equipment import Equipment
from fighter.Stats import Stats
from fighter.Resource import Resource


class OpponentCreator:
    current: Opponent = None

    def generate_enemy(self):
        level = MainCharacter().level
        random_number = random.randrange(0, 100)
        if level < 10:
            OpponentCreator.current = self.__generate_common_enemy(level)
        elif level < 20:
            if random_number < 60:
                OpponentCreator.current = self.__generate_common_enemy(level)
            else:
                OpponentCreator.current = self.__generate_rare_enemy(level)
        elif level < 50:
            if random_number < 60:
                OpponentCreator.current = self.__generate_rare_enemy(level)
            else:
                OpponentCreator.current = self.__generate_mythic_enemy(level)
        else:
            OpponentCreator.current = self.__generate_mythic_enemy(level)

    @staticmethod
    def create_dummy():
        level = 1
        xp = 600
        stats = Stats(0, 0, 0, 0)
        hp = Resource(1000)
        ap = Resource(2)
        sprite_path = "versao_final/assets/enemy_sprites/common/" + random.choice(
            os.listdir("versao_final/assets/enemy_sprites/common/"))
        sprite = OpponentSprite(sprite_path)
        skills = random.sample(SkillCreator.create_skills(), 1)

        Skill(
            [DamageEffect(random.randrange(8, 18), random.choice(list(DamageType)), random.randrange(80, 100),
                          random.randrange(10), EffectTarget.ENEMY)],
            1, 0, "Basic attack", None)
        return Opponent(level, xp, stats, hp, ap, Equipment.default_equipment(), sprite, skills)

    @staticmethod
    def __generate_common_enemy(level: int):
        level = 1
        xp = 300
        stats = Stats(*[random.randrange(5, 10) + level for i in range(4)])
        hp = Resource(random.randrange(300, 500))
        ap = Resource(2)
        sprite_path = "versao_final/assets/enemy_sprites/common/" + random.choice(
            os.listdir("versao_final/assets/enemy_sprites/common/"))
        sprite = OpponentSprite(sprite_path)

        skills = random.sample(SkillCreator.create_skills(), 2)

        # basic_skill = Skill(
        #     [DamageEffect(random.randrange(8, 18), random.choice(list(DamageType)), random.randrange(80, 100), random.randrange(10), EffectTarget.ENEMY)],
        #     1, 0, "Basic attack", None)
        return Opponent(level, xp, stats, hp, ap, Equipment.default_equipment(), sprite, skills)

    @staticmethod
    def __generate_rare_enemy(level: int):
        level = 2
        xp = 600
        stats = Stats(*[random.randrange(10, 20) + level for i in range(4)])
        hp = Resource(random.randrange(500, 1000))
        ap = Resource(2)
        sprite_path = "versao_final/assets/enemy_sprites/rare/" + random.choice(
            os.listdir("versao_final/assets/enemy_sprites/rare/"))
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
        return Opponent(level, xp, stats, hp, ap, Equipment.default_equipment(), sprite, skills)

    @staticmethod
    def __generate_mythic_enemy(level: int):
        xp = 1200
        stats = Stats(*[random.randrange(20, 30) + level for i in range(4)])
        hp = Resource(random.randrange(1000, 2000))
        ap = Resource(2)
        sprite_path = "versao_final/assets/enemy_sprites/mythic/" + random.choice(
            os.listdir("versao_final/assets/enemy_sprites/mythic/"))
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
        return Opponent(level, xp, stats, hp, ap, Equipment.default_equipment(), sprite, skills)
