
class Grade:
    def __init__(self, earned, total, weight):
        self.earned = earned
        self.total = total
        self.weight = weight

    def get_earned(self):
        return self.earned

    def get_total(self):
        return self.total

    def get_weight(self):
        return self.weight

    def set_earned(self, earned):
        if earned < 0:
            print("You entered an invalid 'earned' value.")
            return false
        else:
            self.earned = earned
            return true

    def set_total(self, total):
        if total < 0 or total < self.earned:
            print("You entered an invalid 'total' value.")
            return false
        else:
            self.total = total
            return true

    def set_weight(self, weight):
        if weight < 0:
            print("You entered an invalid 'weight' value")
            return false
        else:
            self.weight = weight
            return true

    def calculate_grade(self):
        return ((float(self.earned) / self.total) * (self.weight))

    def __str__(self):
        return str(self.calculate_grade())
