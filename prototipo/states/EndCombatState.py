from fighter.main_character.MainCharacter import MainCharacter
import pygame
from Singleton import Singleton
from TextSprite import TextSprite
from states.BaseMenuState import BaseMenuState


class EndCombatState(BaseMenuState):
    def __init__(self):
        super(EndCombatState, self).__init__()
        self.menu = []
        self.active_index = 0
        self.previous_index = 0
        self.options = []
        self.player_hp = None
        self.opponent_hp = None

        self.index = 100

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

        if self.active_index != self.previous_index:
            self.options[self.active_index].surf = self.font.render(self.options[self.active_index].text, True, pygame.Color("red"))
            self.options[self.previous_index].surf = self.font.render(self.options[self.previous_index].text, True, pygame.Color("white"))
            self.previous_index = self.active_index

    def draw(self, surface):
        print(f"ec {len(self.options)}")
        surface.blit(Singleton.background, (0,0))

        for i in range(len(Singleton.room.doors())):
            if Singleton.room.doors()[i].next_room_type.value not in self.menu:
                self.menu.append(Singleton.room.doors()[i].next_room_type.value)
                self.index += 150
                if i == 0:
                    surface = self.font.render(Singleton.room.doors()[i].next_room_type.value, True, pygame.Color("red"))
                    self.options.append(TextSprite(Singleton.room.doors()[i].next_room_type.value, surface, surface.get_rect(topleft=(self.index, 500))))

                else:
                    surface = self.font.render(Singleton.room.doors()[i].next_room_type.value, True, pygame.Color("white"))
                    self.options.append(TextSprite(Singleton.room.doors()[i].next_room_type.value, surface, surface.get_rect(topleft=(self.index, 500))))



        for option in [*self.options]:
            surface.blit(option.surf, option.rect)