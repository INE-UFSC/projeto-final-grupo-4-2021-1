from .Item import Item
from .ItemTypes import ItemType
from skill.Skill import Skill
from creators.OpponentCreator import OpponentCreator

class Consumable(Item):
    def __init__(self, name: str, description: str, weight: float, skill: Skill):
        super().__init__(name, description, weight, ItemType.CONSUMABLE)
        self.__skill = skill

    @property
    def skill(self):
        return self.__skill

    def use(self, mc):
        mc.use_skill(self.__skill, OpponentCreator.create_dummy())
        mc.inventory.remove_item(self)
