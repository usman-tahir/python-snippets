
import os.path
import flashcards
import quiz
import random

def validate_quiz_name():
	quiz_name = ""
	flag = len(quiz_name) == 0
	while flag == True:
		quiz_name = input("Enter a quiz name: ")
		if len(quiz_name) > 0:
			flag = False
		else:
			print("Please enter a non-blank quiz name.")
	return quiz_name

def validate_quiz_file():
	quiz_file = ""
	flag = (len(quiz_file) == 0) or not (os.path.isfile(quiz_file))
	while flag == True:
		quiz_file = input("Enter the file name (Example: 'problems.txt'): ")
		if (len(quiz_file) > 0) and (os.path.isfile(quiz_file) == True):
			flag = False
		else:
			print("Please enter a non-blank, valid file name.")
	return "./" + quiz_file

def get_quiz_file():
	quiz_name = validate_quiz_name()
	quiz_file = validate_quiz_file()
	return [quiz_name, quiz_file]
	

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
	quiz_info = get_quiz_file()
	q = quiz.Quiz(quiz_info[0], quiz_info[1])
	correct = start_quiz(q)
	print("\nYou got %s out of %s correct." % (str(correct[0]), str(correct[1])))

if __name__ == "__main__":
	main()