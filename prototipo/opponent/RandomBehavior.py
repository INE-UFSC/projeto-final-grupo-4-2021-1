from Behavior import Behavior
from BehaviorType import BehaviorType
from random import choice
from Opponent import Opponent

class RandomBehavior(Behavior):
    def __init__(self, opponent: Opponent):
        self.__opponent = opponent
        super().__init__(BehaviorType.random)
    
    def choose_skill(self):
        return choice(self.__opponent.skills)

    def plan_action(self):
        pass