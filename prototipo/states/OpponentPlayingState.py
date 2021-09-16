import pygame
from .BaseState import BaseState
from TextSprite import TextSprite
from display.MainCharacterResources import MainCharacterResources
from display.OpponentResources import OpponentResources
from Singleton import Singleton


class OpponentPlayingState(BaseState):
    def __init__(self):
        super(OpponentPlayingState, self).__init__()
        self.player_hp = None
        self.opponent_hp = None
        self.time_active = 0
        self.__new_round = True

    def draw(self, surface):
        surface.blit(Singleton.background, (0,0))
        Singleton.opponent.draw(surface)
        MainCharacterResources.draw(surface)
        OpponentResources.draw(surface)


    def handle_action(self):
        skill = Singleton.opponent.skills[0]
        Singleton.main_character.get_attacked(Singleton.opponent.use_skill(skill))
        Singleton.opponent.ap.decrease_current(skill.cost)

        if Singleton.main_character.hp.is_zero():
            return "END"
        elif Singleton.opponent.ap.is_zero():
            Singleton.main_character.ap.increase_current(2)
            self.__new_round = True
            return "MAIN_CHARACTER_PLAYING"

    def run(self):
        room_level_text = f"Room Level: {str(Singleton.room.number)}"
        surface = self.font.render(room_level_text, True, pygame.Color("white"))
        self.room_level = (TextSprite(room_level_text, surface, surface.get_rect(topleft=(670,10))))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

        if self.__new_round:
            Singleton.opponent.update_combat_status()
            self.__new_round = False

        self.time_active += 1
        if self.time_active > 29:
            self.time_active = 0
            return self.handle_action()
