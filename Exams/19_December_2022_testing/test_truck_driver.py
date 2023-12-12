from project.truck_driver import TruckDriver
import unittest

class Test_TruckDriver(unittest.TestCase):

    def setUp(self):
        self.truck_driver = TruckDriver("Bob", 100)

    def test_init(self):
        self.assertEqual("Bob", self.truck_driver.name)
        self.assertEqual(100, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)


    def test_earned_money_setter_failure(self):
        with self.assertRaises(ValueError) as vl:
            self.truck_driver.earned_money = -1

        self.assertEqual(str(vl.exception), "Bob went bankrupt.")

    def test_earned_money_setter_success(self):
        self.truck_driver.earned_money = 101
        self.assertEqual(101, self.truck_driver.earned_money)


    def test_add_cargo_offer_if_cargo_in_available_cargos(self):
        self.truck_driver.available_cargos["cargo"] = 1
        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("cargo", 1)

        self.assertEqual(str(ex.exception), "Cargo offer is already added.")


    def test_add_cargo_offer_success(self):
        self.assertEqual("Cargo for 1 to cargo was added as an offer.", self.truck_driver.add_cargo_offer("cargo", 1))
        self.assertEqual(self.truck_driver.available_cargos, {"cargo": 1})


    def test_drive_best_cargo_offer_value_error(self):
        self.assertEqual("There are no offers available.", self.truck_driver.drive_best_cargo_offer())


    def test_drive_best_cargo_offer(self):
        self.truck_driver.available_cargos["cargo"] = 10
        self.truck_driver.available_cargos["cargo2"] = 10000
        self.assertEqual("Bob is driving 10000 to cargo2.", self.truck_driver.drive_best_cargo_offer())
        self.assertEqual(self.truck_driver.earned_money, 988250)
        self.assertEqual(self.truck_driver.miles, 10000)

    def test_check_for_activies(self):
        self.truck_driver.earned_money = 100000
        self.truck_driver.check_for_activities(10000)
        self.assertEqual(self.truck_driver.earned_money, 88250)

    def test_repr(self):
        self.truck_driver.miles = 100
        self.assertEqual(self.truck_driver.__repr__(), "Bob has 100 miles behind his back.")




if __name__ == '__main__':
    unittest.main()