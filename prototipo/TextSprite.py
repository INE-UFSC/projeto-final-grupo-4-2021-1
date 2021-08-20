from dataclasses import dataclass
import pygame

@dataclass
class TextSprite:
    text: str
    surf: pygame.Surface
    rect: pygame.Rect
    
