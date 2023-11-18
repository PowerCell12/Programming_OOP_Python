def fibonacci():
  first = 0
  count = 0
  secondtolast = 1
  last = 0
  
  while True:

    if count == 0:
      yield first 
    elif count == 1:
      yield 1
    else:
      first = last + secondtolast
      yield first
      last = secondtolast
      secondtolast  = first

      
    count += 1
