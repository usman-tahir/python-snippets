# Given 2 strings, a and b, return the number of the positions where they
# contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since
# the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
    subsets_a = [a[i:i + 2] for i in range(len(a) - 1)]
    subsets_b = [b[i:i + 2] for i in range(len(b) - 1)]
    return len(subsets_a + subsets_b) - (len(set(subsets_a + subsets_b)))
