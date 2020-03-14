import pygame


class Button():

    def __init__(self, normal, hover, x, y):

        self.normal = pygame.image.load(normal).convert_alpha()
        self.hover = pygame.image.load(hover).convert_alpha()

        self.image = self.normal

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.is_touch = False

    def a_hover(self):
        if self.image == self.normal:
            self.image = self.hover
            self.is_touch = True

    def a_normal(self):
        if self.image == self.hover:
            self.image = self.normal
            self.is_touch = False

    def click(self):
        if self.is_touch == True:
            return True
        return False

    def check_hover(self, pos):
        if pos[0] > self.rect.x and pos[0] < self.rect.x + self.rect.width:
            if pos[1] > self.rect.y and pos[1] < self.rect.y + self.rect.height:
                return True
        return False

    def print_status(self):
        if self.is_touch == True:
            print("Button is touched")
