# Return the number of times that the string "hi" appears anywhere in the
# given string.

def count_hi(s):
    subsets = [s[i:i + 2] for i in range(len(s) - 1)]
    count = 0
    for i in subsets:
        count += 1 if i == 'hi'
    return count
