from Item import Item
from ItemTypes import ItemType
from skill.BuffEffect import BuffEffect

class Trinket(Item):
    def __init__(self, name, description, weight, type, buff_effect):
        super().__init__(name, description, weight, type)
        self.__buff_effect = buff_effect

    @property
    def buff_effect(self):
        return self.__buff_effect
    
    @buff_effect.setter
    def buff_effect(self, buff_effect):
        self.__buff_effect = buff_effect



