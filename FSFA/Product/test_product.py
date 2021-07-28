# from encodings import gbk

import pytest

from cash_flow import CashFlow
from product import Product
from product_manage import ProductManage

# coding = gbk


class TestProduct:
    def teardown(self):
        pass

    @pytest.mark.skip
    def test_product(self, get_product, stagemark):
        self.product = Product()
        assert self.product.product1(get_product)
        self.product.end()

    # @pytest.mark.skip
    def test_product_manage(self, get_product_manage, stagemark):
        self.product_manage = ProductManage()
        assert self.product_manage.productmanage1(get_product_manage)
        self.product_manage.end()

    @pytest.mark.skip
    def test_cash_flow(self, stagemark):
        self.cash_flow = CashFlow()
        assert self.cash_flow.cashflow1()
        self.cash_flow.end()
