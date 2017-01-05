
import argparse
import sys
import time
import itertools
import scrabble
import word

parser = argparse.ArgumentParser(
  description = 'Generate scrabble words from a rack'
)
parser.add_argument(
  'Scrabble word rack:',
  type = str,
  nargs = "+",
  help = "A word rack consisting of 7 letters (ex: 'ZAEFIEE')"
)

def validate_rack(rack):
  elements = list(rack)
  if not all(isinstance(letter, str) for letter in rack):
    return False
  if len(elements) != 7:
    return False
  return True

def generate_words(rack):
  timeout = time.time() + 15
  scrabble_words = scrabble.Scrabble("./words.txt")
  valid = []
  for i in range(2, len(rack) + 1):
    words = itertools.permutations(rack, i)
    for word in list(words):
      current_word = "".join(word)
      if current_word in scrabble_words.words:
        valid.append(current_word)
      else:
        if time.time() > timeout:
          break
  return list(set(valid))

def score_words(words):
  result = ""
  scrabble_words = scrabble.Scrabble("./words.txt")
  scored = []
  for w in words:
    scored.append(word.Word(w, scrabble_words.score_word(w)))
  scored.sort(key = lambda x: x.score, reverse = False)

  for each in scored:
    result += str(each)
  return result


def main():
  current_rack = sys.argv[-1]
  print("Current rack: " + str(current_rack))
  if (validate_rack(current_rack)):
    generated_words = generate_words(current_rack)
    print("Words found: " + str(len(generated_words)))
    print(score_words(generated_words))
  else:
    print("Please enter a valid, 7 element rack.")

if __name__ == "__main__":
  main()
