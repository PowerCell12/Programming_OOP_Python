def multiply(n):
    def decorator(func):
      def wrapper(*args):
        final  = func(*args)
        return final * n

      return wrapper
    return decorator
