from enum import Enum
from DamageClass import DamageClass

class DamageType(Enum):
    fire = DamageClass.magical
    water = DamageClass.magical
    earth = DamageClass.magical
    air = DamageClass.magical

    piercing = DamageClass.physical
    slashing = DamageClass.physical
    blunt = DamageClass.physical

    #Special type, must only be used to specify buffs
    all = 1
    