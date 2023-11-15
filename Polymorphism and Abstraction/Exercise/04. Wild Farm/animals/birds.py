from project.animals.animal import Bird

class Owl(Bird):

  def make_sound(self):
    return "Hoot Hoot"


  def feed(self, food):

    if type(food).__name__ != "Meat":
      return f"{__class__.__name__} does not eat {type(food).__name__}!"
    else:
      self.weight += 0.25 * food.quantity
      self.food_eaten += food.quantity


  def __repr__(self):
    return f"{__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

class Hen(Bird):


  def make_sound(self):
    return "Cluck"


  def feed(self, food):

    self.weight += food.quantity * 0.35
    self.food_eaten += food.quantity

  def __repr__(self):
    return f"{__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"