# tic tac toe game

# ---------------------------Global Variables---------------------------

# game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# if game is playing
game_is_going = True

# who won or tied?
winner = None

# whose turn
current_player = "X"


# ------------===-------------Function----------------------------------
# display board
def display_board():

    print("\n")
    print(board[0] + "|" + board[1] + "|" + board[2] + "    1 | 2 | 3")
    print(board[3] + "|" + board[4] + "|" + board[5] + "    4 | 5 | 6")
    print(board[6] + "|" + board[7] + "|" + board[8] + "    7 | 8 | 9")
    print("\n")


# play game
def play_game():

    # displays initial board
    display_board()

    # loops until game ends
    while game_is_going:

        # handles turns
        handle_turn(current_player)

        # checks if game is done
        check_game_over()

        # changes players
        flip_player()

    # game over
    if winner == "X" or winner == "O":
        print(winner + " won!!")
    elif winner is None:
        print("it is a Tie")


# handles turns
def handle_turn(player):

    # get position from player
    print(player + "'s turn ")
    position = input("Choose a place from 1 to 9: ")

    # makes sure user input is valid and if the spot is open
    valid = False
    while not valid:
        # make sure input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a place from 1 to 9: ")

        # get proper placement
        position = int(position) - 1

        # make sure spot is open
        if board[position] == "-":
            valid = True
        else:
            print("ALERT you cant go there!!!")

    # put piece on board
    board[position] = player
    # displays board
    display_board()


def check_game_over():
    check_win()
    check_tie()


def check_win():
    # sets global variables
    global winner
    # check if there was a winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    # set global variable
    global game_is_going
    # check rows fi they are the same value
    row_one = board[0] == board[1] == board[2] != "-"
    row_two = board[3] == board[4] == board[5] != "-"
    row_three = board[6] == board[7] == board[8] != "-"
    # shows if any rows have a match
    if row_one or row_two or row_three:
        game_is_going = False
    # return row winner
    if row_one:
        return board[0]
    elif row_two:
        return board[3]
    elif row_three:
        return board[6]
    else:
        return None


def check_columns():
    # set global variable
    global game_is_going
    # check rows fi they are the same value
    column_one = board[0] == board[3] == board[6] != "-"
    column_two = board[1] == board[4] == board[7] != "-"
    column_three = board[2] == board[5] == board[8] != "-"
    # shows if any rows have a match
    if column_one or column_two or column_three:
        game_is_going = False
    # return row winner
    if column_one:
        return board[0]
    elif column_two:
        return board[1]
    elif column_three:
        return board[2]
    else:
        return None


def check_diagonals():
    # set global variable
    global game_is_going
    # check rows if they are the same value
    diagonal_one = board[0] == board[4] == board[8] != "-"
    diagonal_two = board[2] == board[4] == board[6] != "-"
    # shows if any rows have a match
    if diagonal_one or diagonal_two:
        game_is_going = False
    # return row winner
    if diagonal_one:
        return board[0]
    elif diagonal_two:
        return board[2]
    else:
        return None


def check_tie():
    # set global variable
    global game_is_going
    # if board is full
    if "-" not in board:
        game_is_going = False
        return True
    else:
        return False


def flip_player():

    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"
    return


# --------------------------Start program---------------------------------
# plays tic tac toe game
play_game()


