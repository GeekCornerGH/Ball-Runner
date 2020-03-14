import pygame
pygame.init()

from game import Game
from buttons import Button
from menu import Skins_Choice

font = pygame.font.SysFont("AcmeFont", 24, bold=True)

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Ball Runner")

game_icon = pygame.image.load("assets/icon.png").convert_alpha()
pygame.display.set_icon(game_icon)

loop_main = True
loop_menu = True
loop_game = False

ball_choice = False

image_bg = pygame.image.load("assets/bg.jpg").convert()
image_logo = pygame.image.load("assets/logo.png").convert_alpha()

button_play = Button("assets/buttons/play_normal.png", "assets/buttons/play_hover.png", 200, 250)
button_skinchoice = Button("assets/buttons/ball_normal.png", "assets/buttons/ball_hover.png", 550, 270)

game = Game(1) #Sets the difficulty to 1 (Normal)
game.load()


text_static_score = font.render("Score :", True, (0, 0, 0))





while loop_main:


    while loop_menu:


        screen.blit(image_bg, (0, 0))

        screen.blit(image_logo, (150, 50))
        screen.blit(button_play.image, button_play.rect)
        screen.blit(button_skinchoice.image, button_skinchoice.rect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop_menu = False
                loop_main = False
                game.save()

                pygame.quit()

            elif event.type == pygame.MOUSEMOTION:
                if button_play.check_hover(event.pos) == True:
                    button_play.a_hover()
                else:
                    button_play.a_normal()

                if button_skinchoice.check_hover(event.pos) == True:
                    button_skinchoice.a_hover()

                else:
                    button_skinchoice.a_normal()


            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                if button_play.click() == True:
                    loop_menu = False
                    loop_game = True

                    game.player.update(game.choosed_skin)

                    game.player.rect.y = 505
                    game.is_gameover = False

                if button_skinchoice.click() == True:
                    loop_menu = False
                    menu_ball_choice = Skins_Choice(game)
                    ball_choice = True




        game.clock.tick(game.framerate)
        pygame.display.flip()

    while ball_choice:

        menu_ball_choice.demo.rotate()

        screen.blit(image_bg, (0,0))
        screen.blit(menu_ball_choice.background, (0,0))
        screen.blit(menu_ball_choice.demo.image, menu_ball_choice.demo.rect)
        screen.blit(menu_ball_choice.quit.image, menu_ball_choice.quit.rect)


        menu_ball_choice.skins.draw(screen)




        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                ball_choice = False
                loop_main = False
                game.save()
                pygame.quit()

            elif event.type == pygame.MOUSEMOTION:
                if menu_ball_choice.quit.check_hover(event.pos) == True:
                    menu_ball_choice.quit.a_hover()
                else:
                    menu_ball_choice.quit.a_normal()

                for obj in menu_ball_choice.skins:
                    if obj.check_hover(event.pos) == True:
                        obj.a_hover()
                    else:
                        obj.a_normal()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                for obj in menu_ball_choice.skins:
                    if obj.is_touch:
                        game.choosed_skin = game.total_skins[obj.name]
                        menu_ball_choice.demo.change(obj.path)

                if menu_ball_choice.quit.is_touch == True:
                    ball_choice = False
                    loop_menu = True
                    del menu_ball_choice



        game.clock.tick(game.framerate)
        pygame.display.flip()

    while loop_game:

    

        text_changing_score = font.render(str(game.score), True, (0, 0, 0))


        screen.blit(image_bg, (0, 0))
        screen.blit(text_static_score, (5, 5))
        screen.blit(text_changing_score, (70, 5))

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
                game.save()

                pygame.quit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game.player.is_jumping = True

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                for wall in game.walls:
                    wall.remove()

                game.score = 0
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

            game.save()

            for wall in game.walls:
                wall.remove()

            game.score = 0
            loop_game = False
            loop_menu = True

        game.clock.tick(game.framerate)
        try:
            pygame.display.flip()

        except:
            print("L'affichage n'a pas pu être mis à jour")

