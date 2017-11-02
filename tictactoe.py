import random

def checkWin(board,sym):
    win = 0
    while(win == 0):
        if(board[0]==board[1]==board[2]==sym):
            win = 1
            break
        if(board[3]==board[4]==board[5]==sym):
            win = 1
            break
        if(board[6]==board[7]==board[8]==sym):
            win = 1
            break
        if(board[0]==board[3]==board[6]==sym):
            win = 1
            break
        if(board[1]==board[4]==board[7]==sym):
            win = 1
            break
        if(board[2]==board[5]==board[8]==sym):
            win = 1
            break
        if(board[0]==board[4]==board[8]==sym):
            win = 1
            break
        if(board[2]==board[4]==board[6]==sym):
            win = 1
            break
        break
    return win

def clearboard(board):
    for x in range(9):
        board[x] = '_'
    return board

def printnewboard():
    for x in range(9):
        if(x%3==0):
            print("")
        print(x+1, end=" ")
    print("")
        
    
print("Welcome to Tic Tac Toe")
newboard = ['_' for x in range(9)]
board = newboard
printnewboard()

print("")
tiles = 0
remtiles = [0,1,2,3,4,5,6,7,8]
while(1):
    win = 0
    print("")
    mark = int(input("Please input position (1-9): "))-1
    if(mark not in range(9) or board[mark]!='_'):
        print("invalid input")
    else:
        
        board[mark] = 'X'
        tiles = tiles + 1
        remtiles.remove(mark)
        
        for x in range(len(board)):
            if(x%3==0):
                print("")
            print(board[x], end=" ")
            
        if(checkWin(board,'X')):
            print("")
            print("Congrats you have won!")
            tiles = 0
            board = clearboard(board)
            printnewboard()
            remtiles = [0,1,2,3,4,5,6,7,8]
            
        if(tiles<9):
            opchoice = random.choice(remtiles)
            board[opchoice] ='O'
            remtiles.remove(opchoice)
            tiles = tiles + 1
        
        print(remtiles)
        for x in range(len(board)):
            if(x%3==0):
                print("")
            print(board[x], end=" ")
            
        if(checkWin(board,'O')):
            print("")
            print("You lost!!")
            tiles = 0
            board = clearboard(board)
            printnewboard()
            remtiles = [0,1,2,3,4,5,6,7,8]   

            
        if(tiles==9):
            print("Draw!")
            tiles = 0
            board = clearboard(board)
            printnewboard()
            remtiles = [0,1,2,3,4,5,6,7,8]

