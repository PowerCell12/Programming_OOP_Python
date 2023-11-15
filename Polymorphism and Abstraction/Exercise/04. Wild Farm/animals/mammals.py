from project.animals.animal import Mammal

class Mouse(Mammal):

  def make_sound(self):
    return "Squeak"


  def feed(self, food):

    if type(food).__name__ != "Fruit" and type(food).__name__ != "Vegetable":
      return f"{__class__.__name__} does not eat {type(food).__name__}!"
    else:
      self.weight += food.quantity * 0.10
      self.food_eaten += food.quantity


  def __repr__(self):
    return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

class Dog(Mammal):

  def make_sound(self):
    return "Woof!"


  def feed(self, food):

    if type(food).__name__ != "Meat":
      return f"{__class__.__name__} does not eat {type(food).__name__}!"
    else:
      self.weight += food.quantity * 0.40
      self.food_eaten += food.quantity

  def __repr__(self):
    return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Cat(Mammal):

  def make_sound(self):
    return "Meow"


  def feed(self, food):

    if type(food).__name__ != "Meat" and type(food).__name__ != "Vegetable":
      return f"{__class__.__name__} does not eat {type(food).__name__}!"
    else:
      self.weight += food.quantity * 0.30
      self.food_eaten += food.quantity

  def __repr__(self):
    return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Tiger(Mammal):


  def make_sound(self):
    return "ROAR!!!"


  def feed(self, food):

    if type(food).__name__ != "Meat":
      return f"{__class__.__name__} does not eat {type(food).__name__}!"
    else:
      self.weight += food.quantity
      self.food_eaten += food.quantity

  def __repr__(self):
    return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
