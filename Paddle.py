import pygame as pg


class Paddle:
    def __init__(self):
        self.sprite = pg.image.load("Assets/Textures/Paddles.png")
        self.sprite = pg.transform.scale(self.sprite, (252*3, 100*3))
        self.sprite_rect = (32*3, 0*3, 32*3, 8*3)
        self.x = pg.display.get_surface().get_width()/2 - self.sprite_rect[2]/2
        self.y = 700
        self.dt = 0
        self.move_left = False
        self.move_right = False
        self.left_boundary = 8*3
        self.right_boundary = pg.display.get_surface().get_width() - 8*3
        self.velocity = 500

    # Places paddle in the middle of the map
    def reset_position(self):
        self.x = pg.display.get_surface().get_width()/2 - self.sprite_rect[2]/2

    # Checks which side of the paddle was hit by the ball
    def collision_side(self, ball_x, ball_y):
        if ball_y < self.y + self.sprite_rect[3]/2 + self.sprite_rect[3]/4:
            if ball_x <= self.x + 4*3:
                return 1            # Left edge
            elif ball_x >= self.x + self.sprite_rect[2] - 4*3:
                return 2            # Right edge
            else:
                if ball_x <= self.x + 9*3:
                    return 3        # Left red
                elif ball_x >= self.x + self.sprite_rect[2] - 9*3:
                    return 4        # Right red
                else:
                    if ball_x < self.x + self.sprite_rect[2]/2:
                        return 5    # Left silver
                    elif ball_x > self.x + self.sprite_rect[2]/2:
                        return 6    # Right silver
                    else:
                        return 7    # Middle
        return 0

    def draw(self, surface):
        surface.blit(self.sprite, (self.x, self.y), self.sprite_rect)

    def update(self, dt):
        if self.move_left:
            self.x -= self.velocity*dt
            if self.x - self.left_boundary < 0:
                self.x = self.left_boundary
        elif self.move_right:
            self.x += self.velocity*dt
            if self.x + self.sprite_rect[2] > self.right_boundary:
                self.x = self.right_boundary - self.sprite_rect[2]
