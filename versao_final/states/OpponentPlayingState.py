import pygame
from .BaseState import BaseState
from creators.OpponentCreator import OpponentCreator
from fighter.main_character.MainCharacter import MainCharacter
from display.compounds.MainCharacterResources import MainCharacterResources
from display.compounds.OpponentResources import OpponentResources
from creators.OpponentCreator import OpponentCreator
from display.components.Background import Background
from display.components.Text import Text


class OpponentPlayingState(BaseState):
    def __init__(self):
        super(OpponentPlayingState, self).__init__()
        self.player_hp = None
        self.opponent_hp = None
        self.time_active = 0
        self.__active_skills = []

        OpponentCreator.current.ap.increase_current(2)
        OpponentCreator.current.update_lingering_effects()
        OpponentCreator.current.update_skills_cooldown()

    def draw(self, surface):
        surface.blit(Background().image, (0,0))

        for skill in self.__active_skills:
            skill.opponent_animation.draw(surface)

        combat_room = Text("versao_final/assets/fonts/menu_option.ttf", 25, pygame.Color(255, 255, 255), "Combat Room", (1100, 25))
        combat_room.draw(surface)

        OpponentCreator.current.draw(surface)
        MainCharacterResources.draw(surface)
        OpponentResources.draw(surface)


    def handle_action(self):
        skill = OpponentCreator.current.choose_skill()

        if not skill:
            return "MAIN_CHARACTER_PLAYING"

        if skill not in self.__active_skills:
            if skill.opponent_animation:
                skill.opponent_animation.reset()
                self.__active_skills.append(skill)
            else:
                OpponentCreator.current.use_skill(skill, MainCharacter())

            OpponentCreator.current.ap.decrease_current(skill.cost)

        if MainCharacter().hp.is_zero():
            return "END"
        elif OpponentCreator.current.ap.is_zero() and not self.__active_skills:
            return "MAIN_CHARACTER_PLAYING"


    def apply_skills(self):
        for index, skill in enumerate(self.__active_skills):
            if skill.opponent_animation.finished:
                OpponentCreator.current.use_skill(skill, MainCharacter())
                self.__active_skills.pop(index)
            else:
                skill.opponent_animation.update()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

        self.apply_skills()

        self.time_active += 1
        if self.time_active > 60:
            self.time_active = 0
            return self.handle_action()
