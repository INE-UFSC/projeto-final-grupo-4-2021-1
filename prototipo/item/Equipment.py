from Armor import Armor
from Weapon import Weapon
from Trinket import Trinket


class Equipment:
    def __init__(self, weapon: Weapon, armor: Armor, trinket: Trinket):
        self.__weapon = weapon
        self.__armor = armor
        self.__trinket = trinket

    @property
    def weapon(self):
        return self.__weapon

    @property
    def armor(self):
        return self.__armor

    @property
    def trinket(self):
        return self.__trinket
    
    @weapon.setter
    def weapon(self, weapon: Weapon):
        self.__weapon = weapon
    
    @armor.setter
    def armor(self, armor: Armor):
        self.__armor = armor
    
    @trinket.setter
    def trinket(self, trinket: Trinket):
        self.__trinket = trinket