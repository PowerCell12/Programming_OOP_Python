class  take_skip:

  def __init__(self, step, count):
    self.step = step
    self.count = count
    self.count1 = 0
    self.final = 0
  
  def __iter__(self):
    self.count1 = 0
    self.final = 0
    
    return self


  def __next__(self):

    if self.count1 == self.count:
      raise StopIteration
    
    self.count1 += 1
    i = self.final
    self.final += self.step
    return i


numbers = take_skip(100, 10)
for number in numbers:
    print(number)
