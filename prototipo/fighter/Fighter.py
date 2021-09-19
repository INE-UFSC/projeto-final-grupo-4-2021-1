from __future__ import annotations
from abc import ABC, abstractmethod
from skill.LingeringEffect import LingeringEffect
from typing import List
from skill.Skill import Skill
from .Resource import Resource
from skill.Buff import Buff
from item.Equipment import Equipment
from .Stats import Stats


class Fighter(ABC):
    def __init__(self, stats: Stats, hp: Resource, ap: Resource, equipment: Equipment, skills: List["Skill"] = []):
        self.__stats = stats
        self.__hp = hp
        self.__ap = ap
        self.__equipment = equipment
        self.__buffs: List["Buff"] = self.__equipment.equipment_buffs()
        self.__skills = skills
        self.__lingering_effects: List["LingeringEffect"] = []

    @property
    def hp(self):
        return self.__hp

    @property
    def ap(self):
        return self.__ap

    @property
    def stats(self):
        return self.__stats

    @property
    def skills(self):
        return self.__skills

    @property
    def equipment(self):
        return self.__equipment

    @property
    def buffs(self):
        return self.__buffs

    @property
    def lingering_effects(self):
        return self.__lingering_effects

    def use_skill(self, skill, target):
        skill.use(self, target)
                     
    def add_buff(self, buff: Buff):
        self.__buffs.append(buff)

    def remove_buff(self, buff: Buff):
        self.__buffs.remove(buff)

    def clear_buffs(self):
        self.__buffs = self.__equipment.equipment_buffs()

    def add_lingering_effect(self, effect: LingeringEffect):
        self.__lingering_effects.append(effect)

    def remove_lingering_effect(self, effect: LingeringEffect):
        self.__lingering_effects.remove(effect)

    def clear_lingering_effects(self):
        self.__lingering_effects.clear()

    def update_lingering_effects(self):
        self.__lingering_effects = list(filter(lambda effect: effect.update(self), self.__lingering_effects))

    def add_skill(self, skill):
        "Appends the skill in self.__skills"
        self.__skills.append(skill)
    
    def remove_skill(self, skill):
        "If the parameter is an Int, then the skill will be poped out by its index. If it is a Skill, then the skill will be removed"
        if isinstance(skill, int):
            self.__skills.pop(skill)
        else:
            self.__skills.remove(skill)
    
    def switch_skill_place(self, currentpos: int, newpos: int):
        "Switch the position of two skills in self.__skills"
        tmp = self.__skills[newpos]
        self.__skills[newpos] = self.__skills[currentpos]
        self.__skills[currentpos] = tmp
