import pygame
from .BaseState import BaseState
from TextSprite import TextSprite
from creators.OpponentCreator import OpponentCreator
from fighter.main_character.MainCharacter import MainCharacter
from display.compounds.MainCharacterResources import MainCharacterResources
from display.compounds.OpponentResources import OpponentResources
from creators.OpponentCreator import OpponentCreator
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
        OpponentCreator.current.draw(surface)
        MainCharacterResources.draw(surface)
        OpponentResources.draw(surface)


    def handle_action(self):
        skill = OpponentCreator.current.skills[0]
        OpponentCreator.current.use_skill(MainCharacter())
        OpponentCreator.current.ap.decrease_current(skill.cost)

        if MainCharacter().hp.is_zero():
            return "END"
        elif OpponentCreator.current.ap.is_zero():
            self.__new_round = True
            return "MAIN_CHARACTER_PLAYING"

    def run(self):
        room_level_text = f"Room Level: {str(Singleton.room.number)}"
        surface = self.font.render(room_level_text, True, pygame.Color(255, 255, 255))
        self.room_level = (TextSprite(room_level_text, surface, surface.get_rect(topleft=(670,10))))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

        if self.__new_round:
            OpponentCreator.current.ap.increase_current(2)
            OpponentCreator.current.update_lingering_effects()
            OpponentCreator.current.update_skills_cooldown()
            self.__new_round = False

        self.time_active += 1
        if self.time_active > 29:
            self.time_active = 0
            return self.handle_action()
