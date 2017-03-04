# Return True if the string "cat" and "dog" appear the same number of times in
# the given string.

def cat_dog(s):
    subsets = [s[i:i + 3] for i in range(len(s) - 2)]
    cat, dog = 0, 0
    for i in subsets:
        if i == 'cat':
            cat += 1
        elif i == 'dog':
            dog += 1
    return len(list(set([cat, dog]))) == 1
