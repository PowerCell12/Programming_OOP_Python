from project.vehicles.base_vehicle import BaseVehicle

class PassengerCar(BaseVehicle):

    def __init__(self,  brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, 450.00)



    def drive(self, mileage: float): ## if error check
        percentage  = mileage / self.max_mileage * 100
        percentage_final = round(percentage)

        self.battery_level -= percentage_final

