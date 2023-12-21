from project.horse_specification.horse import Horse

class Thoroughbred(Horse):

    MAX = 140

    def __init__(self, name, speed):
        super().__init__(name, speed)


    def train(self):
        self.speed = self.MAX if self.speed + 3 > self.MAX else self.speed + 3
