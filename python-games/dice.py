
import random

def roll_dice(highest_roll):
  return random.randint(1, highest_roll)

def return_rolls(highest_roll, number_of_rolls = 1):
  rolls = []
  for roll in range(number_of_rolls):
    rolls.append(roll_dice(highest_roll))
  return rolls

def main():
  highest_roll = int(input("How many sides should this die have? "))
  number_of_rolls = int(input("How many times should this die be rolled? "))
  rolls = return_rolls(highest_roll, number_of_rolls)
  print("The rolls you got were:\n%s" % (str(rolls)))

if __name__ == "__main__":
  main()