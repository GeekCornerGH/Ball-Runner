import pygame


class Player(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()

        self.game = game

        self.is_jumping = False
        self.jump_count = 12

        self.rotate_speed = -20

        self.image = pygame.image.load("assets/skins/default.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 505

        self.origin_image = pygame.image.load("assets/skins/default.png")

        self.angle = 0

    def move(self):
        if self.angle == 360:
            self.angle = 0
        else:
            self.angle += self.rotate_speed


        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self, image):
        self.origin_image = pygame.image.load(image)
        print("PLayer image updated")
