
import calc

class BasicCalculator(calc.Calculator):
  def __init__(self):
    calc.Calculator.__init__(self)
  
  def add(self, a, b):
    self.current_result = (a + b)
    return self.current_result

  def subtract(self, a, b):
    self.current_result = (a - b)
    return self.current_result

  def multiply(self, a, b):
    self.current_result = (a * b)
    return self.current_result
  
  def divide(self, a, b):
    if (b == 0):
      raise ValueError("You cannot divide by zero.")
    self.current_result = (a / b)
    return self.current_result
  
  def __str__(self):
    return calc.Calculator.__str__(self)