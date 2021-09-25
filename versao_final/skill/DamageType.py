from enum import Enum


class DamageType(Enum):
    FIRE = "FIRE"
    WATER = "WATER"
    EARTH = "EARTH"
    AIR = "AIR"

    PIERCING = "PIERCING"
    SLASHING = "SLASHING"
    BLUDGEONING = "BLUDGEONING"

    # Special type, must only be used to specify buffs
    ALL = "ALL"
