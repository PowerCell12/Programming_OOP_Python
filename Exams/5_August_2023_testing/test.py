from project.second_hand_car import SecondHandCar
import unittest

class Test_SecondHandCar(unittest.TestCase):


    def setUp(self):
        self.hand_car = SecondHandCar('Toyota', 'Corolla', 110, 1000)


    def test_init(self):
        self.assertEqual(self.hand_car.model, 'Toyota')
        self.assertEqual(self.hand_car.car_type, 'Corolla')
        self.assertEqual(self.hand_car.mileage, 110)
        self.assertEqual(self.hand_car.price, 1000)
        self.assertEqual(self.hand_car.repairs, [])

    def test_setter_price_error(self):
        with self.assertRaises(ValueError) as vl:
            self.hand_car.price = 1.0

        self.assertEqual(str(vl.exception), 'Price should be greater than 1.0!')


    def test_setter_success_price(self):
        self.hand_car.price = 2000
        self.assertEqual(self.hand_car.price, 2000)


    def test_setter_mileage_error(self):
        with self.assertRaises(ValueError) as vl:
            self.hand_car.mileage = 100

        self.assertEqual(str(vl.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_setter_mileage_success(self):
        self.hand_car.mileage = 200
        self.assertEqual(self.hand_car.mileage, 200)


    def test_set_promotion_erorr(self):
        with self.assertRaises(ValueError) as vl:
            self.hand_car.set_promotional_price(1000)

        self.assertEqual(str(vl.exception), 'You are supposed to decrease the price!')


    def test_set_promotion_success(self):
        self.assertEqual(self.hand_car.set_promotional_price(500), 'The promotional price has been successfully set.')
        self.assertEqual(self.hand_car.price, 500)


    def test_need_repair_impossible(self):
        self.assertEqual(self.hand_car.need_repair(501, "this"), 'Repair is impossible!')


    def test_need_repair_success(self):
        self.assertEqual(self.hand_car.need_repair(500, "this"), 'Price has been increased due to repair charges.')
        self.assertEqual(self.hand_car.price, 1500)
        self.assertEqual(self.hand_car.repairs, ['this'])


    def test_gr_cannot(self):
        other = SecondHandCar('Mercedes', 'Corolla2', 110, 1000)
        self.assertEqual(self.hand_car > other, "Cars cannot be compared. Type mismatch!")


    def test_gt_bigger_price(self):
        other = SecondHandCar('Toyota', 'Corolla', 110, 200)
        self.assertEqual(self.hand_car > other, True)

    def test_gt_lower_price(self):
        other=  SecondHandCar('Toyota', 'Corolla', 110, 1005)
        self.assertEqual(self.hand_car > other, False)


    def test_str(self):
        self.hand_car.repairs.append("this")
        self.hand_car.repairs.append("that")
        self.assertEqual(str(self.hand_car), "Model Toyota | Type Corolla | Milage 110km\nCurrent price: 1000.00 | Number of Repairs: 2")


if __name__ == '__main__':
    unittest.main()