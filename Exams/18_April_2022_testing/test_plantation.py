from project.plantation import Plantation
import unittest

class Test_Plantation(unittest.TestCase):

    def setUp(self):
        self.plantation = Plantation(5)

    def test_init(self):
        self.assertEqual(5, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)


    def test_size_setter_failure(self):
        with self.assertRaises(ValueError) as vl:
            self.plantation.size = -1

        self.assertEqual(str(vl.exception), "Size must be positive number!")

    def test_size_setter_success(self):
        self.plantation.size = 10
        self.assertEqual(10, self.plantation.size)


    def test_hire_worker_failure(self):
        self.plantation.workers.append("Ivan")
        with self.assertRaises(ValueError) as vl:
            self.plantation.hire_worker("Ivan")

        self.assertEqual(str(vl.exception), "Worker already hired!")


    def test_hire_worker_success(self):
        self.assertEqual(self.plantation.hire_worker("Ivan"), "Ivan successfully hired.")
        self.assertEqual(self.plantation.workers, ["Ivan"])


    def test_len(self):
        self.plantation.plants["Plant"] = ["A", "B", "C"]
        self.plantation.plants["Plant2"] = ["D", "E"]
        self.assertEqual(5, len(self.plantation))


    def test_planting_worker_not_in(self):
        with self.assertRaises(ValueError) as vl:
            self.plantation.planting("Ivan", "A")

        self.assertEqual(str(vl.exception), "Worker with name Ivan is not hired!")


    def test_planting_if_more_than(self):
        self.plantation.plants["Plant"] = ["A", "B", "C"]
        self.plantation.plants["Plant2"] = ["D", "E"]
        self.plantation.workers.append("Ivan")
        with self.assertRaises(ValueError) as vl:
            self.plantation.planting("Ivan", "A")

        self.assertEqual(str(vl.exception), "The plantation is full!")



    def test_planting_if_worker_in_plants_keys(self):
        self.plantation.workers.append("Plant")
        self.plantation.plants["Plant"] = ["A", "B", "C"]
        self.assertEqual(self.plantation.planting("Plant", "3"), "Plant planted 3.")
        self.assertEqual(self.plantation.plants["Plant"], ["A", "B", "C", "3"])


    def test_planting_if_worker_not_in_plants_Keys(self):
        self.plantation.workers.append("Ivan")
        self.assertEqual(self.plantation.planting("Ivan", "3"), "Ivan planted it's first 3.")
        self.assertEqual(self.plantation.plants["Ivan"], ["3"])


    def test_str(self):
        self.plantation.workers.append("Ivan")
        self.plantation.workers.append("Peter")
        self.plantation.plants["Plant"] = ["A", "B", "C"]
        self.plantation.plants["Plant2"] = ["D", "E"]
        self.assertEqual(self.plantation.__str__(), "Plantation size: 5\nIvan, Peter\nPlant planted: A, B, C\nPlant2 planted: D, E")


    def test_repr(self):
        self.plantation.workers.append("Ivan")
        self.plantation.workers.append("Peter")
        self.assertEqual(self.plantation.__repr__(), "Size: 5\nWorkers: Ivan, Peter")


if __name__ == "__main__":
    unittest.main()
