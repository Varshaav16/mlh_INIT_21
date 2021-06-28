# Basic Layout
# Board
# play_game
# display_board
# is_valid_move
# flip_turn 
# is_game_over -> is_win or is_tie

board = {position: "-" for position in range(1, 10)}

def is_valid_move(board, position):
    if position not in range(1, 10) or board[position] != "-":
        return False
    return True
    
def display_board(board):
    print()
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])


def play_game(board):
    display_board(board)
    game_is_still_going = True
    current_player = "X"

    while game_is_still_going:
        print("\nPlayer " + current_player + "\'s turn\n")
        handle_turn(board, current_player)
        display_board(board)

        if is_game_over(board, current_player):
            game_is_still_going = False
            print()

        current_player = flip_turn(current_player)

def handle_turn(board, current_player):
    position = int(input("Enter the grid number: ")) 
    if is_valid_move(board, position):
        board[position] = "X" if current_player == "X" else "O"
    else:
        print("INVALID MOVE! \nTry again ")
        handle_turn(board, current_player)



def is_game_over(board, current_player):
    game_over = [is_win(board, current_player), is_tie(board)]
    if game_over[0]:
        print("Game Over!! \nPlayer " + current_player + " won")

    elif game_over[1]:
        print("Tie!")
    return any(game_over)

def is_win(board, current_player):
    return check_rows(board, current_player) or check_columns(board, current_player) or check_diagonals(board, current_player)

def check_rows(board, current_player):
    for i in range(1, 10, 3):
        row = board[i] + board[i + 1] + board[i + 2] 
        if row == current_player * 3:
            return True
    return False

def check_columns(board, current_player):
    for i in range(1, 4):
        column = board[i] + board[i + 3] + board[i + 6] 
        if column == current_player * 3:
            return True
    return False

def check_diagonals(board, current_player):
    left_diagonal = board[1] + board[5] + board[9]
    right_diagonal = board[3] + board[5] + board[7]
  
    if current_player * 3  in [left_diagonal, right_diagonal]:
        return True

    return False


def is_tie(board):
    for i in range(1, 10, 3):
        if "-" in board[i] + board[i + 1] + board[i + 2]:
            return False
    return True


def flip_turn(current_player):
    return "O" if current_player == "X" else "X"

play_game(board)

