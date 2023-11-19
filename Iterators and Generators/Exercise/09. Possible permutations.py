import itertools

def possible_permutations(list1):
  

  final = list(itertools.permutations(list1))


  for permutation in final:

    yield list(permutation)
  
