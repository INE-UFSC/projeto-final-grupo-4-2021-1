import pygame
from .BaseState import BaseState
from creators.OpponentCreator import OpponentCreator
from fighter.main_character.MainCharacter import MainCharacter
from display.compounds.MainCharacterResources import MainCharacterResources
from display.compounds.OpponentResources import OpponentResources
from creators.OpponentCreator import OpponentCreator
from display.components.Background import Background
from display.components.Text import Text


class OpponentPlayingState(BaseState):
    def __init__(self):
        super(OpponentPlayingState, self).__init__()
        self.player_hp = None
        self.opponent_hp = None
        self.time_active = 0
        self.__new_round = True

    def draw(self, surface):
        surface.blit(Background().image, (0,0))

        combat_room = Text("prototipo/assets/fonts/menu_option.ttf", 25, pygame.Color(255, 255, 255), "Combat Room", (1100, 25))
        combat_room.draw(surface)

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
