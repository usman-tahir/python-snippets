
import random

def get_lottery_numbers(amount = 5):
  lottery_numbers = []

  for i in range(amount):
    lottery_numbers.append(random.randint(0, 100))
  
  return lottery_numbers

def get_user_entry(amount = 5):
  user_numbers = []

  for x in range(amount):
    while len(user_numbers) < amount:
      number = int(input("Enter a number between 0 and 100: "))
      if (int(number) and (number >= 0 and number <= 100)):
        user_numbers.append(number)
      else:
        print("Please enter a valid number between 0 and 100")
  
  return user_numbers

def compare_numbers(user_numbers, lottery_numbers):
  matches = 0

  for i in range(len(user_numbers)):
    if lottery_numbers[i] == user_numbers[i]:
      matches += 1
  
  return matches

def main():
  lottery_numbers = get_lottery_numbers()
  user_numbers = get_user_entry()

  matches = compare_numbers(lottery_numbers, user_numbers)
  if matches == len(lottery_numbers):
    print("You won the lottery!")
  else:
    print("You matched %d out of the %d numbers. Better luck next time!" \
      % (matches, len(lottery_numbers)))

if __name__ == "__main__":
  main()