import pygame as pg


# Parent class which each of the game state will inherit from
class State(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.data = {}
        self.font = pg.font.Font(None, 24)

    # Called when state becomes active. Used to pass information between states
    def startup(self, data):
        self.data = data

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass
