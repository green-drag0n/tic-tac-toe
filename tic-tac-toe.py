def intro():
    player_info = ["player_one", "player_two", "X", "O"]
    player_info[0] = input("player 1 please enter your name >>> ")
    player_info[1] = input("player 2 please enter your name >>> ")
    return player_info




def new_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def display_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    return board


def player_input(name, marker):
    location = int(input(f"{name}, its your turn place your marker {marker}, where would you like it?"))
    return location


def placement(board, num, x):
    board[num-1] = x
    return board



def board_check(board):
    print(board)


def replay():
    pass


player_info = intro()
board = new_board()


turn = True
no_winner = True
while no_winner:
    if turn:
        display_board(board)
        num = player_input(player_info[0], player_info[2])
        board = placement(board, num, "X")
        turn = False
    else:
        display_board(board)
        num = player_input(player_info[1], player_info[3])
        board = placement(board, num, "O")
        turn = True
    board_check(board)
replay()