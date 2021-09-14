from room.RoomType import RoomType
from room.Room import Room
from room.Door import Door
from room.Chest import Chest


class TreasureRoom(Room):
    def __init__(self):
        self.__chest = Chest()
        super().__init__(self.make_room)

    def make_room(self):
        return RoomType.RoomType.TREASURE

    def make_doors(self):
        door1 = Door(1, RoomType.COMBAT)
        door2 = Door(2, RoomType.HEAL)

        return [door1, door2]
