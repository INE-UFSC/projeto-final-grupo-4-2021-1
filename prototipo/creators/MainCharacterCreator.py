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

class MainCharacterCreator:
    @staticmethod
    def generate_test_character():
        screen = pygame.display.get_surface().get_rect()
        surface = pygame.image.load("prototipo/assets/skill_icons/enchant-orange-1.png").convert_alpha()
        surface2 = pygame.image.load("prototipo/assets/fire_ball.png").convert_alpha()
        surface3 = pygame.image.load("prototipo/assets/fire_ball.png").convert_alpha()

        animation = LinearAnimation(surface, surface.get_rect(topright = (screen.width, screen.height)), surface.get_rect(center = (screen.center)), 60)
        animation2 = LinearAnimation(surface2, surface2.get_rect(topright = (screen.width, screen.height)), surface2.get_rect(center = (screen.center)), 60)
        animation3 = LinearAnimation(surface3, surface3.get_rect(topright = (screen.width, screen.height)), surface3.get_rect(center = (screen.center)), 60)
        
        healing_skill = Skill([HealingEffect(5, EffectTarget.SELF)], 1, 2, "Heal", "prototipo/assets/skill_icons/heal-jade-1.png", animation)

        weapon = Weapon("Default Sword", "Just your default sword.", 10, {DamageType.FIRE: 10}, None)
        armor =  Armor("Default Armor", "Just your default armor.", 20, {DamageType.PIERCING: 10}, None)
        trinket = Trinket("Default Trinket", "Just your default trinket", 0, None)
        consumable = Consumable("Healing Potion", "Heals for some HP.", 1, healing_skill)

        inventory = Inventory([weapon, armor, trinket, consumable], 999)
        for i in range(11):
            inventory.add_item(consumable)

        main_char = MainCharacter(0, Stats(10, 10, 10, 10), Resource(1000, 100), Resource(5, 0), Equipment.default_equipment(), inventory, 0, [
            Skill([DamageEffect(1000, DamageType.SLASHING, 100, 5, EffectTarget.ENEMY)], 1, 2, "Slashing", "prototipo/assets/skill_icons/enchant-orange-1.png", animation),
            Skill([DamageEffect(100, DamageType.FIRE, 100, 0, EffectTarget.ENEMY)], 1, 1, "Fire", "prototipo/assets/skill_icons/fireball-red-1.png", animation2),
            Skill([PoisonEffect(0.1, 2, EffectTarget.ENEMY)], 1, 2, "Poison", "prototipo/assets/skill_icons/rip-acid-1.png", animation3),              
            Skill([BuffEffect(Buff(0.5, BuffTarget.RESISTANCE, DamageType.ALL), 1, EffectTarget.SELF)], 3, 3, "Block", "prototipo/assets/skill_icons/protect-orange-1.png", animation3),            
            healing_skill
            ])

        main_char.add_buff(Buff(0.5, BuffTarget.DAMAGE, DamageType.FIRE))

    # @staticmethod
    # def generate_skills():
    #     surfaces = 





        #animations = [LinearAnimation(surface, surface.get_rect(topright = (screen.width, screen.height)), surface.get_rect(center = (screen.center)), 60) for x in range(15)]