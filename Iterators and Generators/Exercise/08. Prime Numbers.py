def get_primes(numbers):

  prime = []

  for i in numbers:
    c = 0
    for j in range(1, i):
      if i % j == 0:
        c += 1
    if c == 1:
      prime.append(i)

  for num in prime:

    yield num
