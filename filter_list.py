
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a_filtered = []
for x in a:
  if x < 5:
    # print(str(x))
    a_filtered.append(x)
print(str(a_filtered))

# Ask the user for the bound
bound = int(raw_input("Enter a number: "))
bounded_list = []
for x in a:
  if x < bound:
    bounded_list.append(x)
print("The numbers from list 'a' that are less than " + str(bound) + " are: " + str(bounded_list))
