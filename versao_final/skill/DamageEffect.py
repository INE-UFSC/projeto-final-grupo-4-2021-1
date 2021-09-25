from random import randint

from fighter.Fighter import Fighter
from typing import List
from .Effect import Effect
from .EffectTarget import EffectTarget
from .BuffTarget import BuffTarget
from .DamageType import DamageType
from .Buff import Buff


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

    def apply_effect(self, user: 'Fighter', enemy: 'Fighter'):
        damage = self.__value + user.equipment.weapon.base_damage[self.__type]
        damage = self.__apply_damage_buffs(damage, filter(lambda buff: self.__is_damage_buff(buff), user.buffs))
        damage = self.__calculate_crit(damage)
        damage = self.__calculate_hit(damage)

        if self.target == EffectTarget.SELF:
            user.hp.decrease_current(self.__calculate_final_damage(damage, user))
        elif self.target == EffectTarget.ENEMY:
            enemy.hp.decrease_current(self.__calculate_final_damage(damage, enemy))
        else:
            user.hp.decrease_current(self.__calculate_final_damage(damage, user))
            enemy.hp.decrease_current(self.__calculate_final_damage(damage, enemy))

    def __apply_damage_buffs(self, damage: int, buffs: List["Buff"]):
        buffs = filter(lambda buff: buff.type == self.__type or buff.type == DamageType.ALL, buffs)
        multiplier = sum(buff.multiplier for buff in buffs)
        return damage * max(0, multiplier + 1)

    def __calculate_crit(self, damage: int):
        return damage * 2 if randint(1, 100) <= self.__crit_chance else damage

    def __calculate_hit(self, damage: int):
        return damage if randint(1, 100) <= self.__accuracy else 0

    def __calculate_final_damage(self, damage, receiver: 'Fighter'):
        buffs = filter(lambda buff: self.__is_resistance_buff(buff), receiver.buffs)
        multiplier = sum(buff.multiplier for buff in buffs)
        return (damage - receiver.equipment.armor.base_armor[self.type]) * max(0, 1 - multiplier)

    def __is_damage_buff(self, buff: Buff):
        return buff.target == BuffTarget.DAMAGE and (buff.type == self.__type or buff.type == DamageType.ALL)

    def __is_resistance_buff(self, buff: Buff):
        return buff.target == BuffTarget.RESISTANCE and (buff.type == self.__type or buff.type == DamageType.ALL)
