from abc import ABC
from .Effect import Effect
from fighter.Fighter import Fighter

class CombatStatus(Effect, ABC):
    def __init__(self, id, target, duration, skill, buffs:list = []):
        self.__id = id
        self.__skill = skill
        self.__buffs = buffs
        self.__fighter = None
        self.__duration = duration
        super().__init__(target)
    
    @property
    def skill(self):
        return self.__skill

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

    def use_skill(self):
        self.__fighter.get_attacked(self.__skill)

    def apply_buff(self):
        for buff in self.__buffs:
            self.__fighter.add_buff(buff)

    def remove_buff(self):
        for buff in self.__buffs:
            self.__fighter.remove_buff(buff)

    def update(self):
        self.__duration =- 1
        self.use_skill()
        self.special_action()

        if self.__duration == 1:
            self.remove_combat_status()
            
    def remove_combat_status(self):
        self.remove_buff()
        self.__fighter.combat_status.pop(self.__id)

        

# class Eba(CombatStatus):
#     def __init__(self, target, skills:list = []):
#         super().__init__(target, skills)

# eba = Eba("birl")
# print(eba.target)
