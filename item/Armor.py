from Item import Item

class Armor(Item):
    def __init__(self, name, description, weight, type, base_armor, buff_effect):
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
    def base_armor(self, base_armor):
        self.__base_armor = base_armor

    @buff_effect.setter
    def buff_effect(self, buff_effect):
        self.__buff_effect = buff_effect
