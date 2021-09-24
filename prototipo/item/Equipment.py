from abc import abstractmethod
from skill.DamageType import DamageType
from item.ItemTypes import ItemType
from .Armor import Armor
from .Weapon import Weapon
from .Trinket import Trinket


class Equipment:
    def __init__(self, weapon: Weapon, armor: Armor, trinket: Trinket):
        self.__weapon = weapon
        self.__armor = armor
        self.__trinket = trinket

    @abstractmethod
    def default_equipment():
        return Equipment(Weapon("Hands", "Your own pair of fists.", 0, {DamageType.ALL: 0}, None),
                        Armor("Tattered Clothes", "Useless for battle.", 0, {DamageType.ALL: 0}, None),
                        Trinket("UFSC's Badge of Honor", "Pretty cool looking, but useless nonetheless.", 0, None))

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

    def equipment_buffs(self):
        return list(filter(None, [self.__weapon.buff, self.__armor.buff, self.__trinket.buff]))