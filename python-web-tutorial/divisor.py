
number = int(raw_input("Enter a number to find its divisors: "))
possible_divisors = list(range(1, number + 1))

# print("The possible divisors are: " + str(possible_divisors))

actual_divisors = []

for x in possible_divisors:
  if number % x == 0:
    actual_divisors.append(x)

print("The divisors of " + str(number) + " are: " + str(actual_divisors))

# Prime numbers are only divisible by one and themselves
if (len(actual_divisors) == 2):
  print("This number is prime.")