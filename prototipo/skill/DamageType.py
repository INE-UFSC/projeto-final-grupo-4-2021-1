from enum import Enum
from .DamageClass import DamageClass

class DamageType(Enum):
    FIRE = "FIRE"
    WATER = "WATER"
    EARTH = "EARTH"
    AIR = "AIR"
    MAGICAL = "MAGICAL"

    PIERCING = "PIERCING"
    SLASHING = "SLASHING"
    BLUDGEONING = "BLUDGEONING"

    #Special type, must only be used to specify buffs
    ALL = "ALL"