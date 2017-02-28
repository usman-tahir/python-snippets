# Given a string, return a new string made of every other char starting with
# the first, so "Hello" yields "Hlo".

def string_bits(s):
    letters = [s[letter] for letter in range(len(list(s))) if letter % 2 == 0]
    return ''.join(letters)
