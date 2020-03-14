import pygame
import random
import pickle


from player import Player
from wall import Wall

class Game():
    def __init__(self, difficulty):
        self.player = Player(self)
        self.walls = pygame.sprite.Group()

        self.saver = None

        self.score = 0

        self.framerate = 60
        self.clock = pygame.time.Clock()

        self.is_gameover = False

        self.is_wall_generated = 0

        self.total_skins = {
            "bee_yellow" : "assets/skins/bee_yellow.png", "blue" : "assets/skins/blue.png", "blue_swirl" : "assets/skins/blue_swirl.png",
            "bubble_gum" : "assets/skins/bubble_gum.png", "colorful_swirl" : "assets/skins/colorful_swirl.png", "darkpurple_circle" : "assets/skins/darkpurple_circle.png",
            "default" : "assets/skins/default.png", "green_ray" : "assets/skins/green_ray.png", "green_swirl" : "assets/skins/green_swirl.png",
            "honey" : "assets/skins/honey.png", "ice_spiral" : "assets/skins/ice_spiral.png", "lightray" : "assets/skins/lightray.png", "multicolor" : "assets/skins/multicolor.png",
            "old" : "assets/skins/old.png", "old_gold" : "assets/skins/old_gold.png", "purple_bubble" : "assets/skins/purple_bubble.png",
            "purple_swirl" : "assets/skins/purple_swirl.png", "ray" : "assets/skins/ray.png", "red_light" : "assets/skins/red_light.png",
            "red_swirl" : "assets/skins/red_swirl.png", "space" : "assets/skins/space.png", "tropical" : "assets/skins/tropical.png", "white" : "assets/skins/white.png",
            "yellow_swirl" : "assets/skins/yellow_swirl.png"
        }
        self.unlocked_skins = {}
        self.choosed_skin = self.total_skins["default"]


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

    def save(self):
        self.saver = [self.unlocked_skins, self.choosed_skin]
        pickle.dump(self.saver, open("conf.dat", "wb"))
        
    def load(self):
        self.saver = pickle.load(open("conf.dat", "rb"))
        self.unlocked_skins = self.saver[0]
        self.choosed_skin = self.saver[1]


