# Basic Layout
# Board
# play_game
# display_board
# is_valid_move
# flip_turn 
# is_game_over -> is_win or is_tie

board = {position: "-" for position in range(1, 10)}

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
    handle_turn(board, current_player)
    display_board(board)

    if is_game_over(board):
      game_is_still_going = False
      print("Game Over!!")

    flip_turn(current_player)

def handle_turn(board, current_player):
  position = int(input("Enter the grid number: "))
  board[position] = 'X'

def is_game_over(board):
  return is_win and is_tie

def is_win(board):
  return check_rows(board) and check_columns(board) and check_diagonals(board)

def check_rows(board, current_player):
  
  for i in range(1, 10, 3):
    row = board[i] + board[i + 1] + board[i + 2] 
    if row == current_player * 3:
      return True

  return False


def is_tie(board):
  return False

def flip_turn(current_player):
  return "O" if current_player == "X" else "X"

# play_game(board)
print(check_rows(board, "X"))