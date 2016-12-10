
# Check for even or odd (parity)
number = int(raw_input("Enter a number: "))

# Change the input into a positive number if necessary
if number < 0:
  number = number * -1

if number % 2 == 0:
  parity = "even."
else:
  parity = "odd."

print("This number is " + parity)

# Check for divisibility (remainder of 0)
number_one = int(input("Enter a number: "))
number_two = int(input("Enter a second number: "))

remainder = number_one % number_two

if remainder != 0:
  print(str(number_one) + " does not divide into " + str(number_two) + ".");
else:
  print(str(number_one) + " divides into " + str(number_two) + " " + str(number_one // number_two) + " time(s).")
