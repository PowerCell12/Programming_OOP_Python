from project.services.base_service import BaseService

class SecondaryService(BaseService):

    def __init__(self, name):
        super().__init__(name, 15)


    def details(self):
        to_return = []
        to_return.append(f"{self.name} Secondary Service:")
        if self.robots:
            to_return.append(f"Robots: {' '.join([rob.name for rob in self.robots])}")
        else:
            to_return.append("Robots: none")

        return '\n'.join(to_return)
