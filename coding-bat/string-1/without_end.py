# Given a string, return a version without the first and last char, so "Hello"
# yields "ell". The string length will be at least 2.

def without_end(s):
    if len(s) == 2:
        return ''
    return s[1:-1]
