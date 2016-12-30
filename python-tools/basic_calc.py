
import calc

class BasicCalculator(calc.Calculator):
  def __init__(self):
    calc.Calculator.__init__(self)
  
  def add(self, a, b):
    self.current_result = (a + b)
    return True

  def subtract(self, a, b):
    self.current_result = (a - b)
    return True

  def multiply(self, a, b):
    self.current_result = (a * b)
    return True
  
  def divide(self, a, b):
    if (b == 0):
      return False
    self.current_result = (a / b)
    return True
  
  def __str__(self):
    return calc.Calculator.__str__(self)