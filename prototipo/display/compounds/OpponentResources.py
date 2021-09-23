import pygame
from .Compound import Compound
from display.components.Text import Text
from creators.OpponentCreator import OpponentCreator

class OpponentResources(Compound):
    
    def draw(surface: pygame.Surface):
        current_hp =  OpponentCreator.current.hp.current
        max_hp =  OpponentCreator.current.hp.max

        midtop = (OpponentCreator.current.sprite.rect.midtop[0],  OpponentCreator.current.sprite.rect.top - 40)
        bar_width = 750

        red_bar_rect = pygame.Rect((0,0), (bar_width, 30))
        red_bar_rect.midtop = midtop

        green_bar_rect = pygame.Rect((0,0), (bar_width*current_hp/max_hp, 30))
        green_bar_rect.midtop = midtop
        
        pygame.draw.rect(surface, (0, 0, 0), red_bar_rect, 8) 
        pygame.draw.rect(surface, (255, 0, 0), red_bar_rect)
        pygame.draw.rect(surface, (0, 255, 0), green_bar_rect)

        text = Text("prototipo/assets/fonts/menu_option.ttf", 30, pygame.Color(0, 0, 0), f"{current_hp}/{max_hp}")
        text.rect = text.surface.get_rect(center = red_bar_rect.center)
        text.draw(surface)