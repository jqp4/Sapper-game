from field_class import Field
import pygame


class Hot_Keys :

    def __init__(self) :
        #for i in range(97, 123) : print('\'{0}\' : pygame.K_{0},'.format(chr(i)))
        self.pygame_keys = {    'a' : pygame.K_a,
                                'b' : pygame.K_b,
                                'c' : pygame.K_c,
                                'd' : pygame.K_d,
                                'e' : pygame.K_e,
                                'f' : pygame.K_f,
                                'g' : pygame.K_g,
                                'h' : pygame.K_h,
                                'i' : pygame.K_i,
                                'j' : pygame.K_j,
                                'k' : pygame.K_k,
                                'l' : pygame.K_l,
                                'm' : pygame.K_m,
                                'n' : pygame.K_n,
                                'o' : pygame.K_o,
                                'p' : pygame.K_p,
                                'q' : pygame.K_q,
                                'r' : pygame.K_r,
                                's' : pygame.K_s,
                                't' : pygame.K_t,
                                'u' : pygame.K_u,
                                'v' : pygame.K_v,
                                'w' : pygame.K_w,
                                'x' : pygame.K_x,
                                'y' : pygame.K_y,
                                'z' : pygame.K_z    }


    def set(self, args) :
        new_keys = [self.pygame_keys[args[i]] for i in range(6)]

        self.quit = new_keys[0]
        self.new_game = new_keys[1]
        self.open_all_cells = new_keys[2]
        self.mark = new_keys[3]
        self.unmark = new_keys[4]
        self.dig_out = new_keys[5]



class Game :

    def upload_settings(self, filename) :
        with open(filename) as f:
            read_data = f.read() + '\n'
            
        done = False
        values = []
        while not done :
            if len(read_data) == 0 :
                done = True
            else :
                s = read_data[:read_data.find('\n')]
                if s.find('[') != -1 :
                    try :
                        values.append(s[s.find('[') + 1:s.find(']')])
                    except : 
                        values.append(None)
                read_data = read_data[read_data.find('\n') + 2:]
            
        return values


    def upload_images(self) :
        self.img_free_cell = pygame.image.load('images_26x26/free.png')
        self.img_mark_cell = pygame.image.load('images_26x26/mark.png')
        self.img_bomb = pygame.image.load('images_26x26/bomb.png')
        self.img_ba = [pygame.image.load('images_26x26/{}.png'.format(i)) for i in range(9)]
        self.img_cursor = pygame.image.load('images_26x26/cursor.png')

        self.cell_size = self.img_free_cell.get_rect()[3]
        self.size = self.lenX * self.cell_size,  self.lenY * self.cell_size



    def __init__(self) :
        self.lenX = 40
        self.lenY = 20
        self.ba = int(self.lenX * self.lenY / 7)
        self.field = Field(self.lenX, self.lenY, self.ba)
        self.field.generate()
        self.gameover = False
        self.cursor = [int(self.lenX/2), int(self.lenY/2)]
        self.keys = Hot_Keys()
        self.keys.set(self.upload_settings(filename='settings.mss'))
        self.upload_images()


    def finish_game(self) :
        self.gameover = True
        print('    G A M E      O V E R  ')
        for i in range(len(self.field.field)) :
            for j in range(len(self.field.field[0])) :
                if self.field.field[i][j].status == -1 :
                    self.field.field[i][j].face = 3
                    

    def restart(self) :
        self.gameover = False
        print('     N E W       G A M E  ')
        self.field = Field(self.lenX, self.lenY, self.ba)
        self.field.generate()
        self.cursor = [int(self.lenX/2), int(self.lenY/2)]


    def open_all(self) :
        self.cursor = [-1, -1]
        self.field.open_all()
        self.gameover = True


    













