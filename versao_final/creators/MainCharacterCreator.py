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
from creators.SkillCreator import SkillCreator


class MainCharacterCreator:
    @staticmethod
    def generate_test_character():
        healing_skill = Skill([HealingEffect(5, EffectTarget.SELF)], 1, 2, "Heal",
                              "versao_final/assets/skill_icons/heal-jade-1.png", None)
        weapon = Weapon("Default Sword", "Just your default sword.", 10, {DamageType.FIRE: 10}, None)
        armor = Armor("Default Armor", "Just your default armor.", 20, {DamageType.PIERCING: 10}, None)
        trinket = Trinket("Default Trinket", "Just your default trinket", 0, None)
        consumable = Consumable("Healing Potion", "Heals for some HP.", 1, healing_skill)

        inventory = Inventory([weapon, armor, trinket, consumable], 999)
        for i in range(5):
            inventory.add_item(consumable)

        main_char = MainCharacter(0, Stats(10, 10, 10, 10), Resource(1000, 1000), Resource(5, 0),
                                  Equipment.default_equipment(), inventory, 0, SkillCreator().create_skills())

        main_char.add_buff(Buff(0.5, BuffTarget.DAMAGE, DamageType.FIRE))
