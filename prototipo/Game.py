import pygame


FPS = 60
FramePerSec = pygame.time.Clock()

class Game:
    def __init__(self, screen, states, start_state):
        self.screen = screen
        self.states = states
        self.current_state = self.states[start_state]
        self.previous_state = self.current_state

    def update_state(self, next_state_key):
        if next_state_key == None:
            return
        if next_state_key == "PREVIOUS":
            self.current_state, self.previous_state = self.previous_state, self.current_state
        elif next_state_key == "QUIT":
            quit()
        else:
            self.previous_state = self.current_state
            self.current_state = self.states[next_state_key]
            
    def run_current_state(self):
        "Calls the current state's routine. Returns the key to the next state, or None if the state should not be changed."
        return self.current_state.run()

    def run(self):
        while True:
            next_state_key = self.run_current_state()
            self.current_state.draw(self.screen)
        
            pygame.display.update()
            FramePerSec.tick(FPS)

            self.update_state(next_state_key)