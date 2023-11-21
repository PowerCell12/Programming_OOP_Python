def even_parameters(function):

  def wrapper(*args):

    for arg in args:

      if type(arg) == int:
        if arg % 2 == 0:
          pass
        else:
          return "Please use only even numbers!"
      else:
        return "Please use only even numbers!"


    return function(*args)

  
  return wrapper
