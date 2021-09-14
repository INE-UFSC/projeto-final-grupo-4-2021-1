import pygame
from .BaseMenuState import BaseMenuState
from TextSprite import TextSprite
from Singleton import Singleton
# necessario identificar momento em que passar da sala atual para escolher treasureroom ou healroom
# necessario identificar momento em que troca de turno para passar para opponentplaying


class MainCharacterPlaying(BaseMenuState):
    def __init__(self):
        super(MainCharacterPlaying, self).__init__()
        self.active_index = 0
        self.previous_index = 0
        self.__new_round = True

        self.options = []
        self.player_hp = None
        self.opponent_hp = None
        options = ("Attack","Fire attack", "Effect", "Item", "Options")

        #Pls correct the gambiarra as soon as possible
        index = (800/2) - 100*2

        surface = self.font.render(options[0], True, pygame.Color("red"))
        self.options.append(TextSprite(options[0], surface, surface.get_rect(topleft=(index, 500))))
        for option in options[1:]:
            index += 100
            surface = self.font.render(option, True, pygame.Color("white"))
            self.options.append(TextSprite(option, surface, surface.get_rect(topleft=(index, 500))))

        # #Incitializes text surfaces
        # self.options_surfaces.append(self.font.render(self.options_texts[self.active_index], True, pygame.Color("red")))
        # for option in self.options_texts[1:]:
        #     self.options_surfaces.append(self.font.render(option, True, pygame.Color("white")))

    # def render_text(self, index):
    #     color = pygame.Color("red") if index == self.active_index else pygame.Color("white")
    #     return self.font.render(self.options[index], True, color)

    # def get_text_position(self, text, index):
    #     center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
    #     return text.get_rect(center=center)

    
    #Selecting the active index and used skill must be corrected
    def handle_action(self):
        if self.active_index == 3:
            return "OPTIONS"
        
        else:
            if self.active_index == 1:
                Singleton.opponent.get_attacked(Singleton.main_character.use_skill(Singleton.main_character.skills[1]))
            
            elif self.active_index == 2:
                Singleton.opponent.get_attacked(Singleton.main_character.use_skill(Singleton.main_character.skills[2]))

            elif self.active_index == 3:
                print("You used an item! Wow!")
            
            elif self.active_index == 0:
                Singleton.opponent.get_attacked(Singleton.main_character.use_skill(Singleton.main_character.skills[0]))

            if Singleton.opponent.hp.is_zero():
                return "END_COMBAT"
            elif Singleton.main_character.ap.is_zero():
                Singleton.opponent.ap.refill()
                self.__new_round = True
                return "OPPONENT_PLAYING"

    def run(self):
        room_level_text = f"Room Level: {str(Singleton.room.number)}"
        surface = self.font.render(room_level_text, True, pygame.Color("white"))
        self.room_level = (TextSprite(room_level_text, surface, surface.get_rect(topleft=(670,10))))

        if self.__new_round:
            Singleton.main_character.update_combat_status()
            self.__new_round = False

        player_hp_text = f"Player HP: {Singleton.main_character.hp.current}/{Singleton.main_character.hp.max}"
        opponent_hp_text =  f"Opponent HP: {Singleton.opponent.hp.current}/{Singleton.opponent.hp.max}"

        surface = self.font.render(player_hp_text, True, pygame.Color("blue"))
        self.player_hp = (TextSprite(player_hp_text, surface, surface.get_rect(topleft=(10,10))))

        surface = self.font.render(opponent_hp_text, True, pygame.Color("blue"))
        self.opponent_hp = (TextSprite(opponent_hp_text, surface, surface.get_rect(topleft=(10,40))))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                #Corrigir - o menu deve ser atualizado no mesmo ciclo.
                return self.handle_menu(event.key)

        if self.active_index != self.previous_index:
            self.options[self.active_index].surf = self.font.render(self.options[self.active_index].text, True, pygame.Color("red"))
            self.options[self.previous_index].surf = self.font.render(self.options[self.previous_index].text, True, pygame.Color("white"))
            self.previous_index = self.active_index


    def draw(self, surface):
        surface.blit(Singleton.background, (0,0))
        Singleton.opponent.draw(surface)

        for option in [*self.options, self.player_hp, self.opponent_hp, self.room_level]:
            # text_render = self.render_text(index)
            surface.blit(option.surf, option.rect)
