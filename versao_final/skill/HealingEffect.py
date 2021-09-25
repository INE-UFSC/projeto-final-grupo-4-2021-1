from fighter.Fighter import Fighter
from .Effect import Effect
from .EffectTarget import EffectTarget


class HealingEffect(Effect):
    def __init__(self, amount: int, target: EffectTarget):
        super().__init__(target)
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    def apply_effect(self, user: Fighter, enemy: Fighter):
        if self.target == EffectTarget.SELF:
            user.hp.increase_current(self.__amount)
        elif self.target == EffectTarget.ENEMY:
            enemy.hp.increase_current(self.__amount)
        else:
            user.hp.increase_current(self.__amount)
            enemy.hp.increase_current(self.__amount)
