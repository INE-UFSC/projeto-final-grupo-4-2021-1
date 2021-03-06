from fighter.main_character.MainCharacter import MainCharacter
import pygame
from .BaseMenuState import BaseMenuState
from display.components.Text import Text
import pygame
from item.Equipment import Equipment


class EquipmentState(BaseMenuState):
    def __init__(self):
        super(EquipmentState, self).__init__()
        self.active_index = 0

        font = "versao_final/assets/fonts/menu_option.ttf"

        self.options = [Text(font,
                             60,
                             pygame.Color(255, 255, 0),
                             f"+{option}"
                             ) for option in [
                            "Weapon",
                            "Armor",
                            "Trinket",
                            "Return"]]
        menu_height = 0
        for option in self.options:
            option.rect = option.surface.get_rect(center=(250, 300 + menu_height))
            menu_height += (option.surface.get_height() + 10)

        self.weapon_info = [Text(font,
                                 30,
                                 pygame.Color(255, 255, 0),
                                 f"{info}"
                                 ) for info in [
                                f"Name: {MainCharacter().equipment.weapon.name}",
                                f"Damage: {list(MainCharacter().equipment.weapon.base_damage.values())[0]}",
                                f"Weight: {MainCharacter().equipment.weapon.weight}lbs",
                                f"Description: {MainCharacter().equipment.weapon.description}"]]
        menu_height = 0
        for info in self.weapon_info:
            info.rect = info.surface.get_rect(center=(800, 300 + menu_height))
            menu_height += (info.surface.get_height() + 10)

        self.armor_info = [Text(font,
                                30,
                                pygame.Color(255, 255, 0),
                                f"{info}"
                                ) for info in [
                               f"Name: {MainCharacter().equipment.armor.name}",
                               f"Protection: {list(MainCharacter().equipment.armor.base_armor.values())[0]}",
                               f"Weight: {MainCharacter().equipment.armor.weight}lbs",
                               f"Description: {MainCharacter().equipment.armor.description}"]]
        menu_height = 0
        for info in self.armor_info:
            info.rect = info.surface.get_rect(center=(800, 300 + menu_height))
            menu_height += (info.surface.get_height() + 10)

        self.trinket_info = [Text(font,
                                  30,
                                  pygame.Color(255, 255, 0),
                                  f"{info}"
                                  ) for info in [
                                 f"Name: {MainCharacter().equipment.trinket.name}",
                                 f"Weight: {MainCharacter().equipment.trinket.weight}lbs",
                                 f"Description: {MainCharacter().equipment.trinket.description}"]]
        menu_height = 0
        for info in self.trinket_info:
            info.rect = info.surface.get_rect(center=(800, 300 + menu_height))
            menu_height += (info.surface.get_height() + 10)

    def render_text(self, index):
        color = pygame.Color(255, 0, 0) if index == self.active_index else pygame.Color(255, 255, 255)
        return self.font.render(self.options[index], True, color)

    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)

    def handle_action(self):
        if self.active_index == 0:
            pass
        elif self.active_index == 1:
            pass
        elif self.active_index == 2:
            pass
        else:
            return "PREVIOUS"

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                return self.handle_menu(event.key)

    def draw(self, surface):
        surface.fill(pygame.Color(0, 0, 0))
        for index, option in enumerate(self.options):
            option.color = pygame.Color(255, 0, 0) if index == self.active_index else pygame.Color(255, 255, 255)
            surface.blit(option.surface, option.rect)

        if self.active_index == 0:
            for index, info in enumerate(self.weapon_info):
                surface.blit(info.surface, info.rect)
        elif self.active_index == 1:
            for index, info in enumerate(self.armor_info):
                surface.blit(info.surface, info.rect)
        elif self.active_index == 2:
            for index, info in enumerate(self.trinket_info):
                surface.blit(info.surface, info.rect)
