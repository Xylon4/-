import pytest

from cash_flow import CashFlow
from product import Product
from product_manage import ProductManage


class TestProduct:
    def teardown(self):
        pass
        # self.product.end()

    # @pytest.mark.skip
    def test_product(self, stagemark):
        self.product = Product()
        assert self.product.product1()

    # @pytest.mark.skip
    def test_product_manage(self, stagemark):
        self.product_manage = ProductManage()
        assert self.product_manage.productmanage1()

    def test_cash_flow(self, stagemark):
        self.cash_flow = CashFlow()
        assert self.cash_flow.cashflow1()