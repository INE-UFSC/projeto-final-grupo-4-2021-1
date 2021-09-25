import pygame
from .BaseMenuState import BaseMenuState
from display.components.Text import Text


class OptionsState(BaseMenuState):
    def __init__(self):
        super(OptionsState, self).__init__()
        self.active_index = 0
        self.options = [Text(
            "prototipo/assets/fonts/menu_option.ttf",
            35,
            pygame.Color(255, 255, 255),
            option
        ) for option in ["Option1", "Option2", "Return"]]

        menu_height = 0
        for option in self.options:
            option.rect = option.surface.get_rect(center=(self.screen_rect.center[0], self.screen_rect.center[1] + menu_height))
            menu_height += (option.surface.get_height() + 10)


    def render_text(self, index):
        color = pygame.Color(255, 0, 0) if index == self.active_index else pygame.Color(255, 255, 255)
        return self.font.render(self.options[index], True, color)

    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)

    def handle_action(self):
        if self.active_index == 0:
            # aumentar/baixar volume
            pass
        elif self.active_index == 1:
            pass
        elif self.active_index == 2:
            return "PREVIOUS"

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                return self.handle_menu(event.key)

    def draw(self, surface):
        surface.fill(pygame.Color(0, 0, 0))
        for index, option in enumerate(self.options):
            option.color = pygame.Color(255, 0, 0) if index == self.active_index else pygame.Color(255, 255, 255)
            option.draw(surface)