import pygame
from Singleton import Singleton
from TextSprite import TextSprite
from states.BaseMenuState import BaseMenuState


class EndCombat(BaseMenuState):
    def __init__(self):
        super(EndCombat, self).__init__()
        self.active_index = 0
        self.previous_index = 0
        self.options = []
        self.player_hp = None
        self.opponent_hp = None
        options = ["Treasure Room", "Heal Room"]

        index = (800/2) - 100*2

        surface = self.font.render(options[0], True, pygame.Color("red"))
        self.options.append(TextSprite(options[0], surface, surface.get_rect(topleft=(index, 500))))

        for option in options[1:]:
            index += 300
            surface = self.font.render(option, True, pygame.Color("white"))
            self.options.append(TextSprite(option, surface, surface.get_rect(topleft=(index, 500))))
    def handle_action(self):
        if self.active_index == 0:
            return "TREASURE_ROOM"

        elif self.active_index == 1:
            return "HEAL_ROOM"

        else:
            return "END_COMBAT"

    def run(self):
        Singleton.opponent = None
        if Singleton.main_character.hp.is_zero():
            return "END"

        player_hp_text = f"Player HP: {Singleton.main_character.hp.current}/{Singleton.main_character.hp.max}"

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
        surface.fill(pygame.Color("blue"))
        surface.blit(Singleton.background, (0,0))

        for option in [*self.options]:
            surface.blit(option.surf, option.rect)
