# Given 3 int values, a b c, return their sum. However, if one of the values is
# 13 then it does not count towards the sum and values to its right do not
# count. So for example, if b is 13, then both b and c do not count.

def lucky_sum(a, b, c):
    elements = [a, b, c]

    if not 13 in elements:
        return sum(elements)
    else:
        total = 0
        for e in range(len(elements)):
            if elements[e] == 13 and e < len(elements):
                return total
            else:
                total += elements[e]
