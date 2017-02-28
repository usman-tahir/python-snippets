# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num)
# computes the absolute value of a number.

def near_hundred(n):
    near_100 = abs(100 - n) <= 10
    near_200 = abs(200 - n) <= 10
    return (near_100 or near_200)
