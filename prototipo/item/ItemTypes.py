from Weapon import Weapon
from enum import Enum
class ItemType(Enum):
    WEAPON = 1
    ARMOR = 2
    TRINKET = 3
    CONSUMABLE = 4

from Item import Item

class Trinket(Item):
    def __init__(self, name, description, weight, type, buff_effect):
        super().__init__(name, description, weight, type)
        self.__buff_effect = buff_effect

    def use_item(self):
        pass

amuleto = Trinket("Amuleto Fodão", "Um amuleto muito pica.", 4.3, ItemType.WEAPON, "Gaming")

if amuleto.type.value < 2:
    print("ueu")

print(amuleto.type.value)