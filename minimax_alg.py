import time
EMPTY = "0"
winningStates = [
 '012','345','678','036','147','258','048','246'
]

tile = {
    "0" : ".",
    "1" : "o",
    "2" : "x"
}

def nextTurn(turn):
    return (turn%2) + 1

def isWinner(state,player):
	for template in winningStates:
		valid = True
		for position in template:
			if state[int(position)] != str(player):
				valid = False
				break
		if valid: return True
	return False

def tieGame(state):
    return (EMPTY not in state)

def gameOver(state):
    return tieGame(state) or isWinner(state,1) or isWinner(state,2)

def score(board,player):
    try:
        state = board.state
    except:
        return board
    if isWinner(state,nextTurn(player)):
        return -1
    if tieGame(state):
        return 0
    if isWinner(state,player):
        return 1

class Node():
    def __init__(self,state):
        self.state = state
        self.init_parent = None

class GameState(Node):
    def __init__(self,state,turn):
        super().__init__(state)
        self.turn = turn

    def generateMoves(self):
        if gameOver(self.state):
            return None
        for i in range(9):
            if self.state[i] != EMPTY:
                continue
            temp = list(self.state)
            temp[i] = str(self.turn)
            new_state = GameState(''.join(temp),nextTurn(self.turn))
            if self.init_parent == None:
                new_state.init_parent = new_state
            else:
                new_state.init_parent = self.init_parent
            yield new_state

    def print(self):
        temp = list(self.state)
        for i in range(0,9,4):
            temp.insert(i,"\n")
        print(''.join([tile[val] if val != '\n' else '\n' for val in temp]))


def minimax(start,maximizingPlayer):
    if gameOver(start.state):
        return start

    if maximizingPlayer:
        Eval = float('-inf')
        for child in start.generateMoves():
            val = minimax(child,False)
            Eval = max(Eval,val,key = lambda x : score(x,2))
    else:
        Eval = float('-inf')
        for child in start.generateMoves():
            val = minimax(child,True)
            Eval = max(Eval,val,key = lambda x : score(x,1))
    return Eval


# original: 14.14 seconds
# 13.9 -> reducing list iterations for generating moves
# 7.1 -> winning state algorithm


if "__main__" in __name__:
    start = time.time()
    init = GameState("000000000",2)
    resp = minimax(init,True)
    end = time.time()
    print('time: %s'%(end-start))
    print('endgame')
    resp.print()
    print('move')
    resp.init_parent.print()
