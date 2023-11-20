from functools import wraps

def even_numbers(function):

    @wraps(function)
    def wrapper(*args):
        final = function(*args)
        return [a for a in final if a % 2 ==0]

    return wrapper
