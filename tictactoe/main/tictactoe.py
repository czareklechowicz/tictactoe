import os
from time import sleep

 
X = 'X'
O = 'O'
WINNER = None
PLAY_ON = True
X_O = str()
PLAYER_NAME = str()
FIRST_PLAYER = str()
FIG = str()

 
board = [' ' for _ in range(9)]
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print('')

 

def print_board_nums():
    print('Please find below the numbers you can choose:\n')

    rows = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]
    for row in rows:
        print('| ' + ' | '.join(row) + ' |')
    print('\n\n')

 

def clear_console():
    clear = lambda: os.system('clear')
    clear()

 

def separator():
    print("--------------------------------")

 

def introduction():
    print('Hello, this is the Tic Tac Toe game.\nPlease choose who will be the first player:'
    ' you or your opponent?\n')

 

def whats_your_name():
    player_1 = input('Hello PLAYER 1. What is your name? ')
    player_2 = input('Hello PLAYER 2. What is your name? ')
    return player_1, player_2

 

def print_number(PLAYER_NAME, X_O):
    separator()
    print(f"{PLAYER_NAME} ({X_O}): - it is your turn:")
    separator()
    position = input('\nChoose a possition [1-9]: ')
    return position

 

def choose_player(p1, p2):
    answers = ["Y","N"]
    answer = str()

    while answer not in answers:
        clear_console()
        print('Thank you for typing the names...')
        sleep(3)
        clear_console()

        answer = input(f'{p1} do you want to begin the game? (y/n). Type "n" if {p2} should be the first player: ')
        answer =  answer.upper()


        if answer in answers:
            if answer == "Y":
                FIG = 'X'
                FIRST_PLAYER = p1
                print(f'Okey then, {p1} will begin the game\n')
                sleep(2)
            else:
                FIG = 'O'
                FIRST_PLAYER = p2
                print(f'Okey then, {p2} will be the first player\n')
                sleep(2)
        else:
            print(f'Please choose correct character. "{answer}" is not valid\n')
    return FIG, FIRST_PLAYER 

 

def check_winner():

    rows = check_rows()
    cols = check_columns()
    diags = check_diagonals()
    tie = check_tie()

 

    if rows == None:
        if cols == None:
            if diags == None:
                if tie == None:
                    return None
                else:
                    won = tie
            else:
                won = diags
        else:
            won = cols
    else:
        won = rows

 

    return won 

 

def check_columns():
    global PLAY_ON    

    col1 = board[0] == board[3] == board[6] != " "
    col2 = board[1] == board[4] == board[7] != " "
    col3 = board[2] == board[5] == board[8] != " "

 

    if col1 or col2 or col3:
        PLAY_ON = False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    else:
        return None

 

def check_diagonals():
    global PLAY_ON

    dia1 = board[0] == board[4] == board[8] != " "
    dia2 = board[2] == board[4] == board[6] != " "

    if dia1 or dia2:
        PLAY_ON = False
    if dia1:
        return board[0]
    elif dia2:
        return board[2]
    else:
        return None

 

def check_rows():
    global PLAY_ON

    row1 = board[0] == board[1] == board[2] != " "
    row2 = board[3] == board[4] == board[5] != " "
    row3 = board[6] == board[7] == board[8] != " "

 

    if row1 or row2 or row3:
        PLAY_ON = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None

 

def check_tie():
    global PLAY_ON  

    a = 0


    for row in range(9):
        if board[row] == " ":
            a += 1
        else:
            a = a
    if a == 0:
        PLAY_ON = False
        return True
    else:
        return None

 

def flip_player(fig, p_name, p1, p2):
    if fig == 'X':
        fig = 'O'
    else:
        fig = 'X'

    if p_name == p1:
        p_name = p2
    else:
        p_name = p1
    return fig, p_name

 

def tic_tac_toe_game():
    clear_console()
    introduction()
    player_1, player_2 = whats_your_name()
    FIG, FIRST_PLAYER = choose_player(player_1, player_2)

    X_O = "X" if FIG == "X" else "O"
    PLAYER_NAME = player_1 if FIRST_PLAYER == player_1 else player_2

    clear_console()
    print_board_nums()


    while PLAY_ON:
        position = print_number(PLAYER_NAME, X_O)

        valid = False


        while not valid:
            while position not in ['1','2','3','4','5','6','7','8','9']:
                position = print_number(PLAYER_NAME, X_O)

            pos = int(position) - 1
            if board[pos] == " ":
                valid = True
            else:
                separator()
                print("You can't go there. Go again.")
                separator()
                sleep(2)
                position = print_number(PLAYER_NAME, X_O)    

        position = int(position) - 1
        print(f'\nCurrent Board: {board[position]}')
        board[position] = X_O
        clear_console()
        print_board_nums()
        print_board()
        winner  = check_winner()
        X_O, PLAYER_NAME = flip_player(X_O, PLAYER_NAME, player_1, player_2)

 

    if winner == "X" or winner == "O":
        print(f"The winner is: {FIRST_PLAYER} ('{winner}')\n")
    elif winner == True:
        print("Tie\n")