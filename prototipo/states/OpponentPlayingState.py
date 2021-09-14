import pygame
from .BaseState import BaseState
from TextSprite import TextSprite
from Singleton import Singleton


class OpponentPlaying(BaseState):
    def __init__(self):
        super(OpponentPlaying, self).__init__()
        self.player_hp = None
        self.opponent_hp = None
        self.time_active = 0
        self.__new_round = True

    def draw(self, surface):
        surface.blit(Singleton.background, (0,0))
        Singleton.opponent.draw(surface)
        for hp in [self.player_hp, self.opponent_hp]:
            surface.blit(hp.surf, hp.rect)

    def handle_action(self):
        Singleton.main_character.get_attacked(Singleton.opponent.use_skill(Singleton.opponent.skills[0]))

        if Singleton.main_character.hp.is_zero():
            return "END"
        elif Singleton.opponent.ap.is_zero():
            Singleton.main_character.ap.refill()
            self.__new_round = True
            return "MAIN_CHARACTER_PLAYING"

    def run(self):
        if self.__new_round:
            Singleton.opponent.update_combat_status()
            self.__new_round = False

        player_hp_text = f"Player HP:  {Singleton.main_character.hp.current}/{Singleton.main_character.hp.max}"
        opponent_hp_text =  f"Opponent HP: {Singleton.opponent.hp.current}/{Singleton.opponent.hp.max}"

        surface = self.font.render(player_hp_text, True, pygame.Color("blue"))
        self.player_hp = (TextSprite(player_hp_text, surface, surface.get_rect(topleft=(10,10))))

        surface = self.font.render(opponent_hp_text, True, pygame.Color("blue"))
        self.opponent_hp = (TextSprite(opponent_hp_text, surface, surface.get_rect(topleft=(10,40))))
        self.time_active += 1
        if self.time_active > 119:
            self.time_active = 0
            return self.handle_action()
        
    

