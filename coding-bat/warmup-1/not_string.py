# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.

def not_string(s):
    try:
        if s.index('not') >= 0:
            return s
    except:
        return 'not ' + s
