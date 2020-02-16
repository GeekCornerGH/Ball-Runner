import pygame
pygame.init()

from game import Game



screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Ball Runner")

game_icon = pygame.image.load("assets/icon.png").convert_alpha()
pygame.display.set_icon(game_icon)

loop_main = True
loop_menu = True
loop_game = False

image_bg = pygame.image.load("assets/bg.jpg").convert()
image_logo = pygame.image.load("assets/logo.png").convert_alpha()
image_button = pygame.image.load("assets/Play Button/normal.png").convert_alpha()

game = Game(1) #Sets the difficulty to 1 (Normal)

rect_button = image_button.get_rect()
rect_button.x = 200
rect_button.y = 250
is_button_touch = False


while loop_main:
    while loop_menu:
        screen.blit(image_bg, (0, 0))

        screen.blit(image_logo, (150, 50))
        screen.blit(image_button, rect_button)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop_menu = False
                loop_main = False
                pygame.quit()

            elif event.type == pygame.MOUSEMOTION:
                if event.pos[0] > rect_button.x and event.pos[0] < rect_button.x + rect_button.width:
                    if event.pos[1] > rect_button.y and event.pos[1] < rect_button.y + rect_button.height:
                        image_button = pygame.image.load("assets/Play Button/hover.png").convert_alpha()
                        is_button_touch = True
                else:
                    is_button_touch = False
                    image_button = pygame.image.load("assets/Play Button/normal.png").convert_alpha()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                if is_button_touch == True:
                    loop_menu = False
                    loop_game = True

                    game.player.rect.y = 505
                    game.is_gameover = False



        game.clock.tick(game.framerate)
        pygame.display.flip()


    while loop_game:
        screen.blit(image_bg, (0, 0))

        #Walls group
        for wall in game.walls:
            wall.go_left()
        game.walls.draw(screen)

        game.try_gererate_wall()



        #Player instance
        screen.blit(game.player.image, game.player.rect)
        game.player.move()




        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                loop_game = False
                loop_main = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game.player.is_jumping = True

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                for wall in game.walls:
                    wall.remove()

                loop_game = False
                loop_menu = True

        if game.player.is_jumping:

            if game.player.jump_count >= -12:
                game.player.rect.y -= (game.player.jump_count * abs(game.player.jump_count)) * 0.5
                game.player.jump_count -= 1
            else:
                game.player.jump_count = 12
                game.player.rect.y = 505
                game.player.is_jumping = False

        if game.is_gameover:
            for wall in game.walls:
                wall.remove()

            loop_game = False
            loop_menu = True

        game.clock.tick(game.framerate)
        pygame.display.flip()

