import pygame
from .BaseState import BaseState


class TreasureRoom(BaseState):
    def __init__(self):
        super(TreasureRoom, self).__init__()
        self.active_index = 0
        self.options = ["Inventory", "Select Item", "Options"]

    def render_text(self, index):
        color = pygame.Color("red") if index == self.active_index else pygame.Color("white")
        return self.font.render(self.options[index], True, color)

    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)

    def handle_action(self):
        if self.active_index == 0:
            # aumentar/baixar volume
            pass
        elif self.active_index == 1:
            # a ser definido
            pass
        elif self.active_index == 2:
            self.done = True
            self.next_state = "MENU"

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if self.active_index > 0:
                    self.active_index -= 1
                else:
                    self.active_index = 0
            elif event.key == pygame.K_DOWN:
                if self.active_index < 2:
                    self.active_index += 1
                else:
                    self.active_index = 2
            elif event.key == pygame.K_RETURN:
                self.handle_action()

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            surface.blit(text_render, self.get_text_position(text_render, index))
