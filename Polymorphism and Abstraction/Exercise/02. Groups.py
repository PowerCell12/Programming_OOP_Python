class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    def __str__(self):
        return f'{self.name} {self.surname}'
    

    def __add__(self, other):
        return Person(self.name, other.surname)
    

class Group:

    def __init__(self, name, people):
        self.name = name
        self.people = people ## an list of instances

    def __len__(self):
        return len(self.people)
    

    def __add__(self, other):
        return Group(f"{self.name} {other.name}", self.people + other.people)
    

    def __str__(self):
        return f"Group {self.name} with members {', '.join(str(person) for person in self.people)}"
    

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index].name} {self.people[index].surname}" ## print surname too !!! error
    
