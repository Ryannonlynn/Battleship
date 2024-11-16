'''

This is our battleship game that will take input from user to play a simple game of battleship, between the user and the computer!
Enjoy

Kwabena
Ryannon Varin
CIS 121
 
'''

import random

def create_board(size):
    return [["O" for _ in range(size)] for _ in range(size)]

def print_board(board):
    for row in board:
        print(" ".join(row))

def place_ship(board):
    ship_row = random.randint(0, len(board) - 1)
    ship_col = random.randint(0, len(board[0]) - 1)
    return ship_row, ship_col

def get_guess():
    while True:
        try:
            guess_row = int(input("Guess Row (0-4): "))
            guess_col = int(input("Guess Col (0-4): "))
            if 0 <= guess_row < 5 and 0 <= guess_col < 5:
                return guess_row, guess_col
            else:
                print("Please enter a valid row and column (0-4).")
        

def main_game():
    size = 5
    board = create_board(size)
    ship_row, ship_col = place_ship(board)
    print("Welcome to Battleship!")
    print_board(board)

    for turn in range(5):
        print(f"Turn {turn + 1}")
        guess_row, guess_col = get_guess()

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
        else:
            if board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
            print_board(board)

        if turn == 4:
            print("Game Over! The battleship was at ({}, {}).".format(ship_row, ship_col))



