import pygame
import random


from player import Player
from wall import Wall

class Game():
    def __init__(self, difficulty):
        self.player = Player(self)
        self.walls = pygame.sprite.Group()

        self.framerate = 60
        self.clock = pygame.time.Clock()

        self.is_gameover = False

        self.is_wall_generated = 0

        #Difficulty : 0 : Easy, 1 : Normal, 2 : Hard
        self.difficulty = difficulty

        if self.difficulty == 0:
            self.wall_generating_rarther = 300
        elif self.difficulty == 1:
            self.wall_generating_rarther = 200
        elif self.difficulty == 2:
            self.wall_generating_rarther = 100


    def try_gererate_wall(self):

        self.is_wall_generated = random.randint(0, self.wall_generating_rarther)
        if self.is_wall_generated == 0:
            self.walls.add(Wall(self))

