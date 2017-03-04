# Given a string, return a string where for every char in the original, there
# are two chars.

def double_char(s):
    return ''.join([i * 2 for i in list(s)])
