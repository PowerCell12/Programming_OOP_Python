from project.computer_types.computer import Computer


class Laptop(Computer):

    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        processors = {"AMD Ryzen 9 5950X": 900, "Intel Core i9-11900H": 1050, "Apple M1 Pro": 1200}
        on_the_power_of_2 = {2: 100, 4: 200, 8: 300, 16: 400, 32: 500, 64: 600}

        max_ram = 64

        if processor not in processors.keys():
             raise ValueError(f"{ processor } is not compatible with laptop { self.manufacturer} { self.model}!")

        if ram not in on_the_power_of_2 or ram > max_ram:
             raise ValueError(f"{ ram }GB RAM is not compatible with laptop { self.manufacturer } { self.model }!")


        price = on_the_power_of_2[ram]  + processors[processor]
        self.price = price
        self.processor = processor
        self.ram = ram



        return f"Created { self.manufacturer  } { self.model  } with { processor } and { ram }GB RAM for {  price }$."