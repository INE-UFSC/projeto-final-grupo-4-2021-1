import pygame
from room.RoomType import RoomType
from room.Room import Room
from room.Door import Door
from display.components.Background import Background
from fighter.main_character.MainCharacter import MainCharacter


class HealRoom(Room):
    def __init__(self):
        MainCharacter().hp.increase_current(1)
        super().__init__(self.make_room)
        Background().image = pygame.image.load("prototipo/assets/Cobblestones.png")

    def make_room(self):
        return RoomType.RoomType.HEAL

    def make_doors(self):
        door1 = Door(1, RoomType.COMBAT)
        door2 = Door(2, RoomType.TREASURE)

        return [door1, door2]
