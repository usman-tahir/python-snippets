
# Contains all the methods from the DreamInCode examples

def reverse(string):
    result = ""
    for s in range(len(string) - 1, -1, -1):
        result += string[s]
    return result

def count_vowels(string):
    vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for letter in range(len(string)):
        if string[letter].lower() in ["a", "e", "i", "o", "u"]:
            vowels[string[letter].lower()] += 1
    return vowels

def main():
    print(count_vowels("hello my name is Usman"))

if __name__ == "__main__":
    main()
