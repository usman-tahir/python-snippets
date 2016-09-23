
def get_divisors(number):
  divisors = []
  for x in range(1, number + 1):
    if number % x == 0:
      divisors.append(x)
  return(divisors)

number = int(raw_input("Enter a number: "))
divisors = get_divisors(number)
# print(str(divisors))

if len(divisors) > 2:
  print("This number is not prime.")
else:
  print("This number is prime.")