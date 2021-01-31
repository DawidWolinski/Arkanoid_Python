from State import State
import pygame as pg


class GameOverState(State):
    def __init__(self):
        super(GameOverState, self).__init__()
        self.next_state = "Menu"
        self.victory = False

        # Texts
        w = pg.display.get_surface().get_width()
        self.font = pg.font.Font("Assets/Fonts/ARCADE_N.TTF", 20)

        self.press_to_continue = self.font.render("Press any key to continue", True, (255, 255, 255))
        self.press_to_continue_pos = self.press_to_continue.get_rect(center=(w/2, 700))

        self.game_over = self.font.render("game over", True, (255, 255, 255))
        self.game_over_pos = self.game_over.get_rect(center=(w/2, 350))

        self.congratulations = self.font.render("congratulations", True, (255, 255, 255))
        self.congratulations_pos = self.congratulations.get_rect(center=(w/2, 300))

        self.saved = self.font.render("you saved the world!", True, (255, 255, 255))
        self.saved_pos = self.saved.get_rect(center=(w/2, 350))

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        if event.type == pg.KEYDOWN:
            self.done = True

    def startup(self, data):
        self.data = data
        self.victory = self.data["victory"]

    def draw(self, surface):
        surface.fill((0, 0, 0))

        # If the player beat all the levels
        if self.victory:
            surface.blit(self.congratulations, self.congratulations_pos)
            surface.blit(self.saved, self.saved_pos)
        # If the player lost all lives
        else:
            surface.blit(self.game_over, self.game_over_pos)

        surface.blit(self.press_to_continue, self.press_to_continue_pos)
