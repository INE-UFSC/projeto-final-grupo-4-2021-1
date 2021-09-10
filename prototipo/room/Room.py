from abc import ABC, abstractmethod
import RoomType
from Door import Door


class Room(ABC):
    counter = 0

    def __init__(self, type: RoomType):
        Room.counter += 1
        self.__number = Room.counter
        self.__type = type
        self.__doors = self.make_doors

    @property
    def number(self):
        return self.__number

    @property
    def type(self):
        return self.__type

    @property
    def doors(self):
        return self.__doors

    # Factory method make_room será especializado para cada tipo de sala
    @abstractmethod
    def make_room(self):
        raise NotImplementedError("You should implement this!")

    def make_doors(self):
        door1 = Door(1, RoomType.RoomType.COMBAT)
        door2 = Door(2, RoomType.RoomType.TREASURE)

        return [door1, door2]
