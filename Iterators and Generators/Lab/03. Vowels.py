class vowels:
    VOWELS = "aeiouyAEIOUY"

    def __init__(self, string):
       self.string = string
       self.vowels_in = [vow for vow in self.string if vow in self.VOWELS]


    def __iter__(self):
       return self
    
    def __next__(self):
       
      if not self.vowels_in:
         raise StopIteration

      return self.vowels_in.pop(0)
