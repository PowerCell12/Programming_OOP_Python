from functools import wraps
def logged(function):

    @wraps(function)
    def wrap(*args):
      first = function(*args)

      return f"you called {function.__name__}{args}\nit returned {first}"

    return wrap

