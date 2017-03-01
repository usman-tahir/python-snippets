# Given a string, return a "rotated left 2" version where the first 2 chars are
# moved to the end. The string length will be at least 2.

def left2(s):
    if len(s) == 2:
        return s
    else:
        return s[2:] + s[0:2]
