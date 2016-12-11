
import random

def choose_word():
  file_opened = open("./words.txt")
  words = file_opened.readlines()

  index = random.randint(0, len(words))
  return words[index]

def evaluate_letter_guess(letter, word):
  if letter == "" or len(letter) > 1:
    print("Please guess only one, non-blank letter.")
    return False
  else:
    return letter.lower() in word.lower()

def fill_in_letter(current_guesses, word, guess):
  letters = list(word)
  if evaluate_letter_guess(guess, word):
    if guess in current_guesses:
      print("You already guessed the letter '%s'." % (guess))
    else:
      print("Correct! There are %d %s's in this word." % (letters.count(guess), guess))
      for letter in range(len(letters)):
        if letters[letter] == guess:
          current_guesses[letter] = letters[letter]
  else:
    print("'%s' is not in this word." % (guess))
  return current_guesses

def current_guesses_status(current_guesses):
  output = "\n"
  for current_guess in current_guesses:
    if current_guess != " _ ":
      output += " " + current_guess.upper() + " "
    else:
      output += current_guess
  return output


def main():
  word = choose_word().rstrip("\n")

  incorrect = []
  current_guesses = [" _ "] * len(word)
  guesses = 0

  while " _ " in current_guesses:
    guesses += 1
    guess = input("\nGuess a letter: ")
    if evaluate_letter_guess(guess, word):
      fill_in_letter(current_guesses, word, guess)
      print(current_guesses_status(current_guesses))
    else:
      if not guess in incorrect and len(guess) == 1:
        incorrect.append(guess.lower())
        print("\nCurrent incorrect guesses: " + str(incorrect))
      else:
        if guess != "" and len(guess) == 1:
          print("You have already guessed '%s' incorrectly." % (guess))
  print ("\nYou guessed the word in %d tries." % (guesses))
      

if __name__ == "__main__":
  main()