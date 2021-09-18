from fighter.main_character.MainCharacter import MainCharacter
import pygame
from .BaseMenuState import BaseMenuState
from TextSprite import TextSprite
from Singleton import Singleton
from room.HealRoom import HealRoom


class HealRoomState(BaseMenuState):
    def __init__(self):
        super(HealRoomState, self).__init__()
        self.active_index = 0
        self.previous_index = 0
        self.options = []
        options = ["Inventory", "Options"]
        self.menu = []
        self.index = 100

        surface = self.font.render(options[0], True, pygame.Color("red"))
        self.options.append(TextSprite(options[0], surface, surface.get_rect(topleft=(self.index, 500))))
        for option in options[1:]:
            self.index += 130
            surface = self.font.render(option, True, pygame.Color("white"))
            self.options.append(TextSprite(option, surface, surface.get_rect(topleft=(self.index, 500))))

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

        if self.active_index != self.previous_index:
            self.options[self.active_index].surf = self.font.render(self.options[self.active_index].text, True, pygame.Color("red"))
            self.options[self.previous_index].surf = self.font.render(self.options[self.previous_index].text, True, pygame.Color("white"))
            self.previous_index = self.active_index

        player_hp_text = f"Player HP: {MainCharacter().hp.current}/{MainCharacter().hp.max}"
        surface = self.font.render(player_hp_text, True, pygame.Color("blue"))
        self.player_hp = (TextSprite(player_hp_text, surface, surface.get_rect(topleft=(10,10))))

        room_text = "Heal Room"
        surface = self.font.render(room_text, True, pygame.Color("green"))
        self.room = (TextSprite(room_text, surface, surface.get_rect(topleft=(670,10))))

    def draw(self, surface):
        print(f"hr {len(self.options)}")
        surface.blit(Singleton.background, (0,0))
        surface.blit(self.player_hp.surf, self.player_hp.rect)

        for door in Singleton.room.doors():
            if door.next_room_type.value not in self.menu:
                self.index += 130
                self.menu.append(door.next_room_type.value)
                surface = self.font.render(door.next_room_type.value, True, pygame.Color("white"))
                self.options.append(TextSprite(door.next_room_type.value, surface, surface.get_rect(topleft=(self.index, 500))))

        for option in [*self.options, self.room]:
            surface.blit(option.surf, option.rect)
