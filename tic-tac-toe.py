def intro():
    player_info = ["player_one", "player_two", "X", "O"]
    player_info[0] = input("player 1 please enter your name >>> ")
    player_info[1] = input("player 2 please enter your name >>> ")
    return player_info




def new_board():
    board = [7, 8, 9, 4, 5, 6, 1, 2, 3]
    return board


def display_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    return board


def player_input(name):
    piece = input(f"{name}, its your turn place your marker (X or O)")
    return piece


def placement():
    pass


def board_check():
    pass


def replay():
    pass
player_one, player_two = intro()
display_board(new_board())
