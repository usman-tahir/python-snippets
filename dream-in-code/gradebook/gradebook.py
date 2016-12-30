
from grade import *

class Gradebook:
    def __init__(self, grades):
        self.grades = grades
        self.total_weight = Gradebook.calculate_total_weight(self, grades)

    def calculate_total_weight(self, grades):
        total_weight = 0.00 # Ideally 1.00, after the iteration
        for grade in grades:
            total_weight += grade.get_weight()
        return total_weight

    def calculate_total_grade(self):
        total_grade = 0.00
        for grade in self.grades:
            total_grade += (grade.calculate_grade())
        return (total_grade * 100)

grade_one = Grade(98, 100, 0.10)
grade_two = Grade(76, 100, 0.25)
grade_three = Grade(70, 100, 0.35)
grade_four = Grade(100, 100, 0.30)

grades = [grade_one, grade_two, grade_three, grade_four]
gradebook = Gradebook(grades)
print(gradebook.calculate_total_grade())
