from fighter.main_character.MainCharacter import MainCharacter
import pygame
from Singleton import Singleton
from TextSprite import TextSprite
from states.BaseMenuState import BaseMenuState
from display.Text import Text
from display.TextButton import TextButton
from display.MainCharacterResources import MainCharacterResources


class EndCombatState(BaseMenuState):
    def __init__(self):
        super(EndCombatState, self).__init__()
        self.menu = []
        self.active_index = 0
        self.previous_index = 0
        self.options = []
        self.player_hp = None
        self.opponent_hp = None

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

        player_hp_text = f"Player HP: {MainCharacter().hp.current}/{MainCharacter().hp.max}"

        surface = self.font.render(player_hp_text, True, pygame.Color("blue"))
        self.player_hp = (TextSprite(player_hp_text, surface, surface.get_rect(topleft=(10,10))))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                return self.handle_menu(event.key)

    def draw(self, surface):
        surface.blit(Singleton.background, (0,0))

        adder = 300
        for i in range(len(Singleton.room.doors())):
            if Singleton.room.doors()[i].next_room_type.value not in self.menu:
                self.menu.append(Singleton.room.doors()[i].next_room_type.value)
                if i == 0:
                    option = TextButton("prototipo/assets/combatMenuButton.png", Text("prototipo/assets/fonts/menu_option.ttf", 25, pygame.Color(255, 0, 0), Singleton.room.doors()[i].next_room_type.value))
                    option.rect = option.surface.get_rect(topleft=(adder, 600))
                    adder += (option.surface.get_width() + 200)
                    self.options.append(option)
                else:
                    option = TextButton("prototipo/assets/combatMenuButton.png", Text("prototipo/assets/fonts/menu_option.ttf", 25, pygame.Color(255, 255, 255), Singleton.room.doors()[i].next_room_type.value))
                    option.rect = option.surface.get_rect(topleft=(adder, 600))
                    adder += (option.surface.get_width() + 200)
                    self.options.append(option)

        for index, option in enumerate(self.options):
            option.draw(surface)
            option.change_text_color(pygame.Color(255, 0, 0) if index == self.active_index else pygame.Color(255, 255, 255))
