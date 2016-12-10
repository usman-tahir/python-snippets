import random

# Binary search implementation
def binary_search(sequence, element):
  minimum = 0
  maximum = len(sequence) - 1

  while True:
    if maximum < minimum:
      return -1
    
    middle = (minimum + maximum) // 2

    if sequence[middle] < element:
      minimum = middle + 1
    elif sequence[middle] > element:
      maximum = middle - 1
    else:
      return middle

# Create a random list
a = [random.randrange(0, 101) for x in range(random.randrange(3, 21))]
print(str(a))

number_to_search = int(raw_input("Enter a number to search the generated list: "))
result = binary_search(a, number_to_search)

if result == -1:
  print("This number is not in the list.")
else:
  print("The number %s was found in the list, at position %s." % (str(number_to_search), str(result)))