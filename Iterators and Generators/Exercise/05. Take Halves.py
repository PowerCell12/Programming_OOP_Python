def solution():

  def integers():

    start = 1

    while True:

      yield start

      start += 1


  def halves():

    for i in integers():

      yield i / 2
  
  def take(n, seq):
    final = []

    
    for i in range(n):
      final.append(next(iter(seq)))

    
    return final
  return (take, halves, integers)
