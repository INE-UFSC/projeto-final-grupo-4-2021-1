import pygame

from skill.EffectTarget import EffectTarget
from skill.DamageEffect import DamageEffect
from skill.HealingEffect import HealingEffect
from skill.BuffEffect import BuffEffect
from skill.BuffTarget import BuffTarget
from skill.Buff import Buff
from skill.DamageType import DamageType
from skill.Skill import Skill
from display.components.LinearAnimation import LinearAnimation

class SkillCreator():
    @staticmethod
    def create_skills():
        skills = []
        screen = pygame.display.get_surface().get_rect()

        #FIRE BALL
        fire_ball_surface = SkillCreator.make_surface("prototipo/assets/skill_sprites/fire_ball.png")
        animation = SkillCreator.create_spell_animation(fire_ball_surface, screen)
        enemy_animation = SkillCreator.create_enemy_spell_animation(fire_ball_surface, screen)

        skills.append(Skill([DamageEffect(100, DamageType.FIRE, 100, 0, EffectTarget.ENEMY)], 1, 1, "FIRE BALL!!!", "prototipo/assets/skill_icons/fireball-red-1.png", animation, enemy_animation))

        #FORTIFY SKILL
        skills.append(Skill([HealingEffect(80, EffectTarget.SELF), BuffEffect(Buff(0.2, BuffTarget.RESISTANCE, DamageType.ALL), 2, EffectTarget.SELF)], 1, 2, "Heal and resistance", "prototipo/assets/skill_icons/heal-jade-1.png", None))

        #SLASH ATTACK
        sword_surface = SkillCreator.make_surface("prototipo/assets/skill_sprites/slash.png", (600, 600))
        animation = SkillCreator.create_slash_animation(sword_surface, screen)
        enemy_animation = SkillCreator.create_enemy_spell_animation(sword_surface, screen)

        skills.append(Skill([DamageEffect(240, DamageType.SLASHING, 100, 10, EffectTarget.ENEMY)], 2, 3, "Slashing", "prototipo/assets/skill_icons/slash.png", animation, enemy_animation))

        #EARTH ATTACK
        rock_surface = SkillCreator.make_surface("prototipo/assets/skill_sprites/rock.png")
        animation = SkillCreator.create_spell_animation(rock_surface, screen)
        enemy_animation = SkillCreator.create_enemy_spell_animation(rock_surface, screen)

        skills.append(Skill([DamageEffect(100, DamageType.EARTH, 100, 0, EffectTarget.ENEMY)], 1, 1, "Flying stone!", "prototipo/assets/skill_icons/stone.png", animation, enemy_animation))
        
        #METEOR ATTACK
        meteor_surface = SkillCreator.make_surface("prototipo/assets/skill_sprites/meteor.png", (250, 373))
        animation = SkillCreator.create_spell_animation(meteor_surface, screen)
        enemy_animation = SkillCreator.create_enemy_spell_animation(meteor_surface, screen)

        skills.append(Skill([DamageEffect(150, DamageType.EARTH, 100, 0, EffectTarget.ENEMY), DamageEffect(250, DamageType.FIRE, 100, 0, EffectTarget.ENEMY)], 4, 6, "FLYING FLAMING STOOOONE!!!", "prototipo/assets/skill_icons/meteor.png", animation, enemy_animation))

        return skills

    @staticmethod
    def create_spell_animation(surface, screen):
        return LinearAnimation(surface, surface.get_rect(topright = (screen.width, screen.height)), surface.get_rect(center = (screen.center)), 60)

    @staticmethod
    def create_enemy_spell_animation(surface, screen):
        return LinearAnimation(surface, surface.get_rect(center = screen.center), surface.get_rect(midtop = screen.midbottom), 60)

    @staticmethod
    def create_slash_animation(surface, screen):
        return LinearAnimation(surface, surface.get_rect(topright = (screen.width, 0)), surface.get_rect(bottomleft = (0, screen.height)), 5)

    @staticmethod
    def make_surface(path, size = None):
        surface = pygame.image.load(path).convert_alpha()

        if size:
            return pygame.transform.scale(surface, size)
        else:
            return surface