class dictionary_iter:

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.count = 0
        self.length = len(dictionary)

    def __iter__(self):
        self.count = 0
        return self
    

    def __next__(self):
        if self.count == self.length:
           raise StopIteration
        

        self.count += 1
        count_dic = 0
        global key
        global value

        for key, value in self.dictionary.items():
            count_dic += 1

            if count_dic == self.count:
               break
            
        return key, value
