
import quiz

def ask_questions(quiz_instance):
  score = 0
  q = quiz_instance.get_questions()
  a = quiz_instance.get_answers()

  for i in range(len(q)):
    response = str(input(q[i] + " "))
    if response.lower() == a[i].lower():
      print("Correct!")
      score += 1
    else:
      print("Incorrect.")
  
  return score

def main():
  new_quiz = quiz.Quiz("./questions.txt", "./answers.txt")
  print("You scored %d out of %d points." % (ask_questions(new_quiz), len(new_quiz.get_questions())))

if __name__ == "__main__":
  main()