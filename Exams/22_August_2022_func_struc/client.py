class Client:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart  = []
        self.bill = 0.0
        self.food_added = {}


    @property
    def phone_number(self):
        return  self.__phone_number

    @phone_number.setter
    def phone_number(self, value): ## if error check the last thing

        if value[0] != "0" or len(value) < 10 or [something for something in value if not something.isdigit()]:
            raise ValueError("Invalid phone number!")

        self.__phone_number = value
