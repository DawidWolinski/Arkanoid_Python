from State import State
import pygame as pg


class MenuState(State):
    def __init__(self):
        super(MenuState, self).__init__()
        self.next_state = "Gameplay"

        # Saves screen size
        w, h = pg.display.get_surface().get_size()

        # Saves fonts
        self.font = pg.font.Font("Assets/Fonts/ARCADE_N.TTF", 30)
        self.font_2 = pg.font.Font("Assets/Fonts/ARCADE_N.TTF", 20)

        # Adds Arkanoid logo
        self.logo = pg.image.load("Assets/Textures/Arkanoid_Ship.png")
        self.logo = pg.transform.scale(self.logo, (392*3, 1037*3))

        # Adds menu options
        self.menu_options = []
        self.options_positions = []
        self.option_strings = ["PLAY", "EXIT"]
        # PLAY
        self.menu_options.append(self.font.render(self.option_strings[0], True, (255, 255, 0)))
        self.options_positions.append(self.menu_options[0].get_rect(center=(w/2, 400)))
        # EXIT
        self.menu_options.append(self.font.render(self.option_strings[1], True, (255, 255, 255)))
        self.options_positions.append(self.menu_options[0].get_rect(center=(w/2, 500)))

        # Company name
        self.taito = self.font_2.render("1986 taito corp japan", True, (255, 255, 255))
        self.taito_pos = self.taito.get_rect(center=(w/2, 650))

        self.project_author = self.font_2.render("2021 dawid wolinski", True, (255, 255, 255))
        self.project_author_pos = self.project_author.get_rect(center=(w/2, 700))

        # Current option index
        self.option = 0

    def change_option(self, key):
        # Up
        if key == 0:
            if self.option > 0:
                self.option = self.option - 1
            else:
                self.option = len(self.menu_options) - 1
        # Down
        if key == 1:
            if self.option < len(self.menu_options) - 1:
                self.option = self.option + 1
            else:
                self.option = 0

        for i in range(len(self.menu_options)):
            if i == self.option:
                self.menu_options[i] = self.font.render(self.option_strings[i], True, (255, 255, 0))
            else:
                self.menu_options[i] = self.font.render(self.option_strings[i], True, (255, 255, 255))

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.change_option(0)
            if event.key == pg.K_DOWN:
                self.change_option(1)
            if event.key == pg.K_RETURN:
                if self.option == 0:
                    self.done = True
                elif self.option == 1:
                    self.quit = True

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill((0, 0, 0))

        surface.blit(self.logo, (50, 100), (0, 0, 193*3, 42*3))

        for i in range(len(self.menu_options)):
            surface.blit(self.menu_options[i], self.options_positions[i])

        surface.blit(self.taito, self.taito_pos)

        surface.blit(self.project_author, self.project_author_pos)
