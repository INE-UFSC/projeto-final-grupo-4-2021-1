import pygame
from .BaseMenuState import BaseMenuState
from Singleton import Singleton
from room.TreasureRoom import TreasureRoom
from display.Text import Text
from display.TextButton import TextButton


class TreasureRoomState(BaseMenuState):
    def __init__(self):
        super(TreasureRoomState, self).__init__()
        self.menu = []
        self.active_index = 0
        self.active_index = 0
        self.previous_index = 0
        self.options = []

        self.adder = 50
        for option in ["Inventory", "Select Item", "Options"]:
            option = TextButton("prototipo/assets/combatMenuButton.png", Text(
                "prototipo/assets/fonts/menu_option.ttf",
                25,
                pygame.Color(255, 255, 255),
                option
            ))
            option.rect = option.surface.get_rect(topleft=(self.adder, 600))
            self.adder += (option.surface.get_width() + 20)

            self.options.append(option)

    def handle_action(self):
        if self.active_index == 0:
            print("inventory selected")
            pass
        elif self.active_index == 1:
            print("select item")
            pass
        elif self.active_index == 2:
            self.done = True
            self.next_state = "MENU"
        elif self.active_index == 3:
            return "START_COMBAT"
        elif self.active_index == 4:
            return "HEAL_ROOM"
        else:
            return "TREASURE_ROOM"

    def run(self):
        Singleton.room = TreasureRoom()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                return self.handle_menu(event.key)

    def draw(self, surface):
        surface.blit(Singleton.background, (0,0))

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
                self.adder += (option.surface.get_width() + 20)
                self.options.append(option)

        for index, option in enumerate(self.options):
            option.draw(surface)
            option.change_text_color(pygame.Color(255, 0, 0) if index == self.active_index else pygame.Color(255, 255, 255))

        treasure_room = Text("prototipo/assets/fonts/menu_option.ttf", 25, pygame.Color(255, 255, 255), "Treasure Room", (1100, 25))
        treasure_room.draw(surface)