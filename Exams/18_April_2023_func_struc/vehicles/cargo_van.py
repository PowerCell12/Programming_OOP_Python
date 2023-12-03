from project.vehicles.base_vehicle import BaseVehicle

class CargoVan(BaseVehicle):

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, 180.00)


    def drive(self, mileage: float):
        percentage  = mileage / self.max_mileage * 100
        percentage_final = round(percentage)

        percentage_final += 5
        self.battery_level -= percentage_final
