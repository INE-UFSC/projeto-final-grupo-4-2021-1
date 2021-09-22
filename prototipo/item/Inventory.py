#from Armor import Armor
#from Weapon import Weapon
#from Trinket import Trinket


class Inventory:
    def __init__(self, items, weight_capacity):
        self.__items = items
        self.__weight_capacity = weight_capacity

    @property
    def items(self):
        return self.__items
    
    @property
    def weight_capacity(self):
        return self.__weight_capacity

    @weight_capacity.setter
    def weight_capacity(self, weight_capacity):
        self.__weight_capacity = weight_capacity

    def add_item(self, item):
        self.__items.append(item)
    
    def remove_item(self, item):
        self.__items.remove(item)





