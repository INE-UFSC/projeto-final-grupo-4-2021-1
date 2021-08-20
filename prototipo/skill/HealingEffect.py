from Effect import Effect
from EffectTarget import EffectTarget

class HealingEffect(Effect):
    def __init__(self, amount: int, target: EffectTarget):
        super().init(target)
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount
    
    def apply_effect(self, character: Fighter, enemy: Fighter):
        pass