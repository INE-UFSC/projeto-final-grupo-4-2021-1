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
    def create_skills(self):
        skills = []
        screen = pygame.display.get_surface().get_rect()

        # FIRE BALL
        fire_ball_surface = self.make_surface("versao_final/assets/skill_sprites/fire_ball.png")
        animation = self.create_spell_animation(fire_ball_surface, screen)
        enemy_animation = self.create_enemy_spell_animation(fire_ball_surface, screen)

        skills.append(Skill([DamageEffect(100, DamageType.FIRE, 100, 0, EffectTarget.ENEMY)], 1, 1, "FIRE BALL!!!",
                            "versao_final/assets/skill_icons/fireball-red-1.png", animation, enemy_animation))

        # FORTIFY SKILL
        skills.append(Skill([HealingEffect(80, EffectTarget.SELF),
                             BuffEffect(Buff(0.2, BuffTarget.RESISTANCE, DamageType.ALL), 2, EffectTarget.SELF)], 1, 2,
                            "Heal and resistance", "versao_final/assets/skill_icons/heal-jade-1.png", None))

        # SLASH ATTACK
        sword_surface = self.make_surface("versao_final/assets/skill_sprites/slash.png", (600, 600))
        animation = self.create_slash_animation(sword_surface, screen)
        enemy_animation = self.create_enemy_spell_animation(sword_surface, screen)

        skills.append(Skill([DamageEffect(240, DamageType.SLASHING, 100, 10, EffectTarget.ENEMY)], 2, 3, "Slashing",
                            "versao_final/assets/skill_icons/slash.png", animation, enemy_animation))

        # EARTH ATTACK
        rock_surface = self.make_surface("versao_final/assets/skill_sprites/rock.png")
        animation = self.create_spell_animation(rock_surface, screen)
        enemy_animation = self.create_enemy_spell_animation(rock_surface, screen)

        skills.append(Skill([DamageEffect(100, DamageType.EARTH, 100, 0, EffectTarget.ENEMY)], 1, 1, "Flying stone!",
                            "versao_final/assets/skill_icons/stone.png", animation, enemy_animation))

        # METEOR ATTACK
        meteor_surface = self.make_surface("versao_final/assets/skill_sprites/meteor.png", (250, 373))
        animation = self.create_spell_animation(meteor_surface, screen)
        enemy_animation = self.create_enemy_spell_animation(meteor_surface, screen)

        skills.append(Skill([DamageEffect(150, DamageType.EARTH, 100, 0, EffectTarget.ENEMY),
                             DamageEffect(250, DamageType.FIRE, 100, 0, EffectTarget.ENEMY)], 4, 6,
                            "FLYING FLAMING STOOOONE!!!", "versao_final/assets/skill_icons/meteor.png", animation,
                            enemy_animation))

        return skills

    def create_spell_animation(self, surface, screen):
        return LinearAnimation(surface, surface.get_rect(topright=(screen.width, screen.height)),
                               surface.get_rect(center=(screen.center)), 60)

    def create_enemy_spell_animation(self, surface, screen):
        return LinearAnimation(surface, surface.get_rect(center=screen.center),
                               surface.get_rect(midtop=screen.midbottom), 60)

    def create_slash_animation(self, surface, screen):
        return LinearAnimation(surface, surface.get_rect(topright=(screen.width, 0)),
                               surface.get_rect(bottomleft=(0, screen.height)), 5)

    def make_surface(self, path, size=None):
        surface = pygame.image.load(path).convert_alpha()

        if size:
            return pygame.transform.scale(surface, size)
        else:
            return surface
