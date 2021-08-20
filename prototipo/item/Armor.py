from Item import Item
from ItemTypes import ItemType
from skill.BuffEffect import BuffEffect
from skill.DamageType import DamageType

class Armor(Item):
    def __init__(self, name: str, description: str, weight: float, type: ItemType, base_armor: dict, buff_effect: BuffEffect):
        super().__init__(name, description, weight, type)
        self.__base_armor = base_armor
        self.__buff_effect = buff_effect

    @property
    def base_armor(self):
        return self.__base_armor

    @property
    def buff_effect(self):
        return self.__buff_effect

    @base_armor.setter
    def base_armor(self, base_armor: dict):
        self.__base_armor = base_armor

    @buff_effect.setter
    def buff_effect(self, buff_effect: BuffEffect):
        self.__buff_effect = buff_effect
