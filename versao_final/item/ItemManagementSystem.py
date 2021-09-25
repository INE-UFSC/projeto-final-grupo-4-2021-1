from prototipo.item.Item import Item
from Inventory import Inventory
from Equipment import Equipment

class ItemManagementSystem:
    def __init__(self, inventory: Inventory, equipment: Equipment):
        self.__inventory = inventory
        self.__equipment = equipment

    @property
    def inventory(self):
        return self.__inventory
    
    @property
    def equipment(self):
        return self.__equipment
    
    def is_equippable(self, item):
        if item.type.value <= 3:
            return True
        else:
            return False
    
    def equip_item(self, item: Item):
        if self.is_equippable == True:
            if item.type.value == 1:
                self.equipment.weapon = item
            elif item.type.value == 2:
                self.equipment.armor = item
            else:
                self.equipment.trinket = item
            
            self.inventory.remove_item(item)

            return "Item sucessfully equipped"

        else:
            return "Item cannot be equipped."
    
    def drop_item(self, item: Item):
        self.__inventory.remove_item(item)

        return f"{item.name} dropped."
