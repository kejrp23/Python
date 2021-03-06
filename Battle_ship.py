"""
Created on Code Academy in python language project.
Created by Jason R. Pittman 
Created on 3/19/16
Code partially modified from orginal state.
"""



from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's Play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
"""
REMOVE THESE COMMENTS TO REVEAL
LOCATION OF SHIP FOR DEBUGGING
print ship_row
print ship_col
"""
#This is the main part of the game

for turn in range(4):
    print "turn", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

#This is the winning guess area of the game. 

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship you bum!"
        break
#These are the losing combinations

    else:       
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship Ha Ha !"
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print "Game Over"
    
        print_board(board)
