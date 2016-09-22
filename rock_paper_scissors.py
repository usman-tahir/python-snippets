import sys

def compare(move_one, move_two):
  moves = ["R", "P", "S"]
  if not (move_one in moves) or not (move_two in moves):
    return("You picked an invalid move.")
    sys.exit()
  elif move_one == move_two:
    return("It's a tie!")
  elif move_one == "R":
    if move_two == "S":
      return("Player one won the round!")
    else:
      return("Player two won the round!")
  elif move_one == "P":
    if move_two == "S":
      return("Player two won the round!")
    else:
      return("Player one won the round!")
  elif move_one == "S":
    if move_two == "P":
      return("Player one won the round!")
    else:
      return("Player two won the round!")


player_one = str(raw_input("Enter a name for player one: "))
player_two = str(raw_input("Enter a name for player two: "))

player_one_move = str(raw_input("Enter a move for %s (R, P, S): " % (player_one)))
player_two_move = str(raw_input("Enter a move for %s (R, P, S): " % (player_two)))
print(compare(player_one_move, player_two_move))