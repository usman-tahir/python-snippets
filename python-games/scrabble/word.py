
class Word:
	def __init__(self, word, score):
		self.word = word
		self.score = score

	def get_word(self):
		return self.word

	def get_score(self):
		return self.score

	def set_word(self, word):
		self.word = word

	def set_score(self, score):
		self.score = score

	def __str__(self):
		return self.word + " (" + str(self.score) + ")\n"