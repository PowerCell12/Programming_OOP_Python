class Shop:

    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {} #name >= qunaitty


    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)
    

    def add_item(self, item_name):

        if self.capacity -  1 >= 0:
            self.capacity -= 1

            if item_name in self.items.keys():
                self.items[item_name] += 1
            else:
                self.items[item_name] = 1

            return f"{item_name} added to the shop"

        else:
            return  "Not enough capacity in the shop"
        

    def remove_item(self, item_name, amount):

        if item_name in self.items.keys():
            if self.items[item_name] - amount == 0:
                del self.items[item_name]
                return f"{amount} {item_name} removed from the shop"

            if amount > self.items[item_name]:
                return f"Cannot remove {amount} {item_name}"
        
            self.items[item_name] -= amount
            return f"{amount} {item_name} removed from the shop"
        else:
            return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
