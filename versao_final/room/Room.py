from abc import ABC, abstractmethod
from room.RoomType import RoomType


class Room(ABC):
    def __init__(self, type: RoomType):
        self.__type = type
        self.__doors = self.make_doors

    @property
    def type(self):
        return self.__type

    @property
    def doors(self):
        return self.__doors

    @abstractmethod
    def make_room(self):
        raise NotImplementedError("You should implement this!")

    @abstractmethod
    def make_doors(self):
        raise NotImplementedError("You should implement this!")
