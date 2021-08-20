import pygame
from .BaseState import BaseState
from TextSprite import TextSprite
# necessario identificar momento em que passar da sala atual para escolher treasureroom ou healroom
# necessario identificar momento em que troca de turno para passar para opponentplaying


class MainCharacterPlaying(BaseState):
    def __init__(self):
        super(MainCharacterPlaying, self).__init__()
        self.active_index = 0
        self.previous_index = 0

        self.options = []
        options = ("Attack", "Effect", "Item", "Options")

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

    def handle_action(self):
        if self.active_index == 0:
            #atacar
            pass
        elif self.active_index == 1:
            # return "TREASURE_ROOM"
            #efeito
            pass
        elif self.active_index == 2:
            # return "END"
            #item
            pass
        elif self.active_index == 3:
            return "MENU"

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if self.active_index > 0:
                        self.active_index -= 1
                    else:
                        self.active_index = 0
                elif event.key == pygame.K_RIGHT:
                    if self.active_index < 3:
                        self.active_index += 1
                    else:
                        self.active_index = 3
                elif event.key == pygame.K_RETURN:
                    return self.handle_action()

        if self.active_index != self.previous_index:
            self.options[self.active_index].surf = self.font.render(self.options[self.active_index].text, True, pygame.Color("red"))
            self.options[self.previous_index].surf = self.font.render(self.options[self.previous_index].text, True, pygame.Color("white"))
            self.previous_index = self.active_index


    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        for option in self.options:
            # text_render = self.render_text(index)
            surface.blit(option.surf, option.rect)
