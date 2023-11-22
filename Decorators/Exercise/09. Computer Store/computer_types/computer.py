from abc import ABC, abstractmethod

class Computer(ABC):

    def __init__(self, manufacturer, model):
        if manufacturer.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")
        self.manufacturer = manufacturer
        if model.strip() == "":
            raise ValueError("Model name cannot be empty.")
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0


    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        pass


    def __repr__(self):
        return f"{self.manufacturer} { self.model } with { self.processor } and { self.ram }GB RAM"