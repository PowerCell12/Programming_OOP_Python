def reverse_text(string):

  
  for i in range(len(string) - 1, - 1, - 1):
    char = string[i]

    yield char
