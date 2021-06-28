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
  current_player = 0

  while game_is_still_going:
    handle_turn(board, current_player)
    display_board(board)

    if is_game_over(board):
      game_is_still_going = False
      print("Game Over!!")

   

def handle_turn(board, current_player):
  position = int(input("Enter the grid number: "))
  board[position] = 'X'

def is_game_over(board):
  return is_win and is_tie

def is_win(board):
  return True

def is_tie(board):
  return False

play_game(board)