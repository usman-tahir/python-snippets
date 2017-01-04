
class Scrabble:
    def __init__(self):
        # Words from the official Scrabble Dictionary (SOWPODS)
        self.words = Scrabble.initialize_words(self, "./words.txt")

        # Scores for the individual letters used in a word
        self.scores = {
            "a": 1, "b": 3,
            "c": 3, "d": 2,
            "e": 1, "f": 4,
            "g": 2, "h": 4,
            "i": 1, "j": 8,
            "k": 5, "l": 1,
            "m": 3, "n": 1,
            "o": 1, "p": 3,
            "q": 10, "r": 1,
            "s": 1, "t": 1,
            "u": 1, "v": 4,
            "w": 4, "x": 8,
            "y": 4, "z": 10
        }
    def initialize_words(self, filepath):
        file_opened = open(filepath)
        words = file_opened.readlines()
        parsed_words = []
        for word in words:
            word = word.strip("\n")
            parsed_words.append(word)
        return parsed_words

    def score_word(self, word):
        letters = list(word)
        score = 0
        for letter in letters:
            score += self.scores[letter.lower()]
        return score
