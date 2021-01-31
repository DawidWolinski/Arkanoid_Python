import pygame as pg
from math import pi, cos, sin


class Ball:
    def __init__(self):
        self.sprite = pg.image.load("Assets/Textures/Paddles.png")
        self.sprite = pg.transform.scale(self.sprite, (252*3, 100*3))
        self.sprite_rect = (0*3, 40*3, 5*3, 4*3)
        self.x = 0
        self.y = 900
        self.is_moving = False
        self.velocity_x = 500
        self.velocity_y = 500
        self.speed = 500
        self.left_boundary = 8*3
        self.right_boundary = pg.display.get_surface().get_width() - 8*3
        self.top_boundary = 16*3 + 8*3

    # Changes direction and angle of ball's movement based on which side of the paddle or brick it hit
    def reflect(self, collision_side, angles=0):
        # If it paddle
        if angles != 0:
            self.change_angle(angles)

        if collision_side == 0:     # Right
            self.velocity_x = abs(self.velocity_x)
        elif collision_side == 1:   # Left
            self.velocity_x = -abs(self.velocity_x)
        elif collision_side == 2:   # Bottom
            self.velocity_y = abs(self.velocity_y)
        elif collision_side == 3:   # Top
            self.velocity_y = -abs(self.velocity_y)

    def change_angle(self, angles):
        radians = 2 * pi * (angles/360)

        if self.velocity_x >= 0:
            self.velocity_x = self.speed * cos(radians)
        else:
            self.velocity_x = -self.speed * cos(radians)

        if self.velocity_y >= 0:
            self.velocity_y = self.speed * sin(radians)
        else:
            self.velocity_y = -self.speed * sin(radians)

    def reflect_paddle(self, collision_side):
        if collision_side == 1:
            self.reflect(1, 30)
            self.reflect(3)
        elif collision_side == 2:
            self.reflect(0, 30)
            self.reflect(3)
        elif collision_side == 3:
            self.reflect(1, 45)
            self.reflect(3)
        elif collision_side == 4:
            self.reflect(0, 45)
            self.reflect(3)
        elif collision_side == 5:
            self.reflect(1, 65)
            self.reflect(3)
        elif collision_side == 6:
            self.reflect(0, 65)
            self.reflect(3)
        elif collision_side == 7:
            self.change_angle(65)
            self.reflect(3)

    def draw(self, surface):
        surface.blit(self.sprite, (self.x, self.y), self.sprite_rect)

    def update(self, dt):
        if self.is_moving:
            self.x += self.velocity_x*dt
            self.y += self.velocity_y*dt

            # Bounces ball off the edges of screen
            if self.x > self.right_boundary:
                self.velocity_x = -abs(self.velocity_x)
            if self.x < self.left_boundary:
                self.velocity_x = abs(self.velocity_x)
            if self.y < self.top_boundary:
                self.velocity_y = abs(self.velocity_y)
