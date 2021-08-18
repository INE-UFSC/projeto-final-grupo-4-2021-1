import RoomType
from Room import Room


class CombatRoom(Room):
    def __init__(self, type: RoomType, doors: [], combat_system: CombatSystem):
        super().__init__(type, doors)
        self.__combat_system = combat_system
