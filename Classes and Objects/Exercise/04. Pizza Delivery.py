class PizzaDelivery:

    def __init__(self, name: str, price: float, ingredients: dict):

        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False
        self.bool = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):

        if self.bool:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient in self.ingredients.keys():
            self.ingredients[ingredient] += quantity
            self.price += quantity * price_per_quantity
        else:
            self.ingredients[ingredient] = quantity
            self.price += quantity * price_per_quantity

    
    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):

        if self.bool:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
    
        elif ingredient in self.ingredients.keys() and self.ingredients[ingredient] - quantity < 0:
            return f"Please check again the desired quantity of {ingredient}!"
        
        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_quantity

    def make_order(self):

        if self.bool:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        self.ordered = True

        string = []
        for key,value in self.ingredients.items():
            string.append(f"{key}: {value}")

        self.bool = True
        return  f"You've ordered pizza {self.name} prepared with {', '.join(string)} and the price will be {self.price}lv."
