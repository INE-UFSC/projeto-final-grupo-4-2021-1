from abc import ABC
import RoomType

number = 1


class Room(ABC):
    def __init__(self, type: RoomType, doors: []):
        global number
        self.__number = number
        self.__type = type
        self.__doors = doors
        number += 1

    @property
    def number(self):
        return self.__number

    @property
    def type(self):
        return self.__type

    @property
    def doors(self):
        return self.__doors
