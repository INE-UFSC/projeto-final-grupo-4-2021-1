from .CombatStatus import CombatStatus

class CombatStatusUpdater():
    def __init__(self):
        self.__combat_status = []
    
    def update(self):
        for combat_status in self.__combat_status:
            combat_status.update()