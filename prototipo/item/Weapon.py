from .Item import Item
from .ItemTypes import ItemType
from skill.BuffEffect import BuffEffect
from skill.DamageType import DamageType


class Weapon(Item):
    def __init__(self, name: str, description: str, weight: float, type: ItemType, base_damage: dict, buff_effect: BuffEffect):
        super().__init__(name, description, weight, type)
        self.__base_damage = base_damage
        self.__buff_effect = buff_effect

    @property
    def base_damage(self):
        return self.__base_damage

    @property
    def buff_effect(self):
        return self.__buff_effect

    @base_damage.setter
    def base_damage(self, base_damage):
        self.__base_damage = base_damage

    @buff_effect.setter
    def buff_effect(self, buff_effect):
        self.__buff_effect = buff_effect
