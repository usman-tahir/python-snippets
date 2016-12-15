
import random

# Generate a mastermind puzzle based on a difficulty
def generate_mastermind_puzzle(difficulty = 4):
    # Original list of colors that simulates the colored stones
    colors = ["R", "O", "Y", "G", "B", "I", "V"]
    puzzle = [""] * difficulty

    # Ensures that colors are used only once
    for i in range(difficulty):
        random.shuffle(colors)
        puzzle[i] = colors.pop(0)

    return puzzle

# Determine the correctness of the user's guess based on the actual pattern
def get_positional_status(actual_puzzle, user_guess):
    result = [""] * len(actual_puzzle)

    for i in range(len(actual_puzzle)):
        if actual_puzzle[i] == user_guess[i]:
            result[i] = "C"
        else:
            if actual_puzzle[i] != user_guess[i] and user_guess[i] in actual_puzzle:
                result[i] = "P"
            else:
                result[i] = "I"

    return result

def main():
    puzzle = generate_mastermind_puzzle()
    print(puzzle)
    print(get_positional_status(puzzle, ["R", "G", "Y", "B"]))

if __name__ == "__main__":
    main()
