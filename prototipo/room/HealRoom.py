from room.RoomType import RoomType
from room.Room import Room
from room.Door import Door


class HealRoom(Room):
    def __init__(self):
        super().__init__(self.make_room)

    def make_room(self):
        return RoomType.RoomType.HEAL

    def make_doors(self):
        door1 = Door(1, RoomType.RoomType.COMBAT)
        door2 = Door(2, RoomType.RoomType.TREASURE)

        return [door1, door2]
