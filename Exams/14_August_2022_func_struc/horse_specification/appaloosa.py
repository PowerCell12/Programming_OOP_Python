from project.horse_specification.horse import  Horse

class Appaloosa(Horse):

    MAX = 120

    def __init__(self, name, speed):
        super().__init__(name, speed)


    def train(self):

        self.speed =  self.MAX if self.speed  + 2  > self.MAX else self.speed + 2
