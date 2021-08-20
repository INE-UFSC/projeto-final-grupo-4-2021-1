import pygame
from .BaseState import BaseState

class Init(BaseState):
    def __init__(self):
        super(Init, self).__init__()
        self.active_index = 0
        self.options = ["Start Game", "Quit Game"]

    def render_text(self, index):
        color = pygame.Color("red") if index == self.active_index else pygame.Color("white")
        return self.font.render(self.options[index], True, color)

    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)

    def handle_action(self):
        if self.active_index == 0:
            return "MAIN_CHARACTER_PLAYING"
        elif self.active_index == 1:
            return "QUIT"

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.active_index = 1 if self.active_index <= 0 else 0
                elif event.key == pygame.K_DOWN:
                    self.active_index = 0 if self.active_index >= 1 else 1
                elif event.key == pygame.K_RETURN:
                    return self.handle_action()

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            surface.blit(text_render, self.get_text_position(text_render, index))
