import random

# Open a file and write 10 random numbers to it
with open("random_numbers.txt", "w+") as file:
	for x in range(10):
		file.write("%s\n" % (str(random.randrange(0, 101))))
print("finished creating random_numbers.txt")