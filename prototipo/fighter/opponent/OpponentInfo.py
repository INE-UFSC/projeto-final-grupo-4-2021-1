from abc import ABC

class OpponentInfo(ABC):
    def __init__(self):
        self.__info = "info"

    @property
    def info(self):
        return self.__info