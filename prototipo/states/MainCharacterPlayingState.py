import pygame
from typing import List
from .BaseMenuState import BaseMenuState
from TextSprite import TextSprite
from display.Text import Text
from display.TextButton import TextButton
from display.MainCharacterResources import MainCharacterResources
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
    
        self.options: List["TextButton"] = [TextButton("prototipo/assets/combatMenuButton.png", Text(
            "prototipo/assets/fonts/menu_option.ttf",
            50,
            pygame.Color(255, 255, 255),
            option
        )) for option in ["Attack","Fire Attack", "Effect", "Pass", "Options"]]

        menu_width = 0
        for option in self.options:
            option.rect = option.surface.get_rect(topleft=(50 + menu_width, self.screen_rect.height - option.surface.get_height() - 10))
            menu_width += (option.surface.get_width() + 20)
    
    #Selecting the active index and used skill must be corrected
    def handle_action(self):
        if self.active_index == 0:
            Singleton.opponent.get_attacked(Singleton.main_character.use_skill(Singleton.main_character.skills[0]))

        elif self.active_index == 1:
            Singleton.opponent.get_attacked(Singleton.main_character.use_skill(Singleton.main_character.skills[1]))
            
        elif self.active_index == 2:
            Singleton.opponent.get_attacked(Singleton.main_character.use_skill(Singleton.main_character.skills[2]))

        elif self.active_index == 3:
            return "OPPONENT_PLAYING"
        
        elif self.active_index == 4:
            return "OPTIONS"

        if Singleton.opponent.hp.is_zero():
            return "END_COMBAT"
        elif Singleton.main_character.ap.is_zero():
            Singleton.opponent.ap.increase_current(2)
            self.__new_round = True
            return "OPPONENT_PLAYING"

    def run(self):
        room_level_text = f"Room Level: {str(Singleton.room.number)}"
        surface = self.font.render(room_level_text, True, pygame.Color("white"))
        self.room_level = (TextSprite(room_level_text, surface, surface.get_rect(topleft=(670,10))))

        if self.__new_round:
            Singleton.main_character.update_combat_status()
            self.__new_round = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                return self.handle_menu(event.key)


    def draw(self, surface):
        surface.blit(Singleton.background, (0,0))
        Singleton.opponent.draw(surface)
        MainCharacterResources.draw(surface)

        for index, option in enumerate(self.options):
            option.change_text_color(pygame.Color(255, 0, 0) if index == self.active_index else pygame.Color(255, 255, 255))
            option.draw(surface)
