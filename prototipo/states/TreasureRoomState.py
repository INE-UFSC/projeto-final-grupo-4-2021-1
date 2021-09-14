import pygame
from .BaseMenuState import BaseMenuState
from TextSprite import TextSprite
from Singleton import Singleton


class TreasureRoom(BaseMenuState):
    def __init__(self):
        super(TreasureRoom, self).__init__()
        self.active_index = 0
        self.active_index = 0
        self.previous_index = 0
        self.options = []
        options = ["Inventory", "Select Item", "Options", "Combat Room", "Heal Room"]

        index = 100

        surface = self.font.render(options[0], True, pygame.Color("red"))
        self.options.append(TextSprite(options[0], surface, surface.get_rect(topleft=(index, 500))))
        for option in options[1:]:
            index += 120
            surface = self.font.render(option, True, pygame.Color("white"))
            self.options.append(TextSprite(option, surface, surface.get_rect(topleft=(index, 500))))

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

        if self.active_index != self.previous_index:
            self.options[self.active_index].surf = self.font.render(self.options[self.active_index].text, True, pygame.Color("red"))
            self.options[self.previous_index].surf = self.font.render(self.options[self.previous_index].text, True, pygame.Color("white"))
            self.previous_index = self.active_index

        room_text = "Treasure Room"
        surface = self.font.render(room_text, True, pygame.Color("yellow"))
        self.room = (TextSprite(room_text, surface, surface.get_rect(topleft=(640,10))))

    def draw(self, surface):
        surface.blit(Singleton.background, (0,0))

        for option in [*self.options]:
            surface.blit(option.surf, option.rect)

        surface.blit(self.room.surf, self.room.rect)
