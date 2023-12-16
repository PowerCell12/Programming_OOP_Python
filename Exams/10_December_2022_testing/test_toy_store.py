from project.toy_store import ToyStore
import unittest

class Test_toy_store(unittest.TestCase):

    def setUp(self):
        self.toy_store = ToyStore()


    def test_init(self):
        self.assertEqual(self.toy_store.toy_shelf, {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None})


    def test_add_toy_if_shelf_not_in_keys(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("Z", "pesho")

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")


    def test_add_toy_if_toy_already_in(self):
        self.toy_store.toy_shelf["A"] = "pesho"

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "pesho")

        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_if_toy_already_in_but_other_toy(self):
        self.toy_store.toy_shelf["A"] = "viktor"

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "pesho")

        self.assertEqual(str(ex.exception), "Shelf is already taken!")


    def test_if_add_toy_successful(self):
        self.assertEqual(self.toy_store.add_toy("A", "pesho"), "Toy:pesho placed successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {'A': 'pesho', 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None})


    def test_if_remove_toy_shelf_not_in_keys(self):

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("Z", "pesho")

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")


    def test_if_remove_toy_name_not_true(self):
        self.toy_store.toy_shelf["A"] = "pesho"

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "viktor")

        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")


    def test_if_remove_toy_successful(self):
        self.toy_store.toy_shelf["A"] = "pesho"

        self.assertEqual(self.toy_store.remove_toy("A", "pesho"), "Remove toy:pesho successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None})



if __name__ == "__main__":
    unittest.main()