
class Student:
    # rank = 0
    def __init__(self, name, grades, final_grade):
        self.name = name
        self.grades = grades
        self.final_grade = final_grade
        # self.rank = Student.rank + 1
        # Student.rank += 1

    def get_name(self):
        return self.name

    def get_grades(self):
        return self.grades

    def get_final_grade(self):
        return self.final_grade

    def set_name(self, name):
        self.name = name

    def set_grades(self, grades):
        self.grades = grades

    def set_final_grade(self, final_grade):
        self.final_grade = final_grade

    def __str__(self):
        return "\nName: " + self.name + "\nFinal grade: " + /
            str(self.final_grade) + "%\n"
