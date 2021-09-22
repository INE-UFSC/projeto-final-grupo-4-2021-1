from .Item import Item
from .ItemTypes import ItemType
from skill.Skill import Skill
from fighter.Fighter import Fighter

class Consumable(Item):
    def __init__(self, name: str, description: str, weight: float, skill: Skill):
        super().__init__(name, description, weight, ItemType.CONSUMABLE)
        self.__skill = skill

    @property
    def skill(self):
        return self.__skill

    def use(self, user: Fighter, enemy: Fighter):
        user.use_skill(self.__skill, enemy)
