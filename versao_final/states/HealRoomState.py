import pygame
from .BaseMenuState import BaseMenuState
from room.HealRoom import HealRoom
from display.components.MenuTextButton import MenuTextButton
from display.components.Text import Text
from display.compounds.MainCharacterResources import MainCharacterResources
from display.components.Background import Background


class HealRoomState(BaseMenuState):
    def __init__(self):
        super(HealRoomState, self).__init__()
        self.active_index = 0
        self.previous_index = 0
        self.options = []
        self.menu = []

        self.adder = 150
        for option in [("Inventory", "INVENTORY"), ("Options", "OPTIONS")]:
            option = MenuTextButton("versao_final/assets/combatMenuButton.png", Text(
                "versao_final/assets/fonts/menu_option.ttf",
                35,
                pygame.Color(255, 255, 255),
                option[0]
            ), option[1])
            option.rect = option.surface.get_rect(topleft=(self.adder, 600))
            self.adder += (option.surface.get_width() + 25)

            self.options.append(option)

    def handle_action(self):
        return self.options[self.active_index].on_pressed()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                return self.handle_menu(event.key)

    def draw(self, surface):
        surface.blit(Background().image, (0,0))
        MainCharacterResources.draw(surface)

        for door in HealRoom().doors():
            if door.next_room_type.value not in self.menu:
                self.menu.append(door.next_room_type.value)
                option = MenuTextButton("versao_final/assets/combatMenuButton.png", Text(
                    "versao_final/assets/fonts/menu_option.ttf",
                    35,
                    pygame.Color(255, 255, 255),
                    door.next_room_type.value[0]
                ), door.next_room_type.value[1])
                option.rect = option.surface.get_rect(topleft=(self.adder, 600))
                self.adder += (option.surface.get_width() + 25)
                self.options.append(option)

        for index, option in enumerate(self.options):
            option.select() if index == self.active_index else option.unselect()
            option.draw(surface)

        heal_room = Text("versao_final/assets/fonts/menu_option.ttf", 25, pygame.Color(255, 255, 255), "Heal Room", (1100, 25))
        heal_room.draw(surface)
