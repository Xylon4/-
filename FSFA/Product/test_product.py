import pytest

from cash_flow import CashFlow
from product import Product
from product_manage import ProductManage


class TestProduct:
    def setup(self):
        self.product = Product()
        self.product_manage = ProductManage()
        self.cash_flow = CashFlow()

    def teardown(self):
        self.product.end()

    # @pytest.mark.skip
    def test_product(self, stagemark):
        assert self.product.product1()

    # @pytest.mark.skip
    def test_product_manage(self, stagemark):
        assert self.product_manage.productmanage1()

    def test_cash_flow(self, stagemark):
        assert self.cash_flow.cashflow1()
