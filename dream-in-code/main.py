
# Contains all the methods from the DreamInCode examples

def reverse(string):
    result = ""
    for s in range(len(string) - 1, -1, -1):
        result += string[s]
    return result

def main():
    print(reverse("hello world"))

if __name__ == "__main__":
    main()
