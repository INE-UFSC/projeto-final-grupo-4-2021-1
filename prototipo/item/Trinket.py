from .Item import Item
from .ItemTypes import ItemType
from skill.Buff import Buff

class Trinket(Item):
    def __init__(self, name, description, weight, type, buff: Buff):
        super().__init__(name, description, weight, type)
        self.__buff = buff

    @property
    def buff(self):
        return self.__buff
    
    @buff.setter
    def buff(self, buff_effect):
        self.__buff = buff_effect



