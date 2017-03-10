# Given 3 int values, a b c, return their sum. However, if any of the values is
# a teen -- in the range 13..19 inclusive -- then that value counts as 0, except
# 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"
# that takes in an int value and returns that value fixed for the teen rule. In
# this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main
# no_teen_sum().

def fix_teen(n):
    if n in list(range(13, 20)):
        if n in [15, 16]:
            return n
        return 0
    return n

def no_teen_sum(a, b, c):
    total = 0
    for i in [a, b, c]:
        total += fix_teen(i)
    return total
