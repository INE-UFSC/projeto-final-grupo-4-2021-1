import pygame
from typing import List
from .BaseMenuState import BaseMenuState
from fighter.main_character.MainCharacter import MainCharacter
from creators.OpponentCreator import OpponentCreator
from display.components.Text import Text
from display.components.SkillIconButton import SkillIconButton
from display.components.MenuTextButton import MenuTextButton
from skill.Skill import Skill
from display.compounds.MainCharacterResources import MainCharacterResources
from display.compounds.OpponentResources import OpponentResources
from Singleton import Singleton
# necessario identificar momento em que passar da sala atual para escolher treasureroom ou healroom
# necessario identificar momento em que troca de turno para passar para opponentplaying


class MainCharacterPlayingState(BaseMenuState):
    def __init__(self):
        super(MainCharacterPlayingState, self).__init__()
        self.active_index = 0
        self.options = []
        self.__new_round = True

        self.__active_skill: Skill = None



        for skill in MainCharacter().skills:
            self.options.append(SkillIconButton(skill))

        for option in [("Pass", "OPPONENT_PLAYING"), ("Inventory", "INVENTORY")]:
            self.options.append(MenuTextButton("prototipo/assets/combatMenuButton.png", Text(
                "prototipo/assets/fonts/menu_option.ttf",
                50,
                pygame.Color(255, 255, 255),
                option[0]
            ), option[1]))

        adder = 40
        for option in self.options:
            option.rect = option.surface.get_rect(topleft = (adder, self.screen_rect.height - option.surface.get_height() - 20))
            adder += (option.surface.get_width() + 20)

    
    def handle_action(self):
        if isinstance(self.options[self.active_index], SkillIconButton) and not MainCharacter().ap.is_zero():
            skill = self.options[self.active_index].skill

            if not self.__active_skill:
                self.__active_skill = skill
                MainCharacter().ap.decrease_current(skill.cost)

        else:
            return self.options[self.active_index].on_pressed()

    def run(self):
        if self.__new_round:
            MainCharacter().update_lingering_effects()
            self.__new_round = False

        if OpponentCreator.current.hp.is_zero():
            return "END_COMBAT"

        if MainCharacter().ap.is_zero() and not self.__active_skill:
            OpponentCreator.current.ap.increase_current(2)
            self.__new_round = True
            return "OPPONENT_PLAYING"

        self.apply_skills()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                return self.handle_menu(event.key)

    def apply_skills(self):
        if self.__active_skill:
            if self.__active_skill.main_char_animation.finished:
                MainCharacter().use_skill(self.__active_skill, OpponentCreator.current)
                self.__active_skill.main_char_animation.reset()
                self.__active_skill = None
            else:
                self.__active_skill.main_char_animation.update()

    def draw(self, surface):
        surface.blit(Singleton.background, (0,0))

        OpponentCreator.current.draw(surface)
        MainCharacterResources.draw(surface)
        OpponentResources.draw(surface)

        if self.__active_skill:
            self.__active_skill.main_char_animation.draw(surface)
        else:
            for index, option in enumerate(self.options):
                option.select() if index == self.active_index else option.unselect()
                option.draw(surface)

        room_level = Text("prototipo/assets/fonts/menu_option.ttf", 25, pygame.Color(255, 255, 255), f"Room Level: {str(Singleton.room.number)}", (1100, 25))
        room_level.draw(surface)