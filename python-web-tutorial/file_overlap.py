
def sanitize_input(read_array, type_of_input):
	sanitized = []
	for element in read_array:
		sanitized.append(type_of_input(element.strip("\n")))
	return sanitized

# Open the files
primes_file = open("primes_under_1000.txt", "r")
happy_numbers_file = open("happy_numbers_to_1000.txt", "r")

prime_numbers = sanitize_input(primes_file.readlines(), int)
happy_numbers = sanitize_input(happy_numbers_file.readlines(), int)

overlap = []
for prime in prime_numbers:
	if prime in happy_numbers:
		overlap.append(prime)

print("The numbers that overlap are:")
print(str(overlap))