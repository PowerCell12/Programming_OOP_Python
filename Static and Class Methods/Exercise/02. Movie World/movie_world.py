from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = [] #objects
        self.dvds = [] #objects
        self.DvdCapacity = 15
        self.CustomerCapacity = 10
    
    @staticmethod
    def dvd_capacity(): 
       return 15

    @staticmethod
    def customer_capacity(): 
        return 10
    

    def add_customer(self, customer: Customer):

        if self.CustomerCapacity - 1 >= 0:
            self.CustomerCapacity -=1
            self.customers.append(customer)


    def add_dvd(self, dvd: DVD):
        
        if self.DvdCapacity - 1 >= 0:
            self.DvdCapacity -= 1
            self.dvds.append(dvd)


    def rent_dvd(self, customer_id, dvd_id):
        
        for dvd in self.dvds:
            if dvd_id == dvd.id:
                global dvd1
                dvd1 = dvd

        for customer in self.customers:
            if customer.id == customer_id:
                global customer1
                customer1 = customer


        if dvd1.is_rented == True:

            if dvd1 in customer1.rented_dvds:
                return f"{customer1.name} has already rented {dvd1.name}"
            else:
                return "DVD is already rented"
        
        else:

            if dvd1.age_restriction > customer1.age:
                return f"{customer1.name} should be at least {dvd1.age_restriction} to rent this movie"
            

            for customer in self.customers:

                if customer.id == customer_id:
                    customer.rented_dvds.append(dvd1)

            for dvd in self.dvds:

                if dvd_id == dvd.id:
                    dvd.is_rented = True
            
            return f"{customer1.name} has successfully rented {dvd1.name}"
        

    def return_dvd(self, customer_id, dvd_id):


        for dvd in self.dvds:
            if dvd_id == dvd.id:
                global dvd1
                dvd1 = dvd

        for customer in self.customers:
            if customer.id == customer_id:
                global customer1
                customer1 = customer


        if dvd1 in customer1.rented_dvds:

            for customer in self.customers:
                if customer.id == customer_id:
                    customer.rented_dvds.remove(dvd1)
                    index = self.dvds.index(dvd1)
                    self.dvds[index].is_rented = False
            
            return f"{customer1.name} has successfully returned {dvd1.name}"
        else:
            return f"{customer1.name} does not have that DVD"
        


    def __repr__(self):
        to_return  = []

        for customer in self.customers:

            to_return.append(str(customer))

        for dvd in self.dvds:

            to_return.append(str(dvd))


        return '\n'.join(to_return)



