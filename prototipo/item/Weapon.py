from collections import defaultdict
from .Item import Item
from .ItemTypes import ItemType
from typing import Dict
from skill.Buff import Buff
from skill.DamageType import DamageType


class Weapon(Item):
    def __init__(self, name: str, description: str, weight: float, type: ItemType, base_damage: Dict["DamageType", int], buff: Buff):
        super().__init__(name, description, weight, type)
        self.__base_damage = defaultdict(int, base_damage)
        self.__buff = buff

    @property
    def base_damage(self):
        return self.__base_damage

    @property
    def buff(self):
        return self.__buff

    @base_damage.setter
    def base_damage(self, base_damage):
        self.__base_damage = base_damage

    @buff.setter
    def buff(self, buff):
        self.__buff = buff
