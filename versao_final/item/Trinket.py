from .Item import Item
from .ItemTypes import ItemType
from skill.Buff import Buff

class Trinket(Item):
    def __init__(self, name, description, weight, buff: Buff):
        super().__init__(name, description, weight, ItemType.TRINKET)
        self.__buff = buff

    @property
    def buff(self):
        return self.__buff
    
    @buff.setter
    def buff(self, buff_effect):
        self.__buff = buff_effect

    def use(self, mc):
        mc.inventory.remove_item(self)
        mc.inventory.add_item(mc.equipment.trinket)
        mc.equipment.trinket = self

