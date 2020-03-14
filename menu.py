import pygame
from skins import Skin, Demo
from buttons import Button


class Skins_Choice():
    def __init__(self, game):
        self.background = pygame.image.load("assets/skins_choice.png").convert_alpha()
        self.quit = Button("assets/buttons/quit.png", "assets/buttons/quit_hover.png", 55, 40)

        self.game = game

        self.skins = pygame.sprite.Group()

        self.skin_init_x = self.background.get_rect().x + 100
        self.skin_init_y = self.background.get_rect().y + 100

        for obj in self.game.total_skins:
            self.skins.add(Skin(obj, self.game.total_skins[obj], self.skin_init_x, self.skin_init_y))

            self.skin_init_x += 100
            self.check_init_lenght()

        self.demo = Demo(self.game.choosed_skin)
            

    def check_init_lenght(self):
        if self.skin_init_x >= self.background.get_rect().x + self.background.get_rect().width - 100:
            self.skin_init_x = self.background.get_rect().x + 100
            self.skin_init_y += 100