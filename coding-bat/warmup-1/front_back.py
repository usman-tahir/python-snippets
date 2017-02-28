# Given a string, return a new string where the first and last chars have been
# exchanged.

def front_back(s):
    if len(s) in [0, 1]:
        return s
    elif len(s) == 2:
        return s[-1] + s[0]
    else:
        return s[-1] + s[1:-1] + s[0]
