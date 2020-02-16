import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, generator):
        super().__init__()
        self.game = generator


        self.velocity = 25

        self.image = pygame.image.load("assets/wall.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1080
        self.rect.y = 520

    def go_left(self):
        self.rect.x -= self.velocity
        if self.rect.x + self.rect.width < 0:
            self.remove()
        self.check_player_damage()


    def remove(self):
        self.game.walls.remove(self)

    def check_player_damage(self):

        if self.game.player.rect.y + self.game.player.rect.height > self.rect.y:
            if self.game.player.rect.x + self.game.player.rect.width > self.rect.x:
                if self.game.player.rect.x + self.game.player.rect.width < self.rect.x + self.rect.width:
                    self.game.is_gameover = True

        """if self.game.player.rect.y + self.game.player.rect.height > self.rect.y:
            if self.game.player.rect.x + self.game.player.rect.width > self.rect.x:
                if self.game.player.rect.x > self.rect.x + self.rect.width:
                    self.game.is_gameover = True"""


