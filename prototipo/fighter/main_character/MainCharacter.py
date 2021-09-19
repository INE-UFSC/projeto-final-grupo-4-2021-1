from skill.PosionEffect import PoisonEffect
from skill.Buff import Buff
from helpers.SingletonMeta import ABCSingletonMeta
import pygame

from item.Weapon import Weapon
from item.Armor import Armor
from item.ItemTypes import ItemType
from item.Trinket import Trinket
from fighter.Fighter import Fighter
from fighter.Stats import Stats
from fighter.Resource import Resource
from item.Inventory import Inventory
from item.Equipment import Equipment
from skill.EffectTarget import EffectTarget
from skill.DamageEffect import DamageEffect
from skill.HealingEffect import HealingEffect
from skill.DamageType import DamageType
from skill.Skill import Skill
from skill.BuffTarget import BuffTarget
from skill.BuffEffect import BuffEffect
from display.components.LinearAnimation import LinearAnimation
#importar inventário e equipamento

ATRIBUTE_POINTS_PER_LEVEL = 2

#buffs: dict[bufftarget, dict[DamageType, multiplier]]
class MainCharacter(Fighter, metaclass=ABCSingletonMeta):
    def __init__(self, stats: Stats, hp: Resource, ap: Resource, equipment: Equipment, buffs: dict, inventory: Inventory, exp: int, skills: list = []):
        self.__inventory = inventory
        self.__equipment = equipment
        self.__exp = exp
        super().__init__(stats, hp, ap, equipment, skills)

    @staticmethod
    def generate_test_character():
        screen = pygame.display.get_surface().get_rect()
        surface = pygame.image.load("prototipo/assets/skill_icons/enchant-orange-1.png").convert_alpha()
        surface2 = pygame.image.load("prototipo/assets/fire_ball.png").convert_alpha()
        surface3 = pygame.image.load("prototipo/assets/fire_ball.png").convert_alpha()

        animation = LinearAnimation(surface, surface.get_rect(topright = (screen.width, screen.height)), surface.get_rect(center = (screen.center)), 60)
        animation2 = LinearAnimation(surface2, surface2.get_rect(topright = (screen.width, screen.height)), surface2.get_rect(center = (screen.center)), 60)
        animation3 = LinearAnimation(surface3, surface3.get_rect(topright = (screen.width, screen.height)), surface3.get_rect(center = (screen.center)), 60)
        
        equipment = Equipment(
                Weapon("Default Sword", "Just your default sword.", 10, ItemType.WEAPON, {DamageType.FIRE: 10}, None),
                Armor("Default Armor", "Just your default armor.", 20, ItemType.ARMOR, {DamageType.PIERCING: 10}, None),
                Trinket("Default Trinket", "Just your default trinket", 0, ItemType.TRINKET, None)
                )

        main_char = MainCharacter(Stats(10, 10, 10, 10), Resource(100, 100), Resource(5, 0), equipment, None, None, 0, [
            Skill([DamageEffect(10, DamageType.SLASHING, 100, 5, EffectTarget.ENEMY)], 1,"Slashing", "prototipo/assets/skill_icons/enchant-orange-1.png", animation),
            Skill([DamageEffect(50, DamageType.FIRE, 100, 0, EffectTarget.ENEMY)], 1,"Fire", "prototipo/assets/skill_icons/fireball-red-1.png", animation2),
            Skill([HealingEffect(5, EffectTarget.SELF)], 1, "Heal", "prototipo/assets/skill_icons/heal-jade-1.png", animation),
            Skill([PoisonEffect(0.1, 2, EffectTarget.ENEMY)], 1,"Poison", "prototipo/assets/skill_icons/rip-acid-1.png", animation3),              
            Skill([BuffEffect(Buff(0.5, BuffTarget.RESISTANCE, DamageType.ALL), 1, EffectTarget.SELF)], 1,"Block", "prototipo/assets/skill_icons/protect-orange-1.png", animation3),            
            ])

        main_char.add_buff(Buff(0.5, BuffTarget.DAMAGE, DamageType.FIRE))

    
    @property
    def inventory(self):
        return self.__inventory

    @property
    def equipment(self):
        return self.__equipment

    @property
    def exp(self):
        return self.__exp

    def increase_exp(self, amount):
        "Increases the current EXP by the specified amount"
        self.__exp += amount

    #Implementar mensagem de level up 
    def level_up(self):
        self.stats.add_availablePoints(ATRIBUTE_POINTS_PER_LEVEL)