# Given a string and a non-negative int n, we'll say that the front of the
# string is the first 3 chars, or whatever is there if the string is less than
# length 3. Return n copies of the front;

def front_times(s, n):
    if len(s) in range(4):
        return s * n
    return s[0:3] * n
