from abc import abstractmethod
import pygame
from Singleton import Singleton
from .Text import Text

class OpponentResources:
    @abstractmethod
    def draw(surface, midtop = None):
        current_hp = Singleton.opponent.hp.current
        max_hp = Singleton.opponent.hp.max

        if not midtop:
            midtop = Singleton.screen_rect.midtop
            midtop = (midtop[0], midtop[1] + 20)

        red_bar_rect = pygame.Rect((0,0), (750, 30))
        red_bar_rect.midtop = midtop

        green_bar_rect = pygame.Rect((0,0), (750*current_hp/max_hp, 30))
        green_bar_rect.midtop = midtop
        
        pygame.draw.rect(surface, (0, 0, 0), red_bar_rect, 8) 
        pygame.draw.rect(surface, (255, 0, 0), red_bar_rect)
        pygame.draw.rect(surface, (0, 255, 0), green_bar_rect)

        text = Text("prototipo/assets/fonts/menu_option.ttf", 30, pygame.Color(0, 0, 0), f"{current_hp}/{max_hp}")
        text.rect = text.surface.get_rect(center = red_bar_rect.center)
        text.draw(surface)