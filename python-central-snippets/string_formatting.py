
# Strings to join for building a sentence
name = "Usman"
age = 22
favorite_food = "pizza"
favorite_color = "green"

# Concatenation example
concatenated_string = "Hey, I'm " + name + " and I'm " + str(age) + " years old. I love " \
	+ favorite_food + " and my favorite color is " + favorite_color + "."
print(concatenated_string)

# String created using format method
formatted_string = "Hey, I'm {0} and I'm {1} years old. I love {2} and my favorite color is {3}." \
	.format(name, age, favorite_food, favorite_color)
print(formatted_string)