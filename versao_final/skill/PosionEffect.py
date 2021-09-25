from fighter.Fighter import Fighter
from .EffectTarget import EffectTarget
from .LingeringEffect import LingeringEffect

class PoisonEffect(LingeringEffect):
    def __init__(self, percentage: float, duration: int, target: EffectTarget):
        super().__init__(duration, target)
        self.__percentage = percentage

    def apply_effect(self, user: 'Fighter', enemy: 'Fighter'):
        super().attach(user, enemy)

    def update(self, attached_to: 'Fighter'):
        attached_to.hp.decrease_current(attached_to.hp.current * self.__percentage)
        self.duration -= 1
        return super().update(attached_to)
