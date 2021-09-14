from room.RoomType import RoomType
from room.Room import Room
from room.Door import Door
from Chest import Chest


class TreasureRoom(Room):
    def __init__(self, chest: Chest):
        self.__chest = chest
        super().__init__(self.make_room)

    def make_room(self):
        return RoomType.RoomType.TREASURE

    def make_doors(self):
        door1 = Door(1, RoomType.RoomType.COMBAT)
        door2 = Door(2, RoomType.RoomType.HEAL)

        return [door1, door2]
