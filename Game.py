import pygame as pg


# Class responsible for changing states and running their methods
class Game:
    def __init__(self, screen, states, start_state, title, icon):
        self.done = False
        self.screen = screen
        self.clock = pg.time.Clock()
        self.fps = 60
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]
        pg.display.set_caption(title)
        pg.display.set_icon(icon)

    # Changes to next state
    def change_state(self):
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        data = self.state.data
        self.state = self.states[self.state_name]
        self.state.startup(data)

    # Handling input
    def handle_event(self):
        for event in pg.event.get():
            self.state.get_event(event)

    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.change_state()
        self.state.update(dt)

    # Displaying objects to the screen
    def draw(self):
        self.state.draw(self.screen)

    # The core function of the game's runtime
    def run(self):
        while not self.done:
            # dt - milliseconds since last frame. Used for frame-independent gameplay
            dt = self.clock.tick(self.fps)/1000

            self.handle_event()
            self.update(dt)
            self.draw()

            pg.display.update()
