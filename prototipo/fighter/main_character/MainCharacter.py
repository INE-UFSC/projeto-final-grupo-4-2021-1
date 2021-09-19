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
from display.LinearAnimation import LinearAnimation
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
        surface = pygame.image.load("prototipo/assets/fire_ball.png").convert_alpha()
        surface2 = pygame.image.load("prototipo/assets/fire_ball.png").convert_alpha()
        surface3 = pygame.image.load("prototipo/assets/fire_ball.png").convert_alpha()

        animation = LinearAnimation(surface, surface.get_rect(topright = (screen.width, screen.height)), surface.get_rect(center = (screen.center)), 60)
        animation2 = LinearAnimation(surface2, surface2.get_rect(topright = (screen.width, screen.height)), surface2.get_rect(center = (screen.center)), 60)
        animation3 = LinearAnimation(surface3, surface3.get_rect(topright = (screen.width, screen.height)), surface3.get_rect(center = (screen.center)), 60)
        
        main_char = MainCharacter(Stats(10, 10, 10, 10), Resource(100, 100), Resource(5, 0), Equipment(
                Weapon("Default Sword", "Just your default sword.", 10, ItemType.WEAPON, None, None),
                Armor("Default Armor", "Just your default armor.", 20, ItemType.ARMOR, None, None),
                Trinket("Default Trinket", "Just your default trinket", 0, ItemType.TRINKET, None)
                ), None, None, 0, [
            Skill([DamageEffect(0, DamageType.SLASHING, 100, 0, EffectTarget.ENEMY), BuffEffect(Buff(1, BuffTarget.DAMAGE, DamageType.FIRE), 2, EffectTarget.SELF)], 1,"teste", "prototipo/assets/fire_icon.png", animation),
            Skill([DamageEffect(100, DamageType.FIRE, 100, 0, EffectTarget.ENEMY)], 1,"BURNING", "prototipo/assets/fire_icon.png", animation2),
            Skill([PoisonEffect(0.1, 5, EffectTarget.ENEMY)], 1,"veneno", "prototipo/assets/fire_icon.png", animation3)            
            ])

        #main_char.add_buff(BuffEffect({BuffTarget.DAMAGE: {DamageType.SLASHING: 0.1, DamageType.FIRE: 0.5}}, EffectTarget.BOTH))
        #main_char.add_buff(BuffEffect(BuffTarget.DAMAGE, DamageType.FIRE, 0.5, EffectTarget.BOTH))
        main_char.buffs.append(Buff(0.5, BuffTarget.DAMAGE, DamageType.FIRE))

    
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