class Calculator:

  @staticmethod
  def add(*args):
    total =  0 

    for things in args:
      total += things

    return total


  @staticmethod
  def multiply(*args):
    if args:
      total  = 1

      for things in args:
        total *= things

      return total
    else:
      return 0 

  @staticmethod
  def divide(*args): 

    if args:
      total = args[0]

      for thing in args:
        if thing == args[0]:
          continue

        total /= thing

      return total

    else:
        return 0

  @staticmethod
  def subtract(*args):

    if args:
      total = args[0]

      for thing in args:
        if thing == args[0]:
          continue

        total = total - thing

      return total
      
    else:
        return 0 
