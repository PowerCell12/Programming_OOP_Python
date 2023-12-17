from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:

    def __init__(self):
        self.menu = []
        self.clients_list = []

    ID = 0

    def register_client(self, client_phone_number: str):

        if client_phone_number in [h.phone_number for h in self.clients_list]:
            raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."


    def add_meals_to_menu(self, *meals: Meal):

        for meal in meals:

            if meal.__class__.__name__ != "Starter" and meal.__class__.__name__ != "MainDish" and meal.__class__.__name__ != "Dessert":
                pass
            else:
                self.menu.append(meal)


    def show_menu(self): ## if error check

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        list_menus = []
        for meal in self.menu:
            list_menus.append(meal.details())

        return "\n".join(list_menus)


    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities): ## check most definitely an erorr

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if client_phone_number not in [h.phone_number for h in self.clients_list]:
            self.clients_list.append(Client(client_phone_number))

        bool1 = False
        name_meal = None
        for name in meal_names_and_quantities.keys():
            if name not in [h.name for h in self.menu]:
                bool1 = True
                name_meal = name
                break

        if bool1:
            raise Exception(f"{name_meal} is not on the menu!")


        bool2 = False
        for name, quantity in meal_names_and_quantities.items():
            object = None
            for meal in self.menu:
                if meal.name == name:
                    object = meal
                    break

            if object.quantity < quantity:
                raise Exception(f"Not enough quantity of {object.__class__.__name__}: {name}!")


        person = None
        for per in self.clients_list:
            if per.phone_number == client_phone_number:
                person = per
                break


        for meal, quantity in meal_names_and_quantities.items():
            meal1 = None
            for meal2 in self.menu:
                if meal2.name == meal:
                    meal1 = meal2
                    break

            person.shopping_cart.append(meal1)
            person.food_added[meal] = quantity
            person.bill += meal1.price * quantity
            meal1.quantity -= quantity

        return f"Client {client_phone_number} successfully ordered {', '.join([meal.name for meal in person.shopping_cart])} for {person.bill:.2f}lv."


    def cancel_order(self, client_phone_number: str): ## here
        client = None
        for cli in self.clients_list:
            if cli.phone_number == client_phone_number:
                client = cli
                break

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")


        client.shopping_cart = []
        client.bill =0

        for meal, quantity in client.food_added.items():
            for menu in self.menu:
                if menu.name == meal:
                    menu.quantity += quantity

        return f"Client {client_phone_number} successfully canceled his order."


    def finish_order(self, client_phone_number: str): ## or here
        client = None
        for cli in self.clients_list:
            if cli.phone_number == client_phone_number:
                client = cli
                break

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        bill = client.bill
        client.bill = 0
        client.shopping_cart = []

        self.ID += 1
        return f"Receipt #{self.ID} with total amount of {bill:.2f} was successfully paid for {client_phone_number}."


    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."