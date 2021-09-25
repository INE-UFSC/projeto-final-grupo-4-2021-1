import pygame

from skill.EffectTarget import EffectTarget
from skill.DamageEffect import DamageEffect
from skill.HealingEffect import HealingEffect
from skill.DamageType import DamageType
from skill.Skill import Skill
from skill.BuffTarget import BuffTarget
from skill.BuffEffect import BuffEffect
from display.components.LinearAnimation import LinearAnimation
from item.Weapon import Weapon
from item.Armor import Armor
from item.Consumable import Consumable
from item.Trinket import Trinket
from item.Equipment import Equipment
from item.Inventory import Inventory
from skill.PosionEffect import PoisonEffect
from skill.Buff import Buff
from fighter.main_character.MainCharacter import MainCharacter
from fighter.Stats import Stats
from fighter.Resource import Resource

class SkillCreator():
    @staticmethod
    def create_skills():
        skills = []
        screen = pygame.display.get_surface().get_rect()

        #FIRE BALL
        fire_ball_surface = pygame.image.load("prototipo/assets/skill_sprites/fire_ball.png").convert_alpha()
        animation = SkillCreator.create_spell_animation(fire_ball_surface, screen)

        skills.append(Skill([DamageEffect(100, DamageType.FIRE, 100, 0, EffectTarget.ENEMY)], 1, 1, "FIRE BALL!!!", "prototipo/assets/skill_icons/fireball-red-1.png", animation))

        #FORTIFY SKILL
        skills.append(Skill([HealingEffect(5, EffectTarget.SELF)], 1, 2, "Heal and resistance", "prototipo/assets/skill_icons/heal-jade-1.png", None))

        #SLASH ATTACK
        sword_surface = pygame.image.load("prototipo/assets/skill_sprites/slash.png").convert_alpha()
        animation = SkillCreator.create_slash_animation(sword_surface, screen)

        skills.append(Skill([DamageEffect(1000, DamageType.SLASHING, 100, 5, EffectTarget.ENEMY)], 1, 2, "Slashing", "prototipo/assets/skill_icons/enchant-orange-1.png", animation))

        #EARTH ATTACK
        rock_surface = pygame.image.load("prototipo/assets/skill_sprites/rock.png").convert_alpha()
        animation = SkillCreator.create_spell_animation(rock_surface, screen)

        skills.append(Skill([DamageEffect(100, DamageType.EARTH, 100, 0, EffectTarget.ENEMY)], 1, 1, "Flying stone!", "prototipo/assets/skill_icons/fireball-red-1.png", animation))
        
        #METEOR ATTACK
        meteor_surface = pygame.image.load("prototipo/assets/skill_sprites/meteor.png").convert_alpha()
        animation = SkillCreator.create_spell_animation(meteor_surface, screen)

        skills.append(Skill([DamageEffect(100, DamageType.EARTH, 100, 0, EffectTarget.ENEMY), DamageEffect(100, DamageType.FIRE, 100, 0, EffectTarget.ENEMY)], 1, 1, "FLYING FLAMING STOOOONE!!!", "prototipo/assets/skill_icons/fireball-red-1.png", animation))

        return skills

    @staticmethod
    def create_spell_animation(surface, screen):
        return LinearAnimation(surface, surface.get_rect(topright = (screen.width, screen.height)), surface.get_rect(center = (screen.center)), 60)

    @staticmethod
    def create_slash_animation(surface, screen):
        return LinearAnimation(surface, surface.get_rect(topright = (screen.width, 0)), surface.get_rect(bottomleft = (0, screen.height)), 5)