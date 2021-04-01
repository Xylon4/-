from product import Product


class TestProduct:
    def teardown(self):
        self.product.end()

    def test_product(self, stagemark):
        self.product = Product()
        assert self.product.product1()
