from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def __init__(self, name, description, weight, type):
        self.__name = name
        self.__description = description
        self.__weight = weight
        self.__type = type

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def weight(self):
        return self.__weight

    @property
    def type(self):
        return self.__type
