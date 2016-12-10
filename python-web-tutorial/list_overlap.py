import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

overlap = []

for x in a:
  if x in b:
    overlap.append(x)

print("The list overlap between 'a' and 'b' consists of: " + str(overlap))

# Two lists of random integers between 0 and 10, between 3 and 5 elements long
list_one = [random.randrange(0, 11) for x in range(random.randrange(3, 5))]
list_two = [random.randrange(0, 11) for x in range(random.randrange(3, 5))]
print(str(list_one))
print(str(list_two))