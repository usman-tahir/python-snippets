import random
import sys


def cows_and_bulls_printout(actual, guess):
  if actual < 1000:
    string_actual = ("0" + str(actual))
  else:
    string_actual = str(actual)

  if guess < 1000:
    string_guess = ("0" + str(guess))
  else:
    string_guess = str(guess)
    
  cows_and_bulls = [0, 0]

  for x in range(len(string_actual)):
    if string_actual[x] == string_guess[x]:
      cows_and_bulls[0] += 1
    elif string_actual[x] != string_guess[x]:
      cows_and_bulls[1] += 1
  
  if cows_and_bulls[0] == 4:
    print("\nYou guessed the number! It was: %s" % (string_actual))
    return(False)
  else:
    print("You have %s cows and %s bulls." % (str(cows_and_bulls[0]), str(cows_and_bulls[1])))
    return(True)

# The number must be 4 digits, so it needs to be between 1000 and 9999
generated = random.randint(1000, 10000)
# print(str(generated))
flag = True
guesses = 0

while flag == True:
  guess = int(raw_input("Please enter your 4 digit guess: "))
  guesses += 1
  flag = cows_and_bulls_printout(generated, guess)
print("It took you %s guess(es) to figure out the number." % (str(guesses)))