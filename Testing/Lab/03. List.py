import unittest

class TestIntegers(unittest.TestCase):

    def setUp(self):
        self.integerlist = IntegerList(1, 2, 3, False, 2.4)


    def test_initializing(self):
        self.assertEqual(self.integerlist._IntegerList__data, [1, 2, 3])


    def test_get_data(self):
        data = self.integerlist.get_data()
        self.assertEqual(data, self.integerlist._IntegerList__data)

    def test_add_error_if_not_int(self):

        with self.assertRaises(ValueError) as vl:
            self.integerlist.add(True)

        self.assertEqual(str(vl.exception), "Element is not Integer")


    def test_add_appending(self):
        self.integerlist.add(4)
        self.assertEqual(self.integerlist._IntegerList__data, [1, 2, 3, 4])

    def test_add_return(self):
        self.assertEqual(self.integerlist.add(4), [1, 2, 3, 4])


    def test_remove_index_if_bigger_index(self):
        with self.assertRaises(IndexError) as ix:
            self.integerlist.remove_index(3)

        self.assertEqual(str(ix.exception), "Index is out of range")

    def test_remove_index_del_index(self):
        self.integerlist.remove_index(2)
        self.assertEqual(self.integerlist._IntegerList__data, [1, 2])


    def test_remove_index_return(self):
        first = self.integerlist.remove_index(2)
        self.assertEqual(first, 3)


    def test_get_if_index_bigger_than_length(self):
        with self.assertRaises(IndexError) as ir:
            self.integerlist.get(3)

        self.assertEqual(str(ir.exception), "Index is out of range")

    def test_get_return(self):
        first = self.integerlist.get(1)
        self.assertEqual(first, 2)


    def test_insert_if_index_is_bigger(self):
        with self.assertRaises(IndexError) as ix:
            self.integerlist.insert(3, 4)

        self.assertEqual(str(ix.exception), "Index is out of range")


    def test_insert_if_type_is_other_than_integer(self):
        with self.assertRaises(ValueError) as vl:
            self.integerlist.insert(1, True)

        self.assertEqual(str(vl.exception), "Element is not Integer")


    def test_insert_return(self):
        self.integerlist.insert(2, 4)
        self.assertEqual(self.integerlist._IntegerList__data, [1, 2, 4, 3])

    def test_get_biggest_return(self):
        self.assertEqual(self.integerlist.get_biggest(), 3)


    def test_get_index_return(self):
        self.assertEqual(self.integerlist.get_index(1), 0)


if __name__ == '__main__':
    unittest.main()
