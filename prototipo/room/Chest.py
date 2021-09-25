from item.Weapon import Weapon
from item.Trinket import Trinket
from item.Armor import Armor
from skill.DamageType import DamageType
import random
from helpers.SingletonMeta import ABCSingletonMeta


class Chest(metaclass=ABCSingletonMeta):
    def __init__(self):
        self.__items = self.item_generator()

    @property
    def items(self):
        return self.__items

    def item_generator(self):
        items = []
        chest_item = []

        for _ in range(5):
            items.append(Weapon(f"Weapon {random.randint(1,100)}", "Your own pair of fists.", 1, {DamageType.ALL: 0}, None))
            items.append(Armor(f"Armor {random.randint(1,100)}", "Useless for battle.", 1, {DamageType.ALL: 0}, None))
            items.append(Trinket(f"Trinket {random.randint(1,100)}", "Pretty cool looking, but useless nonetheless.", 1, None))

        for _ in range(3):
            choice = random.choice(items)
            chest_item.append(choice)
            items.remove(choice)

        return chest_item