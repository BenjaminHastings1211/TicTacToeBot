 from minimax import *

resp = GameState("000020000",2)
resp.print()
spot = 9
while not gameOver(resp.state):
    print("-----")

    while (not (0 <= spot <= 8)) or (resp.state[spot] != EMPTY):
        spot = int(input("Pick a valid spot: "))
    temp = list(resp.state)
    temp[spot] = "1"
    newS = GameState(''.join(temp),2)
    winSolution = minimax(newS,10,True);
    winSolution.print()
    resp = winSolution.init_parent
    resp.print()
resp.init_parent.print()
