from Item import Item

class Trinket(Item):
    def __init__(self, name, description, weight, type, buff_effect):
        super().__init__(name, description, weight, type)
        self.__buff_effect = buff_effect

    @property
    def buff_effect(self):
        return self.__buff_effect
    
    @buff_effect.getter
    def buff_effect(self, buff_effect):
        self.__buff_effect = buff_effect



