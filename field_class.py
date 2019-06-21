from random import randint




class Cell :

    def __init__(self, inp_status) :
        #status = -1  -  bomb
        #status = 0-9  -  bomb amount around
        self.status = inp_status
        self.face = 0
        #face = 0 - not marked
        #face = 1 - checkbox
        #face = 2 - number of bombs
        #face = 3 - bomb!


    def touch(self, touch_type) :
        if touch_type == 0 :    # mark
            if self.face == 0 :
                self.face = 1

        elif touch_type == 1 :    #dig out
            if self.face != 1 :
                if self.status >= 0 :
                    self.face = 2
                elif self.status == -1 :
                    self.face = 3

        elif touch_type == 2 :    # unmark
            if self.face == 1 :
                self.face = 0








class Field :

    def __init__(self, inp_width, inp_height, inp_bombs_amount) :
        self.lenX = inp_width
        self.lenY = inp_height
        self.bombs_amount = inp_bombs_amount
        self.field = [[Cell(0) for j in range(self.lenY)] for i in range(self.lenX)]  # строчка столбцов


    def generate(self) :
        for i in range(self.bombs_amount) :
            self.field[randint(0, self.lenX - 1)][randint(0, self.lenY - 1)].status = -1

        for i in range(self.lenX) :
            for j in range(self.lenY) :
                if self.field[i][j].status == 0 :
                    nba = 0   # number od bombs around
                    for di in [-1, 0, 1] :
                        for dj in [-1, 0, 1] :
                            try :
                                if self.field[i + di][j + dj].status == -1 :
                                    nba += 1
                            except : pass
                    self.field[i][j].status = nba


    def uncover_void(self, x, y) :
        #print('sfdf')
        for dx in [-1, 0, 1] :
            for dy in [-1, 0, 1] :
                if not (dx == dy == 0) :
                    try :
                        if self.field[x + dx][y + dy].satus == 0 :
                            self.field[x + dx][y + dy].face = 2
                            self.uncover_void(x + dx, y + dy)
                    except : pass


    def open_all(self) :
        for i in range(self.lenX) :
            for j in range(self.lenY) :
                if self.field[i][j].status == -1 :
                    self.field[i][j].face = 3
                else :
                    self.field[i][j].face = 2



