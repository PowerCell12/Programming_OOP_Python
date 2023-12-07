from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    def __init__(self):
        self.robots = []
        self.services = []


    def add_service(self, service_type: str, name: str):

        if service_type != "MainService" and service_type != "SecondaryService":
            raise Exception("Invalid service type!")

        if service_type == "MainService":
            self.services.append(MainService(name))
        elif service_type == "SecondaryService":
            self.services.append(SecondaryService(name))

        return f"{service_type} is successfully added."


    def add_robot(self, robot_type: str, name: str, kind: str, price: float):

        if robot_type != "MaleRobot" and robot_type != "FemaleRobot":
            raise Exception("Invalid robot type!")

        if robot_type == "MaleRobot":
            self.robots.append(MaleRobot(name, kind, price))
        elif robot_type == "FemaleRobot":
            self.robots.append(FemaleRobot(name, kind, price))

        return f"{robot_type} is successfully added."


    def add_robot_to_service(self, robot_name: str, service_name: str):

        robot = None
        service = None

        for rob in self.robots:
            if rob.name == robot_name:
                robot = rob
                break

        for ser in self.services:
            if ser.name == service_name:
                service = ser
                break

        if robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "MainService": ## if erorr check
            return "Unsuitable service."
        elif robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "SecondaryService": ## if error check
            return "Unsuitable service."

        ## if not enough capactiy
        if service.capacity - len(service.robots) < 1: ## wtf check if error
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."



    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = None

        for ser in self.services:
            if ser.name == service_name:
                service = ser
                break

        if robot_name not in [h.name for h in service.robots]:
            raise Exception("No such robot in this service!")

        robot = None
        for rob in service.robots:
            if rob.name == robot_name:
                robot = rob
                break

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."



    def feed_all_robots_from_service(self, service_name: str):
        service = None
        for ser in self.services:
            if ser.name == service_name:
                service = ser
                break

        for rob in service.robots:
            rob.eating()

        return f"Robots fed: {len(service.robots)}."


    def service_price(self, service_name: str):
        service = None
        for ser in self.services:
            if ser.name == service_name:
                service = ser
                break

        total = 0
        for rob in service.robots:
            total += rob.price

        return f"The value of service {service_name} is {total:.2f}."


    def __str__(self):
        list_return = []
        for ser in self.services:
            list_return.append(ser.details())

        return '\n'.join(list_return)
