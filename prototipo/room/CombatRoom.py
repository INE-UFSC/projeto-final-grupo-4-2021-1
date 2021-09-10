import RoomType
from Room import Room


class CombatRoom(Room):
    def __init__(self):
        self.__type = self.make_room
        super().__init__(self.__type)

    @property
    def type(self):
        return self.__type

    def make_room(self):
        return RoomType.RoomType.TREASURE
