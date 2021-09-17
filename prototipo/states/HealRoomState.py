import pygame
from .BaseMenuState import BaseMenuState
from TextSprite import TextSprite
from Singleton import Singleton
from room.HealRoom import HealRoom
from display.TextButton import TextButton
from display.MainCharacterResources import MainCharacterResources
from display.Text import Text


class HealRoomState(BaseMenuState):
    def __init__(self):
        super(HealRoomState, self).__init__()
        self.active_index = 0
        self.previous_index = 0
        self.options = []
        self.menu = []

        self.adder = 150
        for option in ["Inventory", "Options"]:
            option = TextButton("prototipo/assets/combatMenuButton.png", Text(
                "prototipo/assets/fonts/menu_option.ttf",
                25,
                pygame.Color(255, 255, 255),
                option
            ))
            option.rect = option.surface.get_rect(topleft=(self.adder, 600))
            self.adder += (option.surface.get_width() + 25)

            self.options.append(option)

    def handle_action(self):
        if self.active_index == 0:
            print("Show inventory")
        elif self.active_index == 1:
            return "OPTIONS"
        elif self.active_index == 2:
            return "START_COMBAT"
        elif self.active_index == 3:
            return "TREASURE_ROOM"
        else:
            return "HEAL_ROOM"

    def run(self):
        Singleton.room = HealRoom()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                return self.handle_menu(event.key)

    def draw(self, surface):
        surface.blit(Singleton.background, (0,0))
        MainCharacterResources.draw(surface)

        for door in Singleton.room.doors():
            if door.next_room_type.value not in self.menu:
                self.menu.append(door.next_room_type.value)
                option = TextButton("prototipo/assets/combatMenuButton.png", Text(
                    "prototipo/assets/fonts/menu_option.ttf",
                    25,
                    pygame.Color(255, 255, 255),
                    door.next_room_type.value
                ))
                option.rect = option.surface.get_rect(topleft=(self.adder, 600))
                self.adder += (option.surface.get_width() + 25)
                self.options.append(option)

        for index, option in enumerate(self.options):
            option.draw(surface)
            option.change_text_color(pygame.Color(255, 0, 0) if index == self.active_index else pygame.Color(255, 255, 255))

        heal_room = Text("prototipo/assets/fonts/menu_option.ttf", 25, pygame.Color(255, 255, 255), "Heal Room", (1100, 25))
        heal_room.draw(surface)
