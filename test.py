
a = [1, 2, 3]
b = [5, 10, 15]

# Compiles a list by multiplying the list elements and returning those that are odd
c = [x * y for x in a for y in b if x * y % 2 != 0]
print(str(c))

# Compiles all the products regardless of parity
d = [x * y for x in a for y in b]
print(str(d))