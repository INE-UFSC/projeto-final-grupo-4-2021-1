import RoomType
from Chest import Chest
from Room import Room


class TreasureRoom(Room):
    def __init__(self, type: RoomType, doors: list, chest: Chest):
        super().__init__(type, doors)
        self.__chest = chest
