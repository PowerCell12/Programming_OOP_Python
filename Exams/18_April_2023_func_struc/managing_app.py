from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []



    def register_user(self, first_name: str, last_name: str, driving_license_number: str):

        if driving_license_number in [h.driving_license_number for h in self.users]:
            return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"


    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        if vehicle_type != "PassengerCar" and vehicle_type != "CargoVan":
             return f"Vehicle type {vehicle_type} is inaccessible."

        if license_plate_number in [h.license_plate_number for h in self.vehicles]:
            return f"{license_plate_number} belongs to another vehicle."


        if vehicle_type == "PassengerCar":
            self.vehicles.append(PassengerCar(brand, model, license_plate_number))
        elif vehicle_type == "CargoVan":
            self.vehicles.append(CargoVan(brand, model, license_plate_number))

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."



    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1

        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."


        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."



        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                 route.is_locked = True


        self.routes.append(Route(start_point, end_point, length, route_id))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."



    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):

        vehicle = None
        user = None
        route = None

        for us in self.users:
            if us.driving_license_number == driving_license_number:
                user = us
                break

        for veh in self.vehicles:
            if veh.license_plate_number == license_plate_number:
                vehicle = veh
                break

        for r in self.routes:
            if r.route_id == route_id:
                route = r
                break


        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)



    def repair_vehicles(self, count: int):
        all_damaged = [h for h in self.vehicles if h.is_damaged]

        sorted_all_damaged = sorted(all_damaged, key= lambda  x: (x.brand, x.model))

        count1 = 0
        for i in range(count):

            if i == len(sorted_all_damaged):
                break

            count1 += 1

            sorted_all_damaged[i].is_damaged = False
            sorted_all_damaged[i].battery_level = 100

        return f"{count1} vehicles were successfully repaired!"


    def users_report(self):
        list_final = []

        users = sorted(self.users, key=lambda  x: -x.rating)

        list_final.append(f"*** E-Drive-Rent ***")
        for user in users:
            list_final.append(str(user))

        return "\n".join(list_final)
