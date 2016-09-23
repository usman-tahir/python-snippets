
a = [5, 10, 15, 20, 25]
b = []

for x in range(len(a)):
  if x == 0 or x == len(a) - 1:
    b.append(a[x])

print("Elements in list 'a':")
print(str(a))

print("\nElements in list 'b' (first and last elements of a):")
print(str(b))