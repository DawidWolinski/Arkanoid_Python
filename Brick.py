import pygame as pg


class Brick:
    def __init__(self, type, x, y):
        self.hp = 1
        self.type = type
        self.x = x
        self.y = y
        self.sprite = pg.image.load("Assets/Textures/Bricks.png")
        self.sprite = pg.transform.scale(self.sprite, (128*3, 192*3))
        self.sprite_rect = (0*3, 0*3, 16*3, 8*3)
        self.points = 50
        self.set_type()

    def set_type(self):
        # White
        if self.type == 0:
            self.sprite_rect = (0*3, 0*3, 16*3, 8*3)
            self.points = 50
        # Orange
        elif self.type == 1:
            self.sprite_rect = (16*3, 0*3, 16*3, 8*3)
            self.points = 60
        # Cyan
        elif self.type == 2:
            self.sprite_rect = (32*3, 0*3, 16*3, 8*3)
            self.points = 70
        # Green
        elif self.type == 3:
            self.sprite_rect = (48*3, 0*3, 16*3, 8*3)
            self.points = 80
        # Red
        elif self.type == 4:
            self.sprite_rect = (0*3, 8*3, 16*3, 8*3)
            self.points = 90
        # Blue
        elif self.type == 5:
            self.sprite_rect = (16*3, 8*3, 16*3, 8*3)
            self.points = 100
        # Pink
        elif self.type == 6:
            self.sprite_rect = (32*3, 8*3, 16*3, 8*3)
            self.points = 110
        # Yellow
        elif self.type == 7:
            self.sprite_rect = (48*3, 8*3, 16*3, 8*3)
            self.points = 120
        # Iron - needs to be hit twice
        elif self.type == 8:
            self.sprite_rect = (0*3, 16*3, 16*3, 8*3)
            self.points = 130
            self.hp = 2
        # Golden - indestructible
        elif self.type == 9:
            self.sprite_rect = (0*3, 24*3, 16*3, 8*3)
            self.points = 0

    # Checks from which side the ball hit the brick
    def collision_side(self, ball_x, ball_y):
        dx = abs(ball_x - (self.x + self.sprite_rect[2]/2)) - self.sprite_rect[2]/2
        dy = abs(ball_y - (self.y + self.sprite_rect[3]/2)) - self.sprite_rect[3]/2

        if dy < dx:
            # Right
            if ball_x > self.x:
                return 0
            # Left
            elif ball_x < self.x:
                return 1
        else:
            # Bottom
            if ball_y > self.y:
                return 2
            # Top
            elif ball_y < self.y:
                return 3

    def draw(self, surface):
        surface.blit(self.sprite, (self.x, self.y), self.sprite_rect)
