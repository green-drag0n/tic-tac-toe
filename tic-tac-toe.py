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


def player_input(name, marker, moves):
    while True:
        try:
            location = 69
            while location not in moves:
                location = int(input(f"{name}, its your turn place your marker {marker}, where would you like it?"))
            break
        except ValueError:
            print("Invalid VA")
    moves.remove(location)
    return location, moves


def placement(board, num, x):
    board[num-1] = x
    return board



def board_check(board, player_info):
    if board[0] == board[3] == board[6]:
        if board[0] == player_info[2]:
            print(f'{player_info[0]} you won')
        else:
            print(f'{player_info[1]} you won')
        return False
    elif board[1] == board[4] == board[7]:
        if board[1] == player_info[2]:
            print(f'{player_info[0]} you won')
        else:
            print(f'{player_info[1]} you won')
        return False
    elif board[2] == board[5] == board[8]:
        if board[2] == player_info[2]:
            print(f'{player_info[0]} you won')
        else:
            print(f'{player_info[1]} you won')
        return False
    elif board[0] == board[1] == board[2]:
        if board[0] == player_info[2]:
            print(f'{player_info[0]} you won')
        else:
            print(f'{player_info[1]} you won')
        return False
    elif board[3] == board[4] == board[5]:
        if board[3] == player_info[2]:
            print(f'{player_info[0]} you won')
        else:
            print(f'{player_info[1]} you won')
        return False
    elif board[6] == board[7] == board[8]:
        if board[6] == player_info[2]:
            print(f'{player_info[0]} you won')
        else:
            print(f'{player_info[1]} you won')
        return False
    elif board[0] == board[4] == board[8]:
        if board[0] == player_info[2]:
            print(f'{player_info[0]} you won')
        else:
            print(f'{player_info[1]} you won')
        return False
    elif board[2] == board[4] == board[6]:
        if board[2] == player_info[2]:
            print(f'{player_info[0]} you won')
        else:
            print(f'{player_info[1]} you won')
        return False
    else:
        return True


def replay():
    choice1 = ''
    while choice1 not in ["y","n"]:

        choice = input("would you like to play again? y/n? >>> ")
        choice1 = choice.lower()
    return choice == 'y'




def the_game():
    player_info = intro()
    board = new_board()
    moves = new_board()


    turn = True
    no_winner = True
    while no_winner:
        if turn:
            display_board(board)
            num, moves = player_input(player_info[0], player_info[2], moves)
            board = placement(board, num, "X")
            turn = False
        else:
            display_board(board)
            num, moves = player_input(player_info[1], player_info[3], moves)
            board = placement(board, num, "O")
            turn = True
        no_winner = board_check(board, player_info)
        if len(moves) == 0 and no_winner == True:
            print("Tie game")
            if replay():
                the_game()
    if replay():
        the_game()


if __name__ == '__main__':
    the_game()