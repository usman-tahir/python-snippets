
import random

def generate_random_number(upper, lower):
  return random.randint(upper, lower)

def evaluate_guess(actual, guess):
  if (actual == guess):
    print("You guessed it! The number was: %d" % (actual))
    return True
  elif actual < guess:
    print("Your guess was too high.")
    return False
  else:
    print("Your guess was too low.")
    return False

def main():
  actual = generate_random_number(1, 100)
  guesses = 0
  correct = False

  while correct == False:
    guesses += 1
    guess = int(input("Guess a number between 1 and 100, inclusive: "))
    correct = evaluate_guess(actual, guess)
  print("You guessed the number in %d tries." % (guesses))

if __name__ == "__main__":
  main()