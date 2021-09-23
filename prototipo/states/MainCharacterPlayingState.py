import pygame
from typing import List
from .BaseMenuState import BaseMenuState
from fighter.main_character.MainCharacter import MainCharacter
from fighter.opponent.Opponent import Opponent
from display.components.Text import Text
from display.components.SkillIconButton import SkillIconButton
from display.components.MenuTextButton import MenuTextButton
from display.components.Animation import Animation
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
        self.__new_round = True

        self.__active_skills: List["Skill"] = []

        skills_menu: List["SkillIconButton"] = [SkillIconButton(skill) for skill in MainCharacter().skills]

        adder = 40
        for skill_icon in skills_menu:
            skill_icon.rect = skill_icon.surface.get_rect(topleft = (adder, self.screen_rect.height - skill_icon.surface.get_height() - 20))
            adder += (skill_icon.surface.get_width() + 20)

    
        options_menu: List["MenuTextButton"] = [MenuTextButton("prototipo/assets/combatMenuButton.png", Text(
            "prototipo/assets/fonts/menu_option.ttf",
            50,
            pygame.Color(255, 255, 255),
            option[0]
        ), option[1]) for option in [("Pass", "OPPONENT_PLAYING"), ("Options", "OPTIONS")]]

        adder = self.screen_rect.width - (len(options_menu) * (options_menu[0].surface.get_width() + 30))
        for option in options_menu:
            option.rect = option.surface.get_rect(topleft=(adder, self.screen_rect.height - option.surface.get_height() - 20))
            adder += (option.surface.get_width() + 20)

        self.options = skills_menu + options_menu
    
    #Selecting the active index and used skill must be corrected
    def handle_action(self):
        if isinstance(self.options[self.active_index], SkillIconButton) and not MainCharacter().ap.is_zero():
            skill = self.options[self.active_index].skill

            if skill not in self.__active_skills:
                skill.main_char_animation.reset()
                self.__active_skills.append(skill)
                MainCharacter().ap.decrease_current(skill.cost)

        else:
            return self.options[self.active_index].on_pressed()

    def run(self):
        if Opponent().hp.is_zero():
            Opponent().hp.increase_current(1000)
            Opponent().clear_buffs()
            Opponent().clear_lingering_effects()
            return "END_COMBAT"

        if MainCharacter().ap.is_zero() and not self.__active_skills:
            Opponent().ap.increase_current(2)
            self.__new_round = True
            return "OPPONENT_PLAYING"

        self.apply_skills()
        
        if self.__new_round:
            MainCharacter().update_lingering_effects()
            self.__new_round = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                return self.handle_menu(event.key)

    def apply_skills(self):
        for index, skill in enumerate(self.__active_skills):
            if skill.main_char_animation.finished:
                MainCharacter().use_skill(skill, Opponent())
                self.__active_skills.pop(index)
            else:
                skill.main_char_animation.update()

    def draw(self, surface):
        surface.blit(Singleton.background, (0,0))

        Opponent().draw(surface)
        MainCharacterResources.draw(surface)
        OpponentResources.draw(surface)

        for skill in self.__active_skills:
            skill.main_char_animation.draw(surface)

        for index, option in enumerate(self.options):
            option.select() if index == self.active_index else option.unselect()
            option.draw(surface)

        room_level = Text("prototipo/assets/fonts/menu_option.ttf", 25, pygame.Color(255, 255, 255), f"Room Level: {str(Singleton.room.number)}", (1100, 25))
        room_level.draw(surface)