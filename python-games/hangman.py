
import random

def choose_word():
  file_opened = open("./words.txt")
  words = file_opened.readlines()

  index = random.randint(0, len(words))
  return words[index]

def evaluate_letter_guess(letter, word, valid_letters):
  if letter not in valid_letters:
    print("Please guess only one, non-blank letter.")
    return False
  else:
    return letter.lower() in word.lower()

def fill_in_letter(current_guesses, word, guess, valid_letters):
  letters = list(word)
  if evaluate_letter_guess(guess, word, valid_letters):
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
  valid_letters = [chr(c) for c in range(ord("a"), ord("z") + 1)]
  incorrect = []
  current_guesses = [" _ "] * len(word)
  guesses = 0

  while " _ " in current_guesses:
    guesses += 1
    guess = input("\nGuess a letter: ")
    if evaluate_letter_guess(guess, word, valid_letters):
      fill_in_letter(current_guesses, word, guess, valid_letters)
      print(current_guesses_status(current_guesses))
    else:
      if not guess in incorrect and guess in valid_letters:
        incorrect.append(guess.lower())
        print("\nCurrent incorrect guesses: " + str(incorrect))
      else:
        if guess in valid_letters:
          print("You have already guessed '%s' incorrectly." % (guess))
        else:
          print("You guessed an incorrect character.")
  print ("\nYou guessed the word in %d tries." % (guesses))
      

if __name__ == "__main__":
  main()