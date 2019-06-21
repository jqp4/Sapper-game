from field_class import Field
from pygame import image


class Game :

    def set_cursor(self) :
        pass



    def __init__(self) :
        self.lenX = 40
        self.lenY = 20
        self.ba = int(self.lenX * self.lenY / 5)
        self.field = Field(self.lenX, self.lenY, self.ba)
        self.field.generate()
        self.gameover = False
        self.cursor = [int(self.lenX/2), int(self.lenY/2)]

        '''self.img_free_cell = image.load('images/free.png')
        self.img_mark_cell = image.load('images/mark.png')
        self.img_bomb = image.load('images/-1.png')
        self.img_ba = [image.load('images/{}.png'.format(i)) for i in range(9)]
        
        self.cell_size = self.img_free_cell.get_rect()[3]
        self.size = self.lenX * self.cell_size,  self.lenY * self.cell_size'''

        self.img_free_cell = image.load('images_26x26/free.png')
        self.img_mark_cell = image.load('images_26x26/mark.png')
        self.img_bomb = image.load('images_26x26/bomb.png')
        self.img_ba = [image.load('images_26x26/{}.png'.format(i)) for i in range(9)]
        self.img_cursor = image.load('images_26x26/cursor.png')
        
        self.cell_size = self.img_free_cell.get_rect()[3]
        self.size = self.lenX * self.cell_size,  self.lenY * self.cell_size


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


    '''def move_cursor(self, key, move_keys) :
        if key == move_keys :
            self.cursor[1] += -1
        if key == pygame.K_DOWN :
            self.cursor[1] += 1
        if key == pygame.K_RIGHT :
            self.cursor[0] += 1
        if key == pygame.K_LEFT :
            self.cursor[0] += -1'''

















