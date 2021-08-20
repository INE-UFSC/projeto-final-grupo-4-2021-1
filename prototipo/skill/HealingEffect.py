from .Effect import Effect
from .EffectTarget import EffectTarget

class HealingEffect(Effect):
    def __init__(self, amount: int, target: EffectTarget):
        super().__init__(target)
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount