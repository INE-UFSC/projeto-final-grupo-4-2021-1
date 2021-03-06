import pygame
from display.components.Text import Text
from fighter.main_character.MainCharacter import MainCharacter


class MainCharacterResources:
    def draw(self: pygame.Surface):
        topleft = (20, 20)
        current_hp = MainCharacter().hp.current
        max_hp = MainCharacter().hp.max

        pygame.draw.rect(self, (0, 0, 0), pygame.Rect(topleft, (500, 20)), 5)
        pygame.draw.rect(self, (255, 0, 0), pygame.Rect(topleft, (500, 20)))
        pygame.draw.rect(self, (0, 255, 0), pygame.Rect(topleft, (500 * current_hp / max_hp, 20)))

        current_ap = MainCharacter().ap.current
        max_ap = MainCharacter().ap.max
        for index in range(max_ap):
            pygame.draw.circle(self, (150, 150, 150), ((20 * (index)) + topleft[0] + 8, topleft[1] + 35), 8)
            if index < current_ap:
                pygame.draw.circle(self, (0, 0, 255), ((20 * (index)) + topleft[0] + 8, topleft[1] + 35), 6)

        text = Text("versao_final/assets/fonts/menu_option.ttf", 20, pygame.Color(0, 0, 0), f"{current_hp}/{max_hp}",
                    (topleft[0] + 5, topleft[1] + 1))
        text.draw(self)
