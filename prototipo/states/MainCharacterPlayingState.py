import pygame
from typing import List
from .BaseMenuState import BaseMenuState
from TextSprite import TextSprite
from display.Text import Text
from display.Button import Button
from display.MainCharacterResources import MainCharacterResources
from Singleton import Singleton
# necessario identificar momento em que passar da sala atual para escolher treasureroom ou healroom
# necessario identificar momento em que troca de turno para passar para opponentplaying


class MainCharacterPlaying(BaseMenuState):
    def __init__(self):
        super(MainCharacterPlaying, self).__init__()
        self.active_index = 0
        self.previous_index = 0
        self.__new_round = True

        self.player_hp = None
        self.opponent_hp = None
    
        self.options: List["Button"] = [Button("prototipo/assets/combatMenuButton.png", Text(
            "prototipo/assets/fonts/menu_option.ttf",
            50,
            pygame.Color(255, 255, 255),
            option
        )) for option in ["Attack","Fire Attack", "Effect", "Item", "Options"]]

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
            print("You used an item! Wow!")
        
        elif self.active_index == 4:
            return "OPTIONS"

        if Singleton.opponent.hp.is_zero():
            return "END_COMBAT"
        elif Singleton.main_character.ap.is_zero():
            Singleton.opponent.ap.refill()
            self.__new_round = True
            return "OPPONENT_PLAYING"

    def run(self):
        if self.__new_round:
            Singleton.main_character.update_combat_status()
            self.__new_round = False

        player_hp_text = f"Player HP: {Singleton.main_character.hp.current}/{Singleton.main_character.hp.max}"
        opponent_hp_text =  f"Opponent HP: {Singleton.opponent.hp.current}/{Singleton.opponent.hp.max}"

        surface = self.font.render(player_hp_text, True, pygame.Color("blue"))
        self.player_hp = (TextSprite(player_hp_text, surface, surface.get_rect(topleft=(10,10))))

        surface = self.font.render(opponent_hp_text, True, pygame.Color("blue"))
        self.opponent_hp = (TextSprite(opponent_hp_text, surface, surface.get_rect(topleft=(10,40))))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                #Corrigir - o menu deve ser atualizado no mesmo ciclo.
                return self.handle_menu(event.key)


    def draw(self, surface):
        surface.blit(Singleton.background, (0,0))
        Singleton.opponent.draw(surface)

        for index, option in enumerate(self.options):
            option.change_text_color(pygame.Color(255, 0, 0) if index == self.active_index else pygame.Color(255, 255, 255))
            option.draw(surface)

        MainCharacterResources.draw(surface)

        #for option in [self.player_hp, self.opponent_hp]:
            # text_render = self.render_text(index)
         #   surface.blit(option.surf, option.rect)
