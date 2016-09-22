
word = raw_input("Enter a word: ")
print("You entered " + word + ".")

# Determine if the word is a palindrome
reversed_word = []
index = len(word) - 1

while index >= 0:
  reversed_word.append(word[index])
  index = index - 1

# print(str(reversed_word))
palindrome = True
for x in range(len(word)):
  if word[x] != reversed_word[x]:
    palindrome = False
    break

if palindrome:
  print("This word is a palindrome.")
else:
  print("This word is not a palindrome.")
      