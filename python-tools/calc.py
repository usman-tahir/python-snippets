
class Calculator:
  def __init__(self):
    self.current_result = 0
    self.current_memory = 0
  
  def get_current_result(self):
    return self.current_result
  
  def get_current_memory(self):
    return self.current_memory
  
  def set_current_result(self, result):
    self.current_result = result
  
  def set_current_memory(self, memory):
    self.current_memory = memory
  
  def clear_result(self):
    self.current_result = 0
  
  def clear_memory(self):
    self.current_memory = 0
  
  def __str__(self):
    return "%f" % (self.current_result)
