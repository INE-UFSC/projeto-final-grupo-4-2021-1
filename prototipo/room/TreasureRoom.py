import RoomType
from Chest import Chest
from Room import Room


class TreasureRoom(Room):
    def __init__(self, chest: Chest):
        self.__type = self.make_room
        super().__init__(self.__type)
        self.__chest = chest

    @property
    def type(self):
        return self.__number

    def make_room(self):
        return RoomType.RoomType.COMBAT
