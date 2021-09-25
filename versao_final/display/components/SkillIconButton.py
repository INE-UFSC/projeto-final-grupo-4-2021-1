from skill.Skill import Skill
from .IconButton import IconButton
from fighter.main_character.MainCharacter import MainCharacter
from creators.OpponentCreator import OpponentCreator
import pygame


class SkillIconButton(IconButton):
    def __init__(self, skill: Skill):
        self.__skill = skill
        super().__init__(skill.icon_path, None)

        s = pygame.Surface(self._surface.get_size())
        s.fill((0, 0, 0))
        s.set_alpha(200)
        self.__opaque_rect = s

    @property
    def skill(self):
        return self.__skill

    def on_pressed(self):
        MainCharacter().use_skill(self.__skill, OpponentCreator.current)

    def _blit_selected(self):
        super()._blit_selected()
        self.__blit_availability()

    def _blit_unselected(self):
        super()._blit_unselected()
        self.__blit_availability()

    def __blit_availability(self):
        if self.__skill.active_cooldown or self.__skill.cost > MainCharacter().ap.current:
            self._surface.blit(self.__opaque_rect, (0, 0))
