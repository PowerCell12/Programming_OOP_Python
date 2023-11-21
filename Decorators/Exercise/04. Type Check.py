def type_check(n):
  def decorator(function):

    def wraper(num):

      if type(num) == n:
        return function(num)
      else:
        return "Bad Type"

    return wraper

  return decorator
