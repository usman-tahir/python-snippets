
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

def main():
    if validate_rack(sys.argv[-1]):
        # create_words(sys.argv[-1])
        pass
    else:
        print("Please enter a valid, 7 element rack.")

if __name__ == "__main__":
    main()
