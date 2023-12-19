from project.shopping_cart import ShoppingCart
import unittest

class Test_ShoppingCart(unittest.TestCase):

    def setUp(self):
        self.shopping_cart = ShoppingCart("TestShop", 100.0)

    def test_init(self):
        self.assertEqual("TestShop", self.shopping_cart.shop_name)
        self.assertEqual(100.0, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)


    def test_shop_name_setter_fail(self): ## if error see

        with self.assertRaises(ValueError) as vl:
            self.shopping_cart.shop_name = "testShop"

        with self.assertRaises(ValueError) as vl1:
            self.shopping_cart.shop_name = "Test_Shop"

        self.assertEqual(str(vl.exception), "Shop must contain only letters and must start with capital letter!")
        self.assertEqual(str(vl1.exception), "Shop must contain only letters and must start with capital letter!")


    def test_shop_name_setter_success(self):
        self.shopping_cart.shop_name = "TestShoP"
        self.assertEqual("TestShoP", self.shopping_cart.shop_name)


    def test_add_to_cart_if_price_over_or_equal_100(self):
        with self.assertRaises(ValueError) as vl:
            self.shopping_cart.add_to_cart("test", 100.0)

        self.assertEqual(str(vl.exception), "Product test cost too much!")


    def test_add_to_cart_success(self):
        self.assertEqual(self.shopping_cart.add_to_cart("test", 90), "test product was successfully added to the cart!")
        self.assertEqual(self.shopping_cart.products, {"test": 90})


    def test_remove_from_cart_if_product_in(self):
        self.shopping_cart.products["test"] = 100
        self.shopping_cart.products["test2"] = 90
        self.assertEqual(self.shopping_cart.remove_from_cart("test"), "Product test was successfully removed from the cart!")
        self.assertEqual(self.shopping_cart.products, {"test2": 90})


    def test_remove_from_cart_if_not_in(self):

        with self.assertRaises(ValueError) as vl:
            self.shopping_cart.remove_from_cart("test")

        self.assertEqual(str(vl.exception), "No product with name test in the cart!")


    def test_add_return(self): ## this
        new_cart = ShoppingCart("CaffeShop", 200)
        new_cart.products["test"] = 100
        self.shopping_cart.products["test2"] = 90
        result = new_cart + self.shopping_cart
        anotherone = ShoppingCart("CaffeShopTestShop", 300.0)
        anotherone.products["test"] = 100
        anotherone.products["test2"] = 90
        self.assertEqual(result.shop_name, anotherone.shop_name)
        self.assertEqual(result.budget, anotherone.budget)
        self.assertEqual(result.products, anotherone.products)


    def test_buy_product_error(self):
        self.shopping_cart.add_to_cart("test", 90)
        self.shopping_cart.add_to_cart("test2", 80)
        with self.assertRaises(ValueError) as vl:
            self.shopping_cart.buy_products()

        self.assertEqual(str(vl.exception), "Not enough money to buy the products! Over budget with 70.00lv!")


    def test_buy_product_success(self):
        self.shopping_cart.add_to_cart("test", 90)
        self.assertEqual(self.shopping_cart.buy_products(), "Products were successfully bought! Total cost: 90.00lv.")



if __name__ == "__main__":
    unittest.main()