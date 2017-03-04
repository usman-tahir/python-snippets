# Return the number of times that the string "code" appears anywhere in the
# given string, except we'll accept any letter for the 'd', so "cope" and "cooe"
# count.

def count_code(s):
    subsets = [s[i:i + 4] for i in range(len(s) - 3)]
    count = 0
    for i in subsets:
        if i[0:2] == 'co' and i[-1] == 'e':
            count += 1
    return count
