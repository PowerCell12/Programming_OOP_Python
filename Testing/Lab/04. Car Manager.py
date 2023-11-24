import unittest


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car("tesla", "model a", 2, 4)

    def test_the__init__(self):
        self.assertEqual(self.car.make, "tesla")
        self.assertEqual(self.car.model, "model a")
        self.assertEqual(self.car.fuel_consumption, 2)
        self.assertEqual(self.car.fuel_capacity, 4)
        self.assertEqual(self.car.fuel_amount, 0)


    def test_make_property(self):
        self.assertEqual(self.car.make, "tesla")

    def test_make_setter_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_make_setter(self):
        self.car.make = "teslaX"
        self.assertEqual(self.car.make, "teslaX")


    def test_model_property(self):
        self.assertEqual(self.car.model, "model a")


    def test_model_setter_error(self):

        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_model_setter(self):
        self.car.model = "model b"
        self.assertEqual(self.car.model, "model b")


    def test_fuel_consumption_property(self):
        self.assertEqual(self.car.fuel_consumption, 2)

    def test_fuel_consumption_setter_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_consumption_setter(self):
        self.car.fuel_consumption = 1
        self.assertEqual(self.car.fuel_consumption, 1)


    def test_fuel_capacity_property(self):
        self.assertEqual(self.car.fuel_capacity, 4)


    def test_fuel_capacity_setter_error(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")


    def test_fuel_capacity_setter(self):
        self.car.fuel_capacity = 1
        self.assertEqual(self.car.fuel_capacity, 1)


    def test_fuel_amount_property(self):
        self.assertEqual(self.car.fuel_amount, 0)

    def test_fuel_amount_setter_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount  = -1

        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_fuel_amount_setter(self):
        self.car.fuel_amount = 0
        self.assertEqual(self.car.fuel_amount, 0)


    def test_refuel_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")


    def test_refuel_fuel_amount_raising(self):
        self.car.refuel(1)
        self.assertEqual(self.car.fuel_amount, 1)

    def test_refuel_if_fuel_amount_is_bigger_than_fuel_capacity(self):
        self.car.refuel(5)

        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)


    def test_drive_error(self):

        with self.assertRaises(Exception) as ex:
            self.car.drive(1)

        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_drive_fuel_amount_subtraction(self):
        self.car.fuel_amount = 12
        self.car.drive(12)

        self.assertEqual(self.car.fuel_amount, 11.76)


if __name__ == "__main__":
    unittest.main()
