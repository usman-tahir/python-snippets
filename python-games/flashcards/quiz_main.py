
import os.path
import flashcards
import quiz
import random

def get_quiz_file():
	quiz_name = input("Enter a name for the quiz: ")
	user_file = input("Enter the file name (Example: 'problems.txt'): ")
	if os.path.isfile("./" + str(user_file)):
		if len(quiz_name) > 0:
			return quiz.Quiz(quiz_name, "./" + str(user_file))
		else:
			print("You entered a blank quiz name.")
	else:
		print("Please re-run this script and enter a valid quiz file.")
	

def start_quiz(quiz):
	correct = 0
	asked = 0
	questions = quiz.get_questions()
	total = len(questions)
	print(quiz.get_quiz_description() + "\nAnswer the question, or input 'exit' to quit.")
	for i in range(total):
		current_question = questions[i].get_question()
		current_answer = questions[i].get_answer()

		user_answer = input("\n" + str(current_question) + "? ")
		if (user_answer.lower() == current_answer.lower()):
			print("Correct!")
			correct += 1
			asked += 1
		elif (user_answer.lower() == "exit"):
			break
		else:
			print("Incorrect (" + current_answer + ").")
			asked += 1
	return [correct, asked]



def main():
	q = get_quiz_file()
	correct = start_quiz(q)
	print("\nYou got %s out of %s correct." % (str(correct[0]), str(correct[1])))

if __name__ == "__main__":
	main()