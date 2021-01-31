from State import State
import pygame as pg
from LevelCreator import LevelCreator
from Paddle import Paddle
from Ball import Ball


class GameplayState(State):
    def __init__(self):
        super(GameplayState, self).__init__()
        self.next_state = "GameOver"

        # We start at level 0 but you can just cheat and change it
        self.level = 0
        self.creator = LevelCreator()

        # List with all bricks in the current map/level
        self.layout = self.creator.create_level(self.level)

        # Used for level starting sequence (or after dying) - Round -> Ready -> bounce ball
        # Look at round_start() method
        self.phase = 0
        self.time = 0
        self.w = pg.display.get_surface().get_width()
        self.font = pg.font.Font("Assets/Fonts/ARCADE_N.TTF", 20)
        self.round = self.font.render("round " + str(self.level+1), True, (255, 255, 255))
        self.ready = self.font.render("ready", True, (255, 255, 255))
        self.ready_pos = self.ready.get_rect(center=(self.w/2, 580))
        self.display_round = False
        self.display_ready = False

        # Text showcasing current score
        self.score_font = pg.font.Font("Assets/Fonts/ARCADE_N.TTF", 25)
        self.score_count = 0
        self.score = self.score_font.render("score:" + str(self.score_count), True, (255, 255, 255))

        self.background = pg.image.load("Assets/Textures/Backgrounds.png")
        self.background = pg.transform.scale(self.background, (1152*3, 496*3))

        # Ball cannot fall below bottom boundary
        self.bottom_boundary = pg.display.get_surface().get_height()
        self.start = True

        # Objects denoting number of lives (max is 6)
        self.hp_count = 3
        self.hp = []
        for i in range(5):
            self.hp.append(pg.image.load("Assets/Textures/Backgrounds.png"))
            self.hp[i] = pg.transform.scale(self.hp[i], (1152*3, 496*3))

        self.paddle = Paddle()
        self.ball = Ball()

    def startup(self, data):
        self.data = data

    # Places ball on the paddle
    def position_ball(self):
        self.ball.x = self.paddle.x + self.paddle.sprite_rect[2]/2 - self.ball.sprite_rect[2]/2
        self.ball.y = self.paddle.y - self.ball.sprite_rect[3]

    # Level starting sequence
    def round_start(self, dt):
        if self.phase == 0:
            self.round = self.font.render("round " + str(self.level+1), True, (255, 255, 255))
            self.round_pos = self.round.get_rect(center=(self.w/2, 530))
            self.display_round = True
            self.position_ball()
            self.time += dt
            if self.time >= 1.5:
                self.phase += 1
        elif self.phase == 1:
            self.display_ready = True
            self.position_ball()
            self.time += dt
            if self.time >= 3:
                self.phase += 1
        elif self.phase == 2:
            self.display_round = False
            self.display_ready = False
            self.ball.is_moving = True
            self.phase = 0
            self.time = 0
            self.start = False

    # Checks if two objects are colliding with each other
    def are_colliding(self, object_a, object_b):
        if object_a.x < object_b.x + object_b.sprite_rect[2] and object_a.x + object_a.sprite_rect[2] > object_b.x and object_a.y < object_b.y + object_b.sprite_rect[3] and object_a.y + object_a.sprite_rect[3] > object_b.y:
            return True
        else:
            return False

    # Handles collisions of
    def handle_collisions(self):
        # Collision of ball with bricks
        for index, brick in enumerate(self.layout):
            if self.are_colliding(self.ball, brick):
                collision_side = brick.collision_side(self.ball.x + self.ball.sprite_rect[2]/2, self.ball.y + self.ball.sprite_rect[3]/2)
                self.ball.reflect(collision_side)
                brick.hp -= 1
                if brick.hp <= 0:
                    self.score_count += brick.points
                    self.score = self.score_font.render("score:" + str(self.score_count), True, (255, 255, 255))
                    del self.layout[index]

        # Collision of ball with paddle
        if self.are_colliding(self.ball, self.paddle):
            collision_side = self.paddle.collision_side(self.ball.x + self.ball.sprite_rect[2]/2, self.ball.y + self.ball.sprite_rect[3]/2)
            self.ball.reflect_paddle(collision_side)

        # Collision of ball with the floor
        if self.ball.y - 10*3 > self.bottom_boundary and self.ball.is_moving:
            self.hp_count -= 1
            self.ball.is_moving = False
            self.start = True

    # Resets objects and data
    def reset_gameplay(self):
        self.hp_count = 3
        self.level = 0
        self.start = True
        self.score_count = 0
        self.score = self.score_font.render("score:" + str(self.score_count), True, (255, 255, 255))
        self.paddle.reset_position()
        self.position_ball()
        self.layout = self.creator.create_level(0)
        self.ball.is_moving = False

    def check_state_of_game(self, dt):
        if self.start:
            # If player runs out of lives - lose
            if self.hp_count <= 0:
                self.data["victory"] = False
                self.reset_gameplay()
                self.done = True
            # If not
            else:
                self.round_start(dt)
        # If player breaks all the bricks (except golden ones)
        elif len(self.layout) == self.creator.golden_bricks:
            self.level += 1
            # Next level
            if not self.creator.return_layout(self.level):
                self.data["victory"] = True
                self.reset_gameplay()
                self.done = True
            # If it's the last level
            else:
                self.layout = self.creator.create_level(self.level)
                self.start = True
                self.ball.is_moving = False

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                self.paddle.move_left = True
            elif event.key == pg.K_RIGHT:
                self.paddle.move_right = True
            elif event.key == pg.K_p:
                self.position_ball()
                self.ball.is_moving = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                self.paddle.move_left = False
            elif event.key == pg.K_RIGHT:
                self.paddle.move_right = False

    def update(self, dt):
        self.check_state_of_game(dt)

        self.paddle.update(dt)

        self.ball.update(dt)

        self.handle_collisions()

    def draw(self, surface):
        surface.fill((0, 0, 0))

        surface.blit(self.background, (0, 16*3), self.creator.get_background_rect(self.level))

        for i in range(self.hp_count - 1):
            surface.blit(self.hp[i], (10*3 + i*16*3, 740), self.creator.get_hp_rect(self.level))

        for brick in self.layout:
            brick.draw(surface)

        self.paddle.draw(surface)

        self.ball.draw(surface)

        surface.blit(self.score, (220, 15))

        if self.display_round:
            surface.blit(self.round, self.round_pos)

        if self.display_ready:
            surface.blit(self.ready, self.ready_pos)
