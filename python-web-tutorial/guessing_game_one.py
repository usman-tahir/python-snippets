import random

number = random.randint(1, 9)
number_of_guesses = 0
current_guess = 0

while current_guess != number:
  current_guess = int(raw_input("Guess a number between 1 and 9: "))
  number_of_guesses += 1
  if current_guess == number:
    print("You got it (%s)! It took you %s guesses to guess correctly. " % (str(number), str(number_of_guesses)))
  else:
    if current_guess > number:
      print("Too high.")
    elif current_guess < number:
      print("Too low.")
