
import flashcards

class Quiz:
	def __init__(self, quiz_description, quiz_file):
		self.quiz_description = quiz_description
		self.quiz_file = quiz_file
		self.questions = Quiz.load_questions(self, quiz_file)

	def get_quiz_description(self):
		return self.quiz_description

	def get_quiz_file(self):
		return self.quiz_file

	def get_questions(self):
		return self.questions

	def set_quiz_description(self, quiz_description):
		self.quiz_description = quiz_description

	def set_quiz_file(self, quiz_file):
		self.quiz_file = quiz_file

	def set_questions(self):
		self.questions = Quiz.load_questions(self, self.quiz_file)

	def load_questions(self, quiz_file):
		data = open(quiz_file)
		items = data.readlines()
		questions = []

		for item in items:
			current_pair = item.split(",")
			questions.append(flashcards.Flashcard(current_pair[0], current_pair[1].strip("\n")))
		return questions

q = Quiz("State Capitals", "./state_capitals.txt")