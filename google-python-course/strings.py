
# Common string methods

string_one = "Hello world!"

print(string_one.lower()) # 'hello world!'
print(string_one.upper()) # 'HELLO WORLD!'

string_two = "  Beginning and ending spaces.  "
print(string_two.strip()) # 'Beginning and ending spaces.'

string_three = "22"
string_four = "text"
string_five = " "

print(string_three.isdigit()) # True
print(string_four.isalpha()) # True
print(string_five.isspace()) # True

print(string_one.startswith("Hello")) # True
print(string_one.endswith("world!")) # True

print(string_one.find("H")) # '0'
print(string_one.find("z")) # '-1'

string_six = "Foo Bar Baz Qux"
print(string_six.replace("Bar", "Foo")) # 'Foo Foo Baz Qux'

string_seven = "Too, many commas in, this, sentence"
print(string_seven.split(",")) # ['Too', ' many commas in', ' this', ' sentence']

word_list = ["Hello", "my", "name", "is", "John"]
string_eight = (" ".join(word_list)) # 'Hello my name is John'
print(string_eight)