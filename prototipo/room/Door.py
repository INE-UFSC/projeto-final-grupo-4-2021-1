from room.RoomType import RoomType


class Door:
    def __init__(self, number: int, next_room_type: RoomType):
        self.__number = number
        self.__next_room_type = next_room_type

    @property
    def number(self):
        return self.__number

    @property
    def next_room_type(self):
        return self.__next_room_type
