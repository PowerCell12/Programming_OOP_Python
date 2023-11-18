class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = list(sequence)
        self.number = number
        self.end =0  
        self.all = 0

    def __iter__(self):
        self.end = 0
        self.all = 0
        return self
    

    def __next__(self):
        
        if self.all == self.number:
           raise StopIteration
        
        if self.end >= len(self.sequence):
           self.end = 0

        index = self.end
        self.end +=1
        self.all += 1
        return self.sequence[index]
