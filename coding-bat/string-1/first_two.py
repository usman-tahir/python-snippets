# Given a string, return the string made of its first two chars, so the String
# "Hello" yields "He". If the string is shorter than length 2, return whatever
# there is, so "X" yields "X", and the empty string "" yields the empty string
# "".

def first_two(s):
    if len(s) in [0, 1, 2]:
        return s
    return s[0:2]
