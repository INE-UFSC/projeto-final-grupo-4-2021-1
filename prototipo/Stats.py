#Essa classe ainda não adiciona os buffs ao upar os stats.
#Falta decidir se haverá categorização dos danos ou não.
from Fighter import Fighter
from DamageType import DamageType
from DamageClass import DamageClass

INTELLIGENCE_MULTIPLIER = 1.05
STRENGTH_MULTIPLIER = 1.05
CONSTITUTION_MULTIPLIER = 1.05
WITS_MULTIPLIER = 1.05

class Stats:
    def __init__(self, fighter: Fighter, strengh: int = 0, intelligence: int = 0,
                 constitution: int = 0, wits: int = 0, availablePoints:int = 0):
        self.__fighter = fighter
        self.__intelligence = intelligence
        self.__strength = strengh
        self.__constitution = constitution
        self.__wits = wits
        self.__availablePoints = availablePoints

    @property
    def intelligence(self):
        return self.__intelligence

    @property
    def strengh(self):
        return self.__strength
    
    @property
    def constitution(self):
        return self.__constitution

    @property
    def wits(self):
        return self.__wits

    @property
    def availablePoints(self):
        return self.__availablePoints

    def increase_intelligence(self):
        if self.__availablePoints:
            self.__intelligence += 1
            #Criar um BuffEffect vazio
            for damagetype in DamageType:
                if damagetype.value == DamageClass.magical:
                    pass
                    #Adicionar o buff correspondente ao BuffEffect criado

            self.__availablePoints -= 1

    def increase_strength(self):
        if self.__availablePoints:
            self.__strength += 1
            #Criar um BuffEffect vazio
            for damagetype in DamageType:
                if damagetype.value == DamageClass.physical:
                    pass
                    #Adicionar o buff correspondente ao BuffEffect criado

            self.__availablePoints -= 1

    def increase_constitution(self):
        if self.__availablePoints:
            self.__constitution += 1
            heal = self.__fighter.hp * (CONSTITUTION_MULTIPLIER - 1)
            self.__fighter.hp.increase_max(CONSTITUTION_MULTIPLIER, True)
            self.__fighter.hp.increase_current(heal)
            self.__availablePoints -= 1

    #Implementar Buffs
    def increase_wits(self):
        if self.__availablePoints:
            self.__wits += 1
            self.__availablePoints -= 1

    def add_availablePoints(self, amount):
        self.__availablePoints += amount
    