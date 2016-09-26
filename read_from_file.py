
# Open the file and collect the names from it
with open("names.txt", "r") as file:
	names = file.readlines()

name_instances = {}
for name in names:
	current_name = name.strip("\n")
	if current_name in name_instances.keys():
		name_instances[current_name] += 1
	else:
		# Take into consideration adding the name itself for the first time
		name_instances[current_name] = 1

print("There are %s names in the names.txt file." % (str(len(names))))
print(str(name_instances))

# Print the count for each name in the file
print("Here is a breakdown of the names in this file:")
for item in name_instances.items():
	print("The name '%s' appears %s times in the file." % (item[0], item[1]))
