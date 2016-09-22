
# Input for name (defaults to string)
name = raw_input("Please enter your name: ")

#Input for age (parsed as an integer)
age = int(input("Please enter your age: "))

# print("Your name is %s and you are %s years old." % (name, str(age)))
print("Your name is " + name + " and you are " + str(age) + " years old.")
until_100 = 100 - age

# Determine which message to output
if until_100 <= 100 and until_100 >= 0:
  print("You will turn 100 in %s years." % (str(until_100)))
else:
  print("You are already 100 or over.")