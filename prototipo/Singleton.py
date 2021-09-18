from fighter.main_character.MainCharacter import MainCharacter
from fighter.opponent.Opponent import Opponent
from room.Room import Room
import pygame

class Singleton:
    room: Room = None
    background = None
    screen_rect: pygame.Rect = None

#ATENÇÃO TIME: É PRA IMPLEMENTAR ESPECIALIZAÇÕES DESSE AQUI
class SingletonCertoQueEhPraImplementar(object):
    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
