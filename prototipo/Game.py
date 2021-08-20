import pygame


FPS = 60
FramePerSec = pygame.time.Clock()

class Game:
    def __init__(self, screen, states, start_state):
        self.screen = screen
        self.states = states
        self.current_state = self.states[start_state]
        self.statesQueue = []

    def update_state(self, next_state_key):
        if next_state_key == None:
            return
        if next_state_key == "PREVIOUS":
            self.statesQueue.pop()
            self.current_state = self.statesQueue[-1]
        elif next_state_key == "QUIT":
            quit()
        else:
            self.current_state = self.states[next_state_key]
            self.statesQueue.append(self.states[next_state_key])


    def draw_current_state(self):
        self.current_state.draw(self.screen)

    def run_current_state(self):
        "Calls the current state's routine. Returns the key to the next state, or None if the state should not be changed."
        return self.current_state.run()

    def run(self):
        while True:
            next_state_key = self.run_current_state()
            self.draw_current_state()
        
            pygame.display.update()
            FramePerSec.tick(FPS)

            self.update_state(next_state_key)