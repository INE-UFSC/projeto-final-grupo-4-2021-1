from skill.Skill import Skill
from .IconButton import IconButton
from fighter.main_character.MainCharacter import MainCharacter
from fighter.opponent.Opponent import Opponent


class SkillIconButton(IconButton):
    def __init__(self, skill: Skill):
        self.__skill = skill
        super().__init__(skill.icon_path, None)

    @property
    def skill(self):
        return self.__skill

    def on_pressed(self):
        MainCharacter().use_skill(self.__skill, Opponent())