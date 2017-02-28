# Given a string, return the count of the number of times that a substring
# length 2 appears in the string and also as the last 2 chars of the string,
# so "hixxxhi" yields 1 (we won't count the end substring).

def last2(s):
    count = 0
    last_two = s[len(s) - 2:]

    for x in range(len(s)):
        if s[x:x + 2] == last_two and x < len(s) - 2:
            count += 1
    return count
