import pygame
from .BaseState import BaseState
from TextSprite import TextSprite
import Singleton


class OpponentPlaying(BaseState):
    def __init__(self):
        super(OpponentPlaying, self).__init__()
        self.player_hp = None
        self.opponent_hp = None
        self.time_active = 0

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        for hp in [self.player_hp, self.opponent_hp]:
            surface.blit(hp.surf, hp.rect)

    def handle_action(self):
        Singleton.main_character.get_attacked(Singleton.opponent.use_skill(0))

        if Singleton.main_character.hp.is_zero():
            return "END_COMBAT"
        return "MAIN_CHARACTER_PLAYING"

    def run(self):
        player_hp_text = f"Player HP: {Singleton.main_character.hp.current}/{Singleton.main_character.hp.max}"
        opponent_hp_text =  f"Opponent HP: {Singleton.opponent.hp.current}/{Singleton.opponent.hp.max}"

        surface = self.font.render(player_hp_text, True, pygame.Color("blue"))
        self.player_hp = (TextSprite(player_hp_text, surface, surface.get_rect(topleft=(10,10))))

        surface = self.font.render(opponent_hp_text, True, pygame.Color("blue"))
        self.opponent_hp = (TextSprite(opponent_hp_text, surface, surface.get_rect(topleft=(10,40))))
        self.time_active += 1
        if self.time_active > 119:
            self.time_active = 0
            return self.handle_action()
        
    

