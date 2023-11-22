from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        processors = {"AMD Ryzen 7 5700G": 500, "Intel Core i5-12600K": 600, "Apple M1 Max": 1800}
        on_the_power_of_2 = {2: 100, 4: 200, 8: 300, 16: 400, 32: 500, 64: 600, 128: 700}

        max_ram = 128

        if processor not in processors.keys():
             raise ValueError(f"{ processor } is not compatible with desktop computer { self.manufacturer  } { self.model}!")

        if ram not in on_the_power_of_2.keys() or ram > max_ram:
             raise ValueError(f"{ ram }GB RAM is not compatible with desktop computer { self.manufacturer  } { self.model  }!")


        price = on_the_power_of_2[ram]  + processors[processor]
        self.price = price
        self.processor = processor
        self.ram = ram



        return f"Created { self.manufacturer } { self.model  } with { processor} and { ram }GB RAM for {  price }$."