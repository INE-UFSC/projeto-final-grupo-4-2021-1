from enum import Enum
from .DamageClass import DamageClass

class DamageType(Enum):
    FIRE = DamageClass.MAGICAL
    WATER = DamageClass.MAGICAL
    EARTH = DamageClass.MAGICAL
    AIR = DamageClass.MAGICAL

    PIERCING = DamageClass.PHYSICAL
    SLASHING = DamageClass.PHYSICAL
    BLUDGEONING = DamageClass.PHYSICAL

    #Special type, must only be used to specify buffs
    ALL = 1