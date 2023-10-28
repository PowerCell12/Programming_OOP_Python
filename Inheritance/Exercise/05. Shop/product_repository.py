from project.product import  Product

class ProductRepository:

    def __init__(self):
        self.products = []


    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):

        for product in self.products:

            if product.name == product_name:
                return product


    def remove(self, product_name):

        for product in self.products:

            if product.name == product_name:
                self.products.remove(product)
                break ## maybe error


    def __repr__(self):
        string = ""

        for i in range(len(self.products)):
            product = self.products[i]


            if i != len(self.products) - 1:
                string += f"{product.name}: {product.quantity}\n"
            else:
                string += f"{product.name}: {product.quantity}"

        return string
