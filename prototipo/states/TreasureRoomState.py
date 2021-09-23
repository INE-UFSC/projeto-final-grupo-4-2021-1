import pygame
from .BaseMenuState import BaseMenuState
from Singleton import Singleton
from room.TreasureRoom import TreasureRoom
from display.components.Text import Text
from display.components.MenuTextButton import MenuTextButton


class TreasureRoomState(BaseMenuState):
    def __init__(self):
        super(TreasureRoomState, self).__init__()
        self.menu = []
        self.active_index = 0
        self.previous_index = 0
        self.options = []

        self.adder = 50
        for option in [("Inventory", "INVENTORY"), ("Select Item", None), ("Options", "OPTIONS")]:
            option = MenuTextButton("prototipo/assets/combatMenuButton.png", Text(
                "prototipo/assets/fonts/menu_option.ttf",
                50,
                pygame.Color(255, 255, 255),
                option[0]
            ), option[1])
            option.rect = option.surface.get_rect(topleft=(self.adder, 600))
            self.adder += (option.surface.get_width() + 20)

            self.options.append(option)

    def handle_action(self):
        return self.options[self.active_index].on_pressed()


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
                option = MenuTextButton("prototipo/assets/combatMenuButton.png", Text(
                    "prototipo/assets/fonts/menu_option.ttf",
                    35,
                    pygame.Color(255, 255, 255),
                    door.next_room_type.value[0]
                ), door.next_room_type.value[1])
                option.rect = option.surface.get_rect(topleft=(self.adder, 600))
                self.adder += (option.surface.get_width() + 20)
                self.options.append(option)

        for index, option in enumerate(self.options):
            option.select() if index == self.active_index else option.unselect()
            option.draw(surface)

        treasure_room = Text("prototipo/assets/fonts/menu_option.ttf", 25, pygame.Color(255, 255, 255), "Treasure Room", (1100, 25))
        treasure_room.draw(surface)