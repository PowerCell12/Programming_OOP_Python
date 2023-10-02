def print_figure_upper(size, spaces):
  global stars
  stars = ""
  string = ""
  for i in range(size):  
    stars += "* "
    print(f"{' ' * spaces + stars}")
    spaces -= 1

def print_figure_lower(size, spaces1, stars):
  stars = stars.split()
  string = ""
  for i in range(size):
    stars.pop()
    print(f"{spaces1 * ' '}{' '.join(stars)}")    
    spaces1 += 1


size = int(input())

spaces = size -1 
spaces1 = 1

print_figure_upper(size, spaces)
print_figure_lower(size, spaces1, stars)
