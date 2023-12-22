import unittest

from project.bookstore import Bookstore


class Test_Bookstore(unittest.TestCase):

    def setUp(self):
        self.bookstore = Bookstore(10)

    def test__init__(self):
        self.assertEqual(self.bookstore.books_limit, 10)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bookstore._Bookstore__total_sold_books, 0)

    def test_property_for_total_sold_books(self):
        self.assertEqual(self.bookstore._Bookstore__total_sold_books, 0)

    def test_property_for_books_limit(self):
        self.assertEqual(self.bookstore.books_limit, 10)


    def test_setter_for_books_limit_no_error(self):
        self.bookstore.books_limit = 5
        self.assertEqual(self.bookstore.books_limit, 5)


    def test_setter_for_books_limit_error(self):
        with self.assertRaises(ValueError) as ex:
            self.bookstore.books_limit = 0

        self.assertEqual(str(ex.exception), f"Books limit of 0 is not valid")

    def test_len_function(self):
        self.bookstore.receive_book("title", 10)
        self.assertEqual(len(self.bookstore), 10)

    def test_receive_book_if_no_space(self):

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("title", 11)

        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

    def test_if_receive_books_create_a_new_availability_in_store_by_book_titles_and_output(self):
        self.bookstore.receive_book("title", 10)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"title": 10})
        self.assertEqual(self.bookstore.receive_book("title", 10), "10 copies of title are available in the bookstore.")

    def test_sell_book_error_if_book_not_in_titles(self):

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("title", 1)

        self.assertEqual(str(ex.exception), "Book title doesn't exist!")

    def test_is_there_arent_enough_copies(self):
        self.bookstore.receive_book("title", 10)

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("title", 11)

        self.assertEqual(str(ex.exception), "title has not enough copies to sell. Left: 10")

    def test_sell_book_output_and_other_things(self):
        self.bookstore.receive_book("title", 10)
        self.assertEqual(self.bookstore.sell_book("title", 5), "Sold 5 copies of title")
        self.bookstore.sell_book("title", 5)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles["title"], 0)
        self.assertEqual(self.bookstore._Bookstore__total_sold_books, 10)

    def test__str__(self):
        self.bookstore.receive_book("title", 10)
        self.assertEqual(str(self.bookstore), "Total sold books: 0\nCurrent availability: 10\n - title: 10 copies")


if __name__ == "__main__":
    unittest.main()