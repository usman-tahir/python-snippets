# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(s):
    result = ''
    letters = list(s)
    for i in range(len(letters) + 1):
        result += s[0:i]
    return result
