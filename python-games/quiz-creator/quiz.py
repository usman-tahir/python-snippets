
class Quiz:
  def __init__(self, questions_file, answers_file):
    self.questions_file = questions_file
    self.answers_file = answers_file
    self.parsed_questions = Quiz.parse_data(self, self.questions_file)
    self.parsed_answers = Quiz.parse_data(self, self.answers_file)
  
  def parse_data(self, file_path):
    data = open(file_path).readlines()
    parsed_data = []
    for d in data:
      parsed_data.append(d.rstrip("\n"))
    
    return parsed_data
  
  def get_questions(self):
    return self.parsed_questions
  
  def get_answers(self):
    return self.parsed_answers
  
  def set_questions(self, questions_file):
    self.parsed_questions = Quiz.parse_data(questions_file)
  
  def set_answers(self, answers_file):
    self.parsed_answers = Quiz.parse_data(answers_file)