from room.Chest import Chest
import pygame
from .BaseMenuState import BaseMenuState
from room.TreasureRoom import TreasureRoom
from display.components.Text import Text
from display.components.MenuTextButton import MenuTextButton
from display.components.Background import Background
from fighter.main_character.MainCharacter import MainCharacter


class TreasureRoomState(BaseMenuState):
    def __init__(self):
        super(TreasureRoomState, self).__init__()
        self.menu = []
        self.active_index = 0
        self.previous_index = 0
        self.options = []

        self.adder = 50
        for option in [("Inventory", "INVENTORY"), ("Select Item", None), ("Options", "OPTIONS")]:
            option = MenuTextButton("versao_final/assets/combatMenuButton.png", Text(
                "versao_final/assets/fonts/menu_option.ttf",
                35,
                pygame.Color(255, 255, 255),
                option[0]
            ), option[1])
            option.rect = option.surface.get_rect(topleft=(self.adder, 600))
            self.adder += (option.surface.get_width() + 20)

            self.options.append(option)

    def handle_action(self):
        if self.active_index == 1:
            for item in TreasureRoom().chest.items:
                MainCharacter().inventory.add_item(item)

        return self.options[self.active_index].on_pressed()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                return self.handle_menu(event.key)

    def draw(self, surface):
        surface.blit(Background().image, (0,0))

        for door in TreasureRoom().doors():
            if door.next_room_type.value not in self.menu:
                self.menu.append(door.next_room_type.value)
                option = MenuTextButton("versao_final/assets/combatMenuButton.png", Text(
                    "versao_final/assets/fonts/menu_option.ttf",
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

        treasure = MenuTextButton("versao_final/assets/treasure.png", Text(
                    "versao_final/assets/fonts/menu_option.ttf",
                    35,
                    pygame.Color(255, 255, 255),
                    "O"
                ), "O")
        treasure.rect = option.surface.get_rect(topleft=(400, 20))
        treasure.draw(surface)

        adder_item = 75
        item_options = []
        for item in TreasureRoom().chest.items:
            item_option = Text("versao_final/assets/fonts/menu_option.ttf", 25, pygame.Color(255, 255, 255), item.name, (1100, 25))
            item_option.rect = option.surface.get_rect(topleft=(600, adder_item))
            adder_item += 50
            item_options.append(item_option)

        for item_option in item_options:
            item_option.draw(surface)

        treasure_room = Text("versao_final/assets/fonts/menu_option.ttf", 25, pygame.Color(255, 255, 255), "Treasure Room", (1100, 25))
        treasure_room.draw(surface)
