
import flashcards
import quiz
import random

def start_quiz(quiz):
	correct = 0
	questions = quiz.get_questions()
	total = len(questions)
	print(quiz.get_quiz_description() + "\n")
	for i in range(total):
		current_question = questions[i].get_question()
		current_answer = questions[i].get_answer()

		user_answer = raw_input("\n" + str(current_question) + "? ")
		if (user_answer.lower() == current_answer.lower()):
			print("Correct!")
			correct += 1
		else:
			print("Incorrect (" + current_answer + ").")
	return correct



def main():
	q = quiz.Quiz("State Capitals Quiz", "./state_capitals.txt")
	correct = start_quiz(q)
	print("\nYou got %s out of %s correct." % (str(correct), str(len(q.get_questions()))))

if __name__ == "__main__":
	main()