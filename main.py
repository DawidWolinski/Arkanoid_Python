import sys
import pygame as pg
from Game import Game
from MenuState import MenuState
from GameplayState import GameplayState
from GameOverState import GameOverState


pg.init()
screen = pg.display.set_mode((224*3, 256*3))
icon = pg.image.load("Assets/Textures/arkanoid_icon.png")

states = {"Menu": MenuState(),
          "Gameplay": GameplayState(),
          "GameOver": GameOverState()}


game = Game(screen, states, "Menu", "Arkanoid", icon)
game.run()

pg.quit()
sys.exit()
