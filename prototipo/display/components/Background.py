import pygame
from helpers.SingletonMeta import ABCSingletonMeta


class Background(metaclass=ABCSingletonMeta):
    def __init__(self):
        self.image = pygame.image.load("prototipo/assets/Ruins.png")