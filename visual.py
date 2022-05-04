from tkinter import *
import minimax_alg, random
SIZE = 300

COLORS = {
    '0' : "#fff",
    '1' : "#f00",
    '2' : "#00f"
}

def randomInitMove():
    state = list("200000000")
    random.shuffle(state)
    return ''.join(state)

class Board(Tk):
    def __init__(self,state,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("%sx%s"%(SIZE,SIZE))
        self['bg'] = '#000'
        self.resizable(0,0)
        self.title("TIC-TAC-TOE")
        self.bind_all("<space>",self.reset)
        self.bind_all("<q>",lambda e : self.quit())
        self.size = SIZE
        self.padding = 2
        self.t_size = int(SIZE/3)-self.padding*2
        self.state = state
        self.tiles = []
        self.validTime = True

        self.createBoard()
        self.update()


    def reset(self,event):
        print("___NEW _GAME___")
        self.state = randomInitMove()
        if random.random() > 0:
            self.state = "000000000"
        self.validTime = True
        self.update()

    def createBoard(self):
        i = 0
        for row in range(3):
            for col in range(3):
                t = Tile(i,self,width=self.t_size,height=self.t_size)
                t.grid(column=col,row=row,pady=self.padding,padx=self.padding)
                self.tiles.append(t)
                i+= 1

    def update(self):
        for tile in self.tiles:
            tile.update()

    def handleUserMove(self,id):
        self.validTime = False
        self.state = ''.join(["1" if id == i else self.state[i] for i in range(9)])
        self.botMove()

    def botMove(self):
        resp = minimax_alg.minimax(minimax_alg.GameState(self.state,2),True)
        self.state = resp.init_parent.state
        self.update()
        if minimax_alg.gameOver(resp.init_parent.state):
            self.validTime = False
            return
        self.validTime = True

class Tile(Frame):
    def __init__(self,i,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.index = i
        self.bind("<Button-1>",self._handle)

    def update(self):
        self['bg'] = COLORS[str(self.master.state[self.index])]

    def _handle(self,event):
        if not self.master.validTime: return
        if self.master.state[self.index] != minimax_alg.EMPTY: return
        self.master.handleUserMove(self.index)
        self.update()

if "__main__" in __name__:
    app = Board(randomInitMove());
    app.mainloop()
