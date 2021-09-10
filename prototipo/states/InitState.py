import pygame
from .BaseMenuState import BaseMenuState


class Init(BaseMenuState):
    def __init__(self):
        super(Init, self).__init__()
        self.active_index = 0
        self.options = ["New", "Load", "Options", "Exit"]

    def render_text(self, index):
        color = pygame.Color("red") if index == self.active_index else pygame.Color("white")
        return self.font.render(self.options[index], True, color)

    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)

    def handle_action(self):
        if self.active_index == 0:
            return "START_COMBAT"
        elif self.active_index == 1:
            # load
            pass
        elif self.active_index == 2:
            return "OPTIONS"
        elif self.active_index == 3:
            return "QUIT"

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYUP:
                return self.handle_menu(event.key)

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            surface.blit(text_render, self.get_text_position(text_render, index))
