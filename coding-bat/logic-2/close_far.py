# Given three ints, a b c, return True if one of b or c is "close" (differing
# from a by at most 1), while the other is "far", differing from both other
# values by 2 or more. Note: abs(num) computes the absolute value of a number.

def close_far(a, b, c):
    test_1 = (abs(b - a) <= 1) and (abs(c - b) >= 2 and abs(c - a) >= 2)
    test_2 = (abs(c - a) <= 1) and (abs(b - a) >= 2 and abs(c - b) >= 2)
    return test_1 or test_2
