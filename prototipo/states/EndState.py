import pygame
from .BaseState import BaseState


class End(BaseState):
    def __init__(self):
        super(End, self).__init__()
        self.title = self.font.render("End", True, pygame.Color("white"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.time_active = 0

    def run(self):
        self.time_active += 1
        if self.time_active >= 119:
            return "QUIT"

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        surface.blit(self.title, self.title_rect)
