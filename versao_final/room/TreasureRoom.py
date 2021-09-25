from room.RoomType import RoomType
from room.Room import Room
from room.Door import Door
from room.Chest import Chest
from display.components.Background import Background
import pygame


class TreasureRoom(Room):
    def __init__(self):
        self.__chest = Chest()
        Background().image = pygame.image.load("versao_final/assets/RockCave.png")
        super().__init__(self.make_room)

    @property
    def chest(self):
        return self.__chest

    def make_room(self):
        return RoomType.RoomType.TREASURE

    def make_doors(self):
        door1 = Door(1, RoomType.COMBAT)
        door2 = Door(2, RoomType.HEAL)

        return [door1, door2]
