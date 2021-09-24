from .Buff import Buff
from .BuffTarget import BuffTarget
from .DamageType import DamageType
import fighter.Stats

class StatBuff(Buff):
    def __init__(self, stats, stat: str, buffperpoint: float, target: BuffTarget, type: DamageType):
        super().__init__(None, target, type)
        self.__stats = stats
        self.__stat = stat
        self.__buffperpoint = buffperpoint
    
    @property
    def multiplier(self):
        return self.__stats.stats[self.__stat] * self.__buffperpoint