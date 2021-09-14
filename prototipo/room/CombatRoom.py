import pygame
from room.RoomType import RoomType
from room.Room import Room
from room.Door import Door


class CombatRoom(Room):
    counter = 0

    def __init__(self):
        CombatRoom.counter += 1
        self.__number = CombatRoom.counter
        self.__surf = pygame.Surface(size=(456, 200))
        self.__rect = self.__surf.get_rect(center=(400, 300))
        super().__init__(self.make_room)

    @property
    def number(self):
        return self.__number

    def make_room(self):
        return RoomType.RoomType.COMBAT

    def make_doors(self):
        door1 = Door(1, RoomType.TREASURE)
        door2 = Door(2, RoomType.HEAL)

        door_list = [door1, door2]

        return door_list
