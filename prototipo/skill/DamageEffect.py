from random import randint

from skill.BuffTarget import BuffTarget
from typing import Dict
from .Effect import Effect
from .EffectTarget import EffectTarget
from .DamageType import DamageType

class DamageEffect(Effect):
    def __init__(self, value: float, type: DamageType, accuracy: int, crit_chance: int, target: EffectTarget):
        super().__init__(target)
        self.__value = value
        self.__type = type
        self.__accuracy = accuracy
        self.__crit_chance = crit_chance

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
    
    @property
    def accuracy(self):
        return self.__accuracy

    @accuracy.setter
    def accuracy(self, accuracy):
        self.__accuracy = accuracy

    @property
    def crit_chance(self):
        return self.__crit_chance

    @property
    def type(self):
        return self.__type

    from fighter.Fighter import Fighter
    def apply_effect(self, user: Fighter, enemy: Fighter):
        damage = self.__apply_damage_buffs(self.__value, user.buffs[BuffTarget.DAMAGE])
        damage = self.__calculate_crit(damage)
        damage = self.__calculate_hit(damage)

        if self.target == EffectTarget.SELF:
            user.hp.decrease_current(self.__apply_resistance_buffs(damage, user.buffs[BuffTarget.RESISTANCE]))
        elif self.target == EffectTarget.ENEMY:
            enemy.hp.decrease_current(self.__apply_resistance_buffs(damage, enemy.buffs[BuffTarget.RESISTANCE]))
        else:
            user.hp.decrease_current(self.__apply_resistance_buffs(damage, user.buffs[BuffTarget.RESISTANCE]))
            enemy.hp.decrease_current(self.__apply_resistance_buffs(damage, enemy.buffs[BuffTarget.RESISTANCE]))

    def __apply_damage_buffs(self, damage: int, buffs: Dict["DamageType", float]):
        multiplier = buffs[self.__type] + buffs[DamageType.ALL]
        return damage * max(0, multiplier + 1)

    def __calculate_crit(self, damage: int):
        return damage * 2 if randint(1, 100) <= self.__crit_chance else damage

    def __calculate_hit(self, damage: int):
        return damage if randint(1, 100) <= self.__accuracy else 0

    def __apply_resistance_buffs(self, damage: int, buffs: Dict["DamageType", float]):
        multiplier = buffs[self.__type] + buffs[DamageType.ALL]
        return damage * max(0, 1 - multiplier)

