from typing import Dict
from .LingeringEffect import LingeringEffect
from .EffectTarget import EffectTarget
from .Buff import Buff
from fighter.Fighter import Fighter


class BuffEffect(LingeringEffect):
    def __init__(self, buff: Buff, duration: int, target: EffectTarget):
        super().__init__(duration, target)
        self.__buff = buff

    def apply_effect(self, user: 'Fighter', enemy: 'Fighter'):
        if self.target == EffectTarget.SELF:
            user.add_buff(self.__buff)
        elif self.target == EffectTarget.ENEMY:
            enemy.add_buff(self.__buff)
        else:
            user.add_buff(self.__buff)
            enemy.add_buff(self.__buff)
        super().attach(user, enemy)

    def update(self, attached_to: 'Fighter'):
        self.duration -= 1
        if (self.duration == 0):
            attached_to.remove_buff(self.__buff)
        return super().update(attached_to)