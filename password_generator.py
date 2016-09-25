import random

letters = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
  'n', 'o', 'p', 'q' ,'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
  ]
# print(str(letters))

numbers = list(range(0, 10))
# print(str(numbers))

# Basic symbols
symbols = [
  "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "+"
]
# print(str(symbols))

combined = letters + symbols + numbers
# print(str(combined))

password_length = int(raw_input("How long do you want your password to be? "))
password = ""

for x in range(password_length):
  selected_character = combined[(random.randrange(0, len(combined) - 1))]
  password += str(selected_character)

print("The password generated for you was: ")
print(str(password))