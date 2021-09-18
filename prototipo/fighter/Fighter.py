from abc import ABC, abstractmethod
from copy import deepcopy

from helpers.SingletonMeta import ABCSingletonMeta

from skill.Skill import Skill
from skill.Effect import Effect
from .Resource import Resource
from skill.DamageType import DamageType
from skill.DamageEffect import DamageEffect
from skill.BuffTarget import BuffTarget
from skill.EffectTarget import EffectTarget
from skill.HealingEffect import HealingEffect
from skill.BuffEffect import BuffEffect
from item.Equipment import Equipment
from .Stats import Stats
#buffs: dict[bufftarget, dict[DamageType, multiplier: float]]


class Fighter(ABC):
    def __init__(self, stats: Stats, hp: Resource, ap: Resource, equipment: Equipment, skills: list = [], combat_status: dict = {}):
        self.__stats = stats
        self.__hp = hp
        self.__ap = ap
        self.__equipment = equipment
        self.__buffs = self.initialize_buffs()
        self.__skills = skills
        self.__combat_status = combat_status

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
    def combat_status(self):
        return self.__combat_status
    
    def initialize_buffs(self):
        buffs = {}
        for buffTarget in BuffTarget:
            buffs[buffTarget] = {}
            for damageType in DamageType:
                buffs[buffTarget][damageType] = 0
        return buffs

    def use_skill(self, skill):
        "Returns the list of effects with it's values multiplied by the buffs multipliers in self.__buffs"
        if isinstance(skill, Skill):
            effects = deepcopy(skill.effects)
        else:
            effects = deepcopy(skill)
        
        for effect in effects:
            if isinstance(effect, DamageEffect):
                #for damageType in effect.damage:
                #Multiplica o dano pelo multiplicador do elemento somado com o multiplicador de dano geral, em self.__buffs

                multiplier = self.__buffs[BuffTarget.DAMAGE][effect.type] + self.__buffs[BuffTarget.DAMAGE][DamageType.ALL]
                effect.value *= max(0, multiplier + 1)

                if effect.target == EffectTarget.SELF or effect.target == EffectTarget.BOTH:
                    self.__hp.decrease_current(effect.value)

                #Implementar precisão --------------------------------------------------------------------------------------------------------------------

            if isinstance(effect, HealingEffect):
                if effect.target == EffectTarget.SELF or effect.target == EffectTarget.BOTH:
                    self.__hp.increase_current(effect.amount)
            
            #TODO calcular dano com base nos buffs
            if isinstance(effect, CombatStatus):
                effect.effects = self.use_skill(effect.effects)
                if effect.target == EffectTarget.SELF or effect.target == EffectTarget.BOTH:
                    effect.fighter = self
                    
                    self.add_combat_status(effect)
                    
                    effect.apply_buff()

        

        return effects

    def add_combat_status(self, combat_status):
        self.__combat_status[combat_status.id] = combat_status

    def update_combat_status(self):
        finished_status = []
        for combat_status in self.__combat_status.values():
            if combat_status.update():
                finished_status.append(combat_status)

        for combat_status in finished_status:
            self.remove_combat_status(combat_status)

    def remove_combat_status(self, combat_status):
        for buff in combat_status.buffs:
            self.__fighter.remove_buff(buff)

        self.__combat_status.pop(combat_status.id)

    def get_attacked(self, effects: Effect):
        for effect in effects:
            if isinstance(effect, DamageEffect):
                #for damageType in effect.damage:
                multiplier = self.__buffs[BuffTarget.RESISTANCE][effect.type] + self.__buffs[BuffTarget.RESISTANCE][DamageType.ALL]
                effect.value *= max(0, 1 - multiplier)

                if effect.target == EffectTarget.ENEMY or effect.target == EffectTarget.BOTH:

                    #Multiplica o valor do dano por -1 e aplica na vida
                    self.__hp.decrease_current(effect.value)

            if isinstance(effect, HealingEffect):
                if effect.target == EffectTarget.ENEMY or effect.target == EffectTarget.BOTH:
                    self.__hp.increase_current(effect.amount) 

            #TODO calcular dano com base nos buffs
            if isinstance(effect, CombatStatus):
                if effect.target == EffectTarget.ENEMY or effect.target == EffectTarget.BOTH:
                    effect.fighter = self
                    self.add_combat_status(effect)
                    
                    effect.apply_buff()

        return effects
                     
    def add_buff(self, buff: BuffEffect):
        "Adds up the buff multiplier received by BuffEffect on self.__buffs"
        self.__buffs[buff.buffTarget][buff.damageType] += buff.multiplier

        # for target, damage in buff_effect.buff.items():
        #     for damageType, multiplier in damage.items():
        #         self.__buffs[target][damageType] += multiplier


    def remove_buff(self, buff: BuffEffect):
        "Subtracts the value of the buff effects received by BuffEffect on self.__buffs"
        self.__buffs[buff.buffTarget][buff.damageType] -= buff.multiplier

        # for target, damage in buff_effect.buff.items():
        #     for damageType, multiplier in damage.items():
        #             self.__buffs[target][damageType] -= multiplier

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

class CombatStatus(Effect, ABC):
    def __init__(self, id, target, duration, effects, buffs:list = []):
        self.__id = id
        self.__effects = effects
        self.__buffs = buffs
        self.__fighter = None
        self.__duration = duration
        super().__init__(target)
    
    @property
    def effects(self):
        return self.__effects
    
    @effects.setter
    def effects(self, effects):
        self.__effects = effects

    @property
    def buffs(self):
        return self.__buffs

    @property
    def id(self):
        return self.__id

    @property
    def duration(self):
        return self.__duration

    @property
    def fighter(self):
        return self.__fighter
    
    @fighter.setter
    def fighter(self, fighter: Fighter):
        self.__fighter = fighter
        
    def special_action(self):
        pass

    def apply_effects(self):
        self.__fighter.get_attacked(self.__effects)

    def apply_buff(self):
        for buff in self.__buffs:
            self.__fighter.add_buff(buff)

    def update(self):
        "Returns True if the status should end"
        self.__duration -= 1
        self.apply_effects()
        self.special_action()

        if self.__duration == 0:
            return True