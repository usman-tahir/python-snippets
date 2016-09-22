
name = raw_input("Please enter your name: ")
age = input("Please enter your age: ")

print("Your name is %s and you are %s years old." % (name, str(age)))
until_100 = 100 - int(age)

if until_100 <= 100 and until_100 >= 0:
  print("You will turn 100 in %s years." % (str(until_100)))
else:
  print("You are already 100 or over.")