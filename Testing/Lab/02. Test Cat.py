import unittest


class CatTests(unittest.TestCase):

    def setUp(self):
        self.cat = Cat("Fido")


    def  test_cat_increase_after_eating(self): ##right
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)


    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)


    def test_cat_cannot_eat_after_eating(self): ## right
        self.cat.fed = True

        with self.assertRaises(Exception) as e:
            self.cat.eat()

        self.assertEqual(str(e.exception), 'Already fed.')


    def test_cannot_fall_asleep_if_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')


    def test_cat_not_sleepy_after_sleeping(self):
        self.cat.fed = True
        self.cat.sleepy = True
        
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()
