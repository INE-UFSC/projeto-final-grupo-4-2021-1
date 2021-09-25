#Essa classe ainda não adiciona os buffs ao upar os stats.
#Falta decidir se haverá categorização dos danos ou não.
from skill.DamageType import DamageType
from skill.StatBuff import StatBuff
from skill.BuffTarget import BuffTarget
from skill.DamageType import DamageType

STATS_MULTIPLIER = 0.01

class Stats:
    def __init__(self, strengh: int = 0, intelligence: int = 0,
                 constitution: int = 0, wits: int = 0, availablePoints = 0):
        self.__stats = {
            "INTELLIGENCE": intelligence,
            "STRENGTH": strengh,
            "CONSTITUTION": constitution,
            "WITS": wits
        }

        self.__buffs = [
            StatBuff(self, "INTELLIGENCE", STATS_MULTIPLIER, BuffTarget.DAMAGE, DamageType.ALL),
            StatBuff(self, "CONSTITUTION", STATS_MULTIPLIER, BuffTarget.RESISTANCE, DamageType.ALL),
            StatBuff(self, "WITS", STATS_MULTIPLIER, BuffTarget.RESISTANCE, DamageType.ALL),
            StatBuff(self, "STRENGTH", STATS_MULTIPLIER, BuffTarget.DAMAGE, DamageType.ALL)
        ]

        self.__availablePoints = availablePoints

    @property
    def buffs(self):
        return self.__buffs

    @property
    def stats(self):
        return self.__stats

    @property
    def availablePoints(self):
        return self.__availablePoints

    def upgrade_stat(self, stat: str, amount = 1):
        if stat in self.__stats:
            self.__stats[stat] += amount
        self.__availablePoints -= 1 

    def add_availablePoints(self, amount):
        self.__availablePoints += amount
    