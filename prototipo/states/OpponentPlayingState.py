import pygame
from .BaseState import BaseState
from TextSprite import TextSprite
from fighter.opponent.Opponent import Opponent
from fighter.main_character.MainCharacter import MainCharacter
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
        Opponent().draw(surface)
        MainCharacterResources.draw(surface)
        OpponentResources.draw(surface)


    def handle_action(self):
        skill = Opponent().skills[0]
        Opponent().use_skill(skill, MainCharacter())
        Opponent().ap.decrease_current(skill.cost)

        if MainCharacter().hp.is_zero():
            return "END"
        elif Opponent().ap.is_zero():
            MainCharacter().ap.increase_current(2)
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
            Opponent().update_lingering_effects()
            self.__new_round = False

        self.time_active += 1
        if self.time_active > 29:
            self.time_active = 0
            return self.handle_action()
