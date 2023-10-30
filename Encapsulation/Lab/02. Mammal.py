class Mammal:

    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    __kingdom = "animals"

    def make_sound(self):
        return f"{self.name} makes {self.sound}"
    
    def get_kingdom(self):
        return Mammal.__kingdom
    
    def info(self):
        return f"{self.name} is of type {self.type}"
