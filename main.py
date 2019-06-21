from game_class import Game
import sys
import time
import pygame




def main() :
    game = Game()
    size = game.size
    pygame.init()
    screen = pygame.display.set_mode(size)
    w_close = False

    #move_keys = [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]

    while not w_close :
        # --- обработка событий ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                w_close = True

        '''if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if not game.gameover :
                    x = int(pos[0] / game.cell_size)
                    y = int(pos[1] / game.cell_size)

                    game.cursor[0] = x
                    game.cursor[1] = y

                    if event.button == 1 : 
                        game.field.field[y][x].touch(1)
                    elif event.button == 3 : 
                        game.field.field[y][x].touch(0)

                    if game.field.field[y][x].face == 3 :
                        game.finish_game()
                    if (game.field.field[y][x].status == 0) & (game.field.field[y][x].face == 2) :
                        game.field.uncover_void(y, x)
                else :
                    pass'''

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_q : # quit
                w_close = True
            if event.key == pygame.K_r : # restart
                game.restart()

            if event.key == pygame.K_m :
                game.field.field[game.cursor[0]][game.cursor[1]].touch(0)
            if event.key == pygame.K_u :
                game.field.field[game.cursor[0]][game.cursor[1]].touch(2)

            if event.key == pygame.K_d :
                x = game.cursor[0]
                y = game.cursor[1]
                game.field.field[x][y].touch(1)
                if game.field.field[x][y].face == 3 :
                    game.finish_game()
                if (game.field.field[x][y].status == 0) & (game.field.field[x][y].face == 2) :
                    game.field.uncover_void(x, y)
            

        # --- игровая логика ---
        pos = pygame.mouse.get_pos()
        if not game.gameover :
            x = int(pos[0] / game.cell_size)
            y = int(pos[1] / game.cell_size)
            game.cursor[0] = x
            game.cursor[1] = y


        # --- отрисовка кртинки ---
        for i in range(game.lenX) :
            for j in range(game.lenY) :
                x = i * game.cell_size
                y = j * game.cell_size

                face = game.field.field[i][j].face
                img = None
                if face == 0 : img = game.img_free_cell
                if face == 1 : img = game.img_mark_cell
                if face == 2 : img = game.img_ba[game.field.field[i][j].status]
                if face == 3 : img = game.img_bomb
                    
                screen.blit(img, [x, y])
        screen.blit(game.img_cursor, [game.cursor[0]*game.cell_size, game.cursor[1]*game.cell_size])


        pygame.display.flip()
        pygame.time.wait(5)


    sys.exit()



main()