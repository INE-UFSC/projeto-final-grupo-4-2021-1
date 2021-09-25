import pygame
from display.components.Text import Text
from creators.OpponentCreator import OpponentCreator


class OpponentResources():
    def draw(self: pygame.Surface):
        current_hp = OpponentCreator.current.hp.current
        max_hp = OpponentCreator.current.hp.max

        midtop = (OpponentCreator.current.sprite.rect.midtop[0], OpponentCreator.current.sprite.rect.top - 40)
        bar_width = 750

        red_bar_rect = pygame.Rect((0, 0), (bar_width, 30))
        red_bar_rect.midtop = midtop

        green_bar_rect = pygame.Rect((0, 0), (bar_width * current_hp / max_hp, 30))
        green_bar_rect.midtop = midtop

        pygame.draw.rect(self, (0, 0, 0), red_bar_rect, 8)
        pygame.draw.rect(self, (255, 0, 0), red_bar_rect)
        pygame.draw.rect(self, (0, 255, 0), green_bar_rect)

        text = Text("versao_final/assets/fonts/menu_option.ttf", 30, pygame.Color(0, 0, 0), f"{current_hp}/{max_hp}")
        text.rect = text.surface.get_rect(center=red_bar_rect.center)
        text.draw(self)
