
sentence = str(raw_input("Please enter a complete sentence: "))
words = sentence.split(" ")
# print(str(words))

# Determine the number of words, to loop back from the last word
length = len(words) - 1
reversed_sentence = ""

# Build the new sentence
while length >= 0:
  reversed_sentence += (words[length] + " ")
  length -= 1

print(reversed_sentence)