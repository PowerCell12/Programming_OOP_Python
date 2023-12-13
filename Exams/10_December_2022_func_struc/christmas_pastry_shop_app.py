from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    def __init__(self):
      self.booths = []
      self.delicacies = []
      self.income = 0



    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        if name in [h.name for h in self.delicacies]:
            raise Exception(f"{name} already exists!")

        if type_delicacy != "Stolen" and type_delicacy != "Gingerbread":
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")


        if type_delicacy == "Stolen":
            self.delicacies.append(Stolen(name, price))
        elif type_delicacy == "Gingerbread":
            self.delicacies.append(Gingerbread(name, price))

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."


    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        if booth_number in [h.booth_number for h in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")


        if type_booth != "Open Booth" and type_booth != "Private Booth":
            raise Exception(f"{type_booth} is not a valid booth!")


        if type_booth == "Open Booth":
            self.booths.append(OpenBooth(booth_number, capacity))
        elif type_booth == "Private Booth":
            self.booths.append(PrivateBooth(booth_number, capacity))

        return f"Added booth number {booth_number} in the pastry shop."


    def reserve_booth(self, number_of_people: int): ## if errors check

        bool1 = False
        booth_number = None

        for booth in self.booths:

            if booth.is_reserved == False and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                bool1 = True
                booth_number = booth.booth_number
                break


        if not bool1:
            raise Exception(f"No available booth for {number_of_people} people!")
        else:
            return f"Booth {booth_number} has been reserved for {number_of_people} people."


    def order_delicacy(self, booth_number: int, delicacy_name: str): ## probably wrong check
        booth  = None
        delicacy =None

        if booth_number not in [h.booth_number for h in self.booths]:
            raise Exception(f"Could not find booth {booth_number}!")

        if delicacy_name not in [h.name for h in self.delicacies]:
            raise Exception(f"No {delicacy_name} in the pastry shop!")


        for booth1 in self.booths:
            if booth_number == booth1.booth_number:
                booth = booth1
                break


        for delicacy1 in self.delicacies:
            if delicacy_name == delicacy1.name:
                delicacy = delicacy1
                break


        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):
        booth = None
        bill = 0

        for booth1 in self.booths:
            if booth1.booth_number == booth_number:
                booth = booth1
                break

        self.income += booth.price_for_reservation
        bill += booth.price_for_reservation
        for delicacy in booth.delicacy_orders:
            self.income += delicacy.price
            bill += delicacy.price

        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0
        list_return = []
        list_return.append(f"Booth {booth.booth_number}:")
        list_return.append(f"Bill: {bill:.2f}lv.")

        return "\n".join(list_return)

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
