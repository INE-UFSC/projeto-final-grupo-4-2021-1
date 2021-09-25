from helpers.SingletonMeta import ABCSingletonMeta
from fighter.Fighter import Fighter
from fighter.Stats import Stats
from fighter.Resource import Resource
from item.Inventory import Inventory
from item.Equipment import Equipment

ATRIBUTE_POINTS_PER_LEVEL = 2

class MainCharacter(Fighter, metaclass=ABCSingletonMeta):
    def __init__(self, level, stats: Stats, hp: Resource, ap: Resource, equipment: Equipment, inventory: Inventory, exp: int, skills: list = [], xp=0):
        self.__inventory = inventory
        self.__equipment = equipment
        self.__leveled_up = False
        super().__init__(level, stats, hp, ap, equipment, skills)
    
    @property
    def inventory(self):
        return self.__inventory

    @property
    def leveled_up(self):
        return self.__leveled_up

    @leveled_up.setter
    def leveled_up(self, leveled_up):
        self.__leveled_up = bool(leveled_up)

    @property
    def equipment(self):
        return self.__equipment

    def level_up(self):
        self.__leveled_up = True
        self.hp.increase_max(self.stats.stats["CONSTITUTION"])
        self.stats.add_availablePoints(ATRIBUTE_POINTS_PER_LEVEL)
        self._level += 1

    def add_xp(self, xp):
        self._xp += xp

        while True:
            if self._level < 5:
                if self._xp > 500:
                    self._xp -= 500
                    self.level_up()
                else:
                    return

            elif self._level < 10:
                if self._xp > 1000:
                    self._xp -= 1000
                    self.level_up()
                else:
                    return

            elif self._level < 20:
                if self._xp > 1500:
                    self._xp -= 1500
                    self.level_up()
                else:
                    return

            else:
                if self._xp > 2000:
                    self._xp -= 2000
                    self.level_up()
                else:
                    return
                