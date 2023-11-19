def number_increment(numbers):
  def increase():

      new_list = [char + 1 for char in numbers]
      
      return new_list
  return increase()
