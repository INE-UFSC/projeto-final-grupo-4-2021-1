from fighter.main_character.MainCharacter import MainCharacter
import pygame
from states.BaseMenuState import BaseMenuState
from display.components.Text import Text
from display.components.MenuTextButton import MenuTextButton
from display.compounds.MainCharacterResources import MainCharacterResources
from room.CombatRoom import CombatRoom
from display.components.Background import Background
from MusicPlayer import MusicPlayer


class EndCombatState(BaseMenuState):
    def __init__(self):
        super(EndCombatState, self).__init__()
        self.menu = []
        self.active_index = 0
        self.previous_index = 0
        self.options = []
        MusicPlayer().stop_music()

    def handle_action(self):
        if self.active_index == 0:
            return "TREASURE_ROOM"

        elif self.active_index == 1:
            return "HEAL_ROOM"

        else:
            return "END_COMBAT"

    def run(self):
        if MainCharacter().hp.is_zero():
            return "END"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                return self.handle_menu(event.key)

    def draw(self, surface):
        surface.blit(Background().image, (0, 0))
        MainCharacterResources.draw(surface)

        adder = 300
        for i in range(len(CombatRoom().doors())):
            if CombatRoom().doors()[i].next_room_type.value not in self.menu:
                self.menu.append(CombatRoom().doors()[i].next_room_type.value)
                if i == 0:
                    option = MenuTextButton("versao_final/assets/combatMenuButton.png",
                                            Text("versao_final/assets/fonts/menu_option.ttf", 35,
                                                 pygame.Color(255, 0, 0),
                                                 CombatRoom().doors()[i].next_room_type.value[0]),
                                            CombatRoom().doors()[i].next_room_type.value[1])
                    option.rect = option.surface.get_rect(topleft=(adder, 600))
                    adder += (option.surface.get_width() + 200)
                    self.options.append(option)
                else:
                    option = MenuTextButton("versao_final/assets/combatMenuButton.png",
                                            Text("versao_final/assets/fonts/menu_option.ttf", 35,
                                                 pygame.Color(255, 255, 255),
                                                 CombatRoom().doors()[i].next_room_type.value[0]),
                                            CombatRoom().doors()[i].next_room_type.value[1])
                    option.rect = option.surface.get_rect(topleft=(adder, 600))
                    adder += (option.surface.get_width() + 200)
                    self.options.append(option)

        for index, option in enumerate(self.options):
            option.select() if index == self.active_index else option.unselect()
            option.draw(surface)
