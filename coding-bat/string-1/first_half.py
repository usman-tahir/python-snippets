# Given a string of even length, return the first half. So the string "WooHoo"
# yields "Woo".

def first_half(s):
    return s[:len(s) // 2]
