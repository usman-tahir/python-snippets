import random

# Loop style
def return_unique(some_list):
  uniques = []
  for x in some_list:
    if x not in uniques:
      uniques.append(x)
  return sorted(uniques)

# Usage of set
def return_set(some_list):
  return(sorted(list(set(some_list))))

# Generate a list of random integers between 3 and 20 in size
a = [random.randrange(0, 101) for x in range(random.randrange(3, 21))]
print(str(a))
# List without any duplicates
b = return_unique(a)
print(str(b))

c = return_set(a)
print(str(c))

# Check to see if the above two methods return the same input
# of unique elements
print(str(b) == str(c))