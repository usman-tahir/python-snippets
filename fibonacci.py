import sys

def fibonacci(a):
  return(a.append(a[-1] + a[-2]))

number = int(raw_input("How many fibonacci numbers do you wish to generate? "))
fibonacci_numbers = []

if number > 1:
  a = [1, 1]
  for x in range(number - 2):
    fibonacci(a)
else:
  if number == 0:
    a = []
  elif number == 1:
    a = [1]
  else:
    print("That was an invalid number.")
    sys.exit()

print("The %s fibonacci number(s) generated were:" % (str(number)))
print(str(a))