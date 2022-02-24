import pytest

from XAMS.Product.Product.filing import Filing
from XAMS.Product.Product.revenue_product import RevenueProduct
from XAMS.Product.Product.series import Series
from XAMS.Product.Product.valuation_product import ValuationProduct
from XAMS.Report.conftest import sheet54, sheet55, sheet56, sheet57
from XAMS.Tool.test_excel import TestExcel


class TestProduct:
    # 万能导入用例
    def test_universal(self, stagemark, menu, value, test_goal, step):
        self.list = TestExcel()
        if test_goal == '模拟操作':
            second_menu = f'{menu[1]}-{menu[2]}'
            address = value[0]
            if second_menu == '产品管理-产品系列定义':
                self.test_series_excel(stagemark, menu, value, address, step)
            elif second_menu == '产品管理-产品报备管理':
                self.test_filing_excel(stagemark, menu, value, address, step)
            elif second_menu == '产品管理-收益型产品信息管理':
                self.test_revenue_product_excel(stagemark, menu, value, address, step)
            elif second_menu == '产品管理-净值型产品信息管理':
                self.test_valuation_product_excel(stagemark, menu, value, address, step)
            else:
                print("模拟操作案例：该产品暂不支持，请修改用例")
        elif test_goal == '升级对比':
            second_menu = f'{menu[2]}-{menu[3]}'
            address = value[0]
        else:
            print("该测试目的暂不支持，请修改用例")
            return False

    @pytest.mark.skip
    def test_series_excel(self, stagemark, menu, value, address, step):
        self.series = Series(address)
        assert self.series.series_excel(menu, value)
        if step is not None:
            self.series.end()
        print(f"{sheet54}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_filing_excel(self, stagemark, menu, value, address, step):
        self.filing = Filing(address)
        assert self.filing.filing_excel(menu, value)
        if step is not None:
            self.filing.end()
        print(f"{sheet55}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_revenue_product_excel(self, stagemark, menu, value, address, step):
        self.revenue_product = RevenueProduct(address)
        assert self.revenue_product.revenue_product_excel(menu, value)
        if step is not None:
            self.revenue_product.end()
        print(f"{sheet56}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_valuation_product_excel(self, stagemark, menu, value, address, step):
        self.valuation_product = ValuationProduct(address)
        assert self.valuation_product.valuation_product_excel(menu, value)
        if step is not None:
            self.valuation_product.end()
        print(f"{sheet57}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')
