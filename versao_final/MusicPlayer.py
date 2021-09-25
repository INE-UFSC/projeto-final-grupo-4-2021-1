import pygame as pg
from helpers.SingletonMeta import ABCSingletonMeta


class MusicPlayer(metaclass=ABCSingletonMeta):
    def start_player(self):
        pg.init()
        pg.mixer.init()

    def play_music(self, file):
        pg.mixer.music.load(file)
        pg.mixer.music.play(-1, -0, 0)

    def play_sound(self, file):
        sound = pg.mixer.Sound(file)
        sound.play()

    def stop_music(self):
        pg.mixer.music.fadeout(1000)
        pg.mixer.music.unload()
