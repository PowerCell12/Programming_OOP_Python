class Smartphone:

  def __init__(self, memory):

    self.memory = memory
    self.apps = []
    self.is_on  = False

  def power(self):

    if self.is_on == False:
      self.is_on = True
    else:
      self.is_on = False


  def install(self, app, app_memory):

    if self.is_on == True and self.memory - app_memory >= 0:
      self.apps.append(app)
      self.memory -= app_memory
      return f"Installing {app}"
    elif self.is_on == False and self.memory - app_memory >=0:
      return f"Turn on your phone to install {app}"

    return f"Not enough memory to install {app}"


  def status(self):
    return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
