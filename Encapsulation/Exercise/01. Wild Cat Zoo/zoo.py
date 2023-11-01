from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []


    def add_animal(self, animal, price):


        if self.__budget - price >= 0 and self.__animal_capacity - 1 >= 0:

            self.__budget -= price
            self.__animal_capacity -= 1
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        
        elif self.__budget - price < 0:
            return "Not enough budget"
        
        return "Not enough space for animal"
    

    def hire_worker(self, worker): ## worker - object
        if self.__workers_capacity  - 1 >= 0:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"
    

    def fire_worker(self, worker_name):  # not an object

        for worker in self.workers:

            if worker.name == worker_name:
                self.workers.remove(worker)
                self.__workers_capacity += 1
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"
    

    def pay_workers(self):


        mountly = 0

        for worker in self.workers:
            mountly += worker.salary

        if mountly > self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"
        
        self.__budget -= mountly
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"
    

    def tend_animals(self):

        mountly_care = 0

        for animal in self.animals:

            mountly_care += animal.money_for_care


        if mountly_care > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        
        self.__budget -= mountly_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
    

    def profit(self, amount): 

        self.__budget += amount


    def animals_status(self):
        dict_animals  = {"Lion": [], "Tiger": [], "Cheetah": []}
        to_return = []

        to_return.append(f"You have {len(self.animals)} animals")

        for animal in self.animals:

            if animal.__class__.__name__ == "Tiger":
                dict_animals["Tiger"].append(animal)

            elif animal.__class__.__name__ == "Cheetah":
                dict_animals["Cheetah"].append(animal)

            elif animal.__class__.__name__ == "Lion":
                dict_animals["Lion"].append(animal)



        for key,value in dict_animals.items(): 
            
            to_return.append(f"----- {len(value)} {key}s:")

            for val in value:
                to_return.append(f"Name: {val.name}, Age: {val.age}, Gender: {val.gender}")

        return "\n".join(to_return)


    def workers_status(self):
        dict_workers  = {"Keeper": [], "Caretaker": [], "Vet": []}
        to_return = []

        to_return.append(f"You have {len(self.workers)} workers")

        for worker in self.workers:

            if worker.__class__.__name__ == "Keeper":
                dict_workers["Keeper"].append(worker)

            elif worker.__class__.__name__ == "Caretaker":
                dict_workers["Caretaker"].append(worker)

            elif worker.__class__.__name__ == "Vet":
                dict_workers["Vet"].append(worker)

        for key,value in dict_workers.items(): 
            
            to_return.append(f"----- {len(value)} {key}s:")

            for val in value:
                to_return.append(f"Name: {val.name}, Age: {val.age}, Salary: {val.salary}")

        return "\n".join(to_return)
