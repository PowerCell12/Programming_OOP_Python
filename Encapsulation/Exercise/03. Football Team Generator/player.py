class Player:


  def __init__(self, name, sprint, dribble, passing, shooting):
    self.__name = name
    self.__sprint = sprint
    self.__dribble = dribble
    self.__passing = passing
    self.__shooting = shooting

  @property
  def name(self):
    return self.__name


  def __str__(self):
    to_return = []

    to_return.append(f"Player: {self.__name}")
    to_return.append(f"Sprint: {self.__sprint}")
    to_return.append(f"Dribble: {self.__dribble}")
    to_return.append(f"Passing: {self.__passing}")
    to_return.append(f"Shooting: {self.__shooting}")

    return "\n".join(to_return)

