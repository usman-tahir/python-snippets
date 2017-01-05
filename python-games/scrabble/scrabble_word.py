
import argparse
import sys
import itertools
import scrabble

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
    print(elements)
    if not all(isinstance(letter, str) for letter in rack):
        return False

    if len(elements) != 7:
        return False
    return True

def generate_word(rack, letter, min_length, max_length):
    words = []
    for i in range(min_length, max_length):
        for j in itertools.product(rack, repeat = i):
            if j[0].startswith(letter):
                words.append("".join(j))
    print(len(words))
    return words

def create_words(rack):
    s = scrabble.Scrabble("./words.txt")
    validated_words = []

    for x in range(len(rack)):
        generated_words = generate_word(rack, rack[x], 1, 7)
        for y in generated_words:
            if y in s.words:
                validated_words.append(y)
    return validated_words

def main():
    if validate_rack(sys.argv[-1]):
        print(sys.argv[-1])
        validated_words = create_words(sys.argv[-1])
    else:
        print("Please enter a valid, 7 element rack.")

if __name__ == "__main__":
    main()
