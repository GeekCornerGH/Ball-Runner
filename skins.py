import pygame

class Skin(pygame.sprite.Sprite):

    def __init__(self, name, image, x, y):
        super().__init__()

        self.path = image
        self.oImage = pygame.image.load(image)
        self.image = self.oImage

        self.is_touch = False

        self.name = name

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def check_hover(self, pos):
        if pos[0] > self.rect.x and pos[0] < self.rect.x + self.rect.width:
            if pos[1] > self.rect.y and pos[1] < self.rect.y + self.rect.height:
                self.is_touch = True
                return True
        self.is_touch = False
        return False

    def a_hover(self):
        self.image = pygame.transform.rotozoom(self.oImage, 0, 1.1)

    def a_normal(self):
        self.image = self.oImage


class Demo():
    def __init__(self, image):

        self.oImage = pygame.image.load(image)
        self.image = self.oImage

        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500

        self.rotate_angle = -20
        self.angle = 0

    def rotate(self):
        self.image = pygame.transform.rotozoom(self.oImage, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.angle += self.rotate_angle

    def change(self, image):
        self.oImage = pygame.image.load(image)

