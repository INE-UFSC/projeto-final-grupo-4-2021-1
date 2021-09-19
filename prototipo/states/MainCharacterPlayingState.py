import pygame
from typing import List
from .BaseMenuState import BaseMenuState
from TextSprite import TextSprite
from fighter.main_character.MainCharacter import MainCharacter
from fighter.opponent.Opponent import Opponent
from display.Text import Text
from display.IconButton import IconButton
from display.TextButton import TextButton
from display.Animation import Animation
from skill.Skill import Skill
from display.MainCharacterResources import MainCharacterResources
from display.OpponentResources import OpponentResources
from Singleton import Singleton
# necessario identificar momento em que passar da sala atual para escolher treasureroom ou healroom
# necessario identificar momento em que troca de turno para passar para opponentplaying


class MainCharacterPlayingState(BaseMenuState):
    def __init__(self):
        super(MainCharacterPlayingState, self).__init__()
        self.active_index = 0
        self.previous_index = 0
        self.__new_round = True

        self.player_hp = None
        self.opponent_hp = None

        self.__active_skills: List["Skill"] = []

        skills_menu: List["IconButton"] = [IconButton("prototipo/assets/icon_shadow.png", skill.icon_path) for skill in MainCharacter().skills]

        adder = self.screen_rect.center[0] - (5 * skills_menu[0].background.get_width())
        for skill_icon in skills_menu:
            skill_icon.rect = skill_icon.surface.get_rect(topleft = (adder, self.screen_rect.height - skill_icon.surface.get_height() - 20))
            adder += (skill_icon.surface.get_width() + 20)

    
        options_menu: List["TextButton"] = [TextButton("prototipo/assets/combatMenuButton.png", Text(
            "prototipo/assets/fonts/menu_option.ttf",
            50,
            pygame.Color(255, 255, 255),
            option
        )) for option in ["Pass", "Options"]]

        adder = self.screen_rect.width - (len(options_menu) * (options_menu[0].surface.get_width() + 20))
        for option in options_menu:
            option.rect = option.surface.get_rect(topleft=(adder, self.screen_rect.height - option.surface.get_height() - 150))
            adder += (option.surface.get_width() + 20)

        self.options = skills_menu + options_menu
    
    #Selecting the active index and used skill must be corrected
    def handle_action(self):
        if self.active_index < 10 and not MainCharacter().ap.is_zero():
            skill = MainCharacter().skills[self.active_index]

            if skill not in self.__active_skills:
                skill.main_char_animation.reset()
                self.__active_skills.append(skill)
                MainCharacter().ap.decrease_current(skill.cost)

        elif self.active_index == 3:
            return "OPPONENT_PLAYING"
        
        elif self.active_index == 4:
            return "OPTIONS"

    def run(self):
        if Opponent().hp.is_zero():
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
            if isinstance(option, TextButton):
                option.change_text_color(pygame.Color(255, 0, 0) if index == self.active_index else pygame.Color(255, 255, 255))

            elif isinstance(option, IconButton):
                option.change_background("prototipo/assets/red_circle.png" if index == self.active_index else "prototipo/assets/icon_shadow.png")
            
            option.draw(surface)

        room_level = Text("prototipo/assets/fonts/menu_option.ttf", 25, pygame.Color(255, 255, 255), f"Room Level: {str(Singleton.room.number)}", (1100, 25))
        room_level.draw(surface)