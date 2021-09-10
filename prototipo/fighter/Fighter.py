from abc import ABC, abstractmethod
from copy import deepcopy

from skill.Skill import Skill
from .Resource import Resource
from skill.DamageType import DamageType
from skill.DamageEffect import DamageEffect
from skill.BuffTarget import BuffTarget
from skill.EffectTarget import EffectTarget
from skill.HealingEffect import HealingEffect
from skill.BuffEffect import BuffEffect
from item.Equipment import Equipment
from .Stats import Stats
from skill.CombatStatus import CombatStatus
from Singleton import Singleton
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
        
    #Remover?
    def basicattack(self):
        if self.__skills:
            return self.use_skill(0)

    def initialize_buffs(self):
        buffs = {}
        for buffTarget in BuffTarget:
            buffs[buffTarget] = {}
            for damageType in DamageType:
                buffs[buffTarget][damageType] = 0
        return buffs

    def use_skill(self, idx):
        "Returns a copy of the skill with it's values multiplied by the buffs multipliers in self.__buffs"
        skill = deepcopy(self.__skills[idx])
        for index, effect in enumerate(skill.effects):
            if isinstance(effect, DamageEffect):
                for damageType in effect.damage:
                    #Multiplica o dano pelo multiplicador do elemento somado com o multiplicador de dano geral, em self.__buffs

                    multiplier = self.__buffs[BuffTarget.DAMAGE][damageType] + self.__buffs[BuffTarget.DAMAGE][DamageType.ALL]
                    skill.effects[index].damage[damageType] *= max(0, multiplier + 1)

                    if effect.target == EffectTarget.SELF or effect.target == EffectTarget.BOTH:
                        self.__hp.decrease_current(effect.damage[damageType])

                    #Implementar precisão --------------------------------------------------------------------------------------------------------------------

            if isinstance(effect, HealingEffect):
                if effect.target == EffectTarget.SELF or effect.target == EffectTarget.BOTH:
                    self.__hp.increase_current(effect.amount)
            
            #TODO implementação de BuffEffect
            if isinstance(effect, CombatStatus):
                if effect.target == EffectTarget.SELF or effect.target == EffectTarget.BOTH:
                    effect.fighter = self
                    self.combat_status[effect.id] = effect
                    Singleton.CombatStatusUpdater.add(effect)
                    
                    effect.apply_buff()
                    effect.update()

        self.__ap.decrease_current(skill.cost)

        return skill

    def add_combat_status(self, combat_status: CombatStatus):
        self.__combat_status[combat_status.id]

    def update_combat_status(self):
        for combat_status in self.__combat_status.items():
            combat_status.update()

    def get_attacked(self, skill: Skill):
        for index, effect in enumerate(skill.effects):
            if isinstance(effect, DamageEffect):
                for damageType in effect.damage:
                    multiplier = self.__buffs[BuffTarget.RESISTANCE][damageType] + self.__buffs[BuffTarget.RESISTANCE][DamageType.ALL]
                    skill.effects[index].damage[damageType] *= max(0, multiplier + 1)

                    if effect.target == EffectTarget.ENEMY or effect.target == EffectTarget.BOTH:

                        #Multiplica o valor do dano por -1 e aplica na vida
                        self.__hp.decrease_current(effect.damage[damageType])

            if isinstance(effect, HealingEffect):
                if effect.target == EffectTarget.ENEMY or effect.target == EffectTarget.BOTH:
                    self.__hp.increase_current(effect.amount) 

            if isinstance(effect, BuffEffect):
                pass

        return skill
                     
    def add_buff(self, buff_effect: BuffEffect):
        "Adds up the values of the buff effects received by BuffEffect on self.__buffs"
        for target, damage in buff_effect.buff.items():
            for damageType, multiplier in damage.items():
                try:
                    self.__buffs[target][damageType] += multiplier
                except:
                    self.__buffs[target][damageType] = multiplier

    def remove_buff(self, buff_effect: BuffEffect):
        "Subtracts the value of the buff effects received by BuffEffect on self.__buffs"
        for target, damage in buff_effect.buff.items():
            for damageType, multiplier in damage.items():
                    self.__buffs[target][damageType] -= multiplier

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
