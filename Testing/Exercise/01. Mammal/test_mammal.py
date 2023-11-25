import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):

    def setUp(self):
        self.mammal = Mammal("buldog", "dog", "woof")

    def test_initializing(self):
        self.assertEqual(self.mammal.name, "buldog")
        self.assertEqual(self.mammal.type, "dog")
        self.assertEqual(self.mammal.sound, "woof")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), "buldog makes woof")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info(self):
        self.assertEqual(self.mammal.info(), "buldog is of type dog")


if __name__ == "__main__":
    unittest.main()
