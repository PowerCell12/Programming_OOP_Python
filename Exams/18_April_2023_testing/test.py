from project.robot import Robot
import unittest

class Test_Robot(unittest.TestCase):

    def setUp(self):
        self.robot = Robot("12", "Education", 10, 10)

    def test_unit(self):
        self.assertEqual(self.robot.robot_id, "12")
        self.assertEqual(self.robot.category, "Education")
        self.assertEqual(self.robot.available_capacity, 10)
        self.assertEqual(self.robot.price, 10)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])


    def test_robot_class_attributs(self):
        self.assertEqual(self.robot.PRICE_INCREMENT, 1.5)
        self.assertEqual(self.robot.ALLOWED_CATEGORIES, ['Military', 'Education', 'Entertainment', 'Humanoids'])



    def test_setter_failure(self):

        with self.assertRaises(ValueError) as vl:
            self.robot.category = "What is this"

        self.assertEqual(str(vl.exception), "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")


    def test_setter_success(self):
        self.robot.category = "Military"
        self.assertEqual(self.robot.category, "Military")



    def test_price_setter_failure(self):
        with self.assertRaises(ValueError) as vl:
            self.robot.price = -1

        self.assertEqual(str(vl.exception), "Price cannot be negative!")


    def test_price_setter_success(self):
        self.robot.price = 10
        self.assertEqual(self.robot.price, 10)


    def test_upgrade_if_hard_in(self):
        self.robot.hardware_upgrades.append("Hard")
        self.assertEqual(self.robot.upgrade("Hard", 10), "Robot 12 was not upgraded.")


    def test_upgrade_success(self):
        self.assertEqual(self.robot.upgrade('Hard', 15), "Robot 12 was upgraded with Hard.")
        self.assertEqual(self.robot.hardware_upgrades, ['Hard'])
        self.assertEqual(self.robot.price, 32.5)


    def test_update_if_capacity_lower(self):
        self.assertEqual(self.robot.update(1.5, 11), "Robot 12 was not updated.")
        self.robot.software_updates.append(1.5)
        self.assertEqual(self.robot.update(1.5, 5), "Robot 12 was not updated.")


    def test_update_success(self):
        self.assertEqual(self.robot.update(1.5, 5), "Robot 12 was updated to version 1.5.")
        self.assertEqual(self.robot.available_capacity, 5)
        self.assertEqual(self.robot.software_updates, [1.5])


    def test_gt_if_bigger(self):
        other = Robot("13", "Education", 10, 5)
        self.assertEqual(self.robot > other, "Robot with ID 12 is more expensive than Robot with ID 13.")


    def test_gt_equal(self):
        other = Robot("13", "Education", 10, 10)
        self.assertEqual(self.robot > other, "Robot with ID 12 costs equal to Robot with ID 13.")


    def test_gt_lower(self):
        other = Robot("13", "Education", 10, 50)
        self.assertEqual(self.robot > other, "Robot with ID 12 is cheaper than Robot with ID 13.")


if __name__ == "__main__":
    unittest.main()