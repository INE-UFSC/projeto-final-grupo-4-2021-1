from collections import defaultdict
from .Item import Item
from .ItemTypes import ItemType
from skill.Buff import Buff

class Armor(Item):
    def __init__(self, name: str, description: str, weight: float, base_armor: dict, buff: Buff):
        super().__init__(name, description, weight, ItemType.ARMOR)
        self.__base_armor = defaultdict(int, base_armor)
        self.__buff = buff

    @property
    def base_armor(self):
        return self.__base_armor

    @property
    def buff(self):
        return self.__buff

    @base_armor.setter
    def base_armor(self, base_armor: dict):
        self.__base_armor = base_armor

    @buff.setter
    def buff(self, buff: Buff):
        self.__buff = buff

    def use(self, mc):
        mc.inventory.remove_item(self)
        mc.inventory.add_item(mc.equipment.armor)
        mc.equipment.armor = self
