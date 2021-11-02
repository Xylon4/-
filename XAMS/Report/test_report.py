import pytest
import xlrd

from XAMS.Report.Finance.valuation import Valuation
from XAMS.Report.Financial.Asset_pool_registry import AssetPoolRegistry
from XAMS.Report.Financial.product import Product
from XAMS.Report.conftest import Excel_basedata, Excel_custom, sheet1, sheet2, sheet3, sheet4
from XAMS.Tool.test_excel import TestExcel
from XAMS.conftest import stagemark


class TestReport:
    # 万能导入用例
    def test_universal(self):
        self.list = TestExcel()
        count = len(self.list.code_list())
        n = 0
        while n < count:
            code = self.list.code_list()[n]
            menu = self.list.group_ele_dic().get(code)
            value = self.list.group_value_dic().get(code)
            second_menu = f'{menu[0]}-{menu[1]}'
            if second_menu == '估值管理-估值表':
                self.test_valuation_excel(stagemark, menu, value)
            n = n + 1
        print(f'自动化案例执行完毕，共{count}条')

    @pytest.mark.skip
    # 根据excel导入内容选择执行案例
    def test_option(self):
        # 打开excel文件
        excel = xlrd.open_workbook(Excel_basedata)
        # 获取sheet，通过Excel表格名称()获取工作表
        S1 = excel.sheet_by_name(f'{sheet1}')
        S2 = excel.sheet_by_name(f'{sheet2}')
        S3 = excel.sheet_by_name(f'{sheet3}')
        # 校验工作表数据(统计操作列表中"1"的重复次数)
        self.list = TestExcel()
        count1 = self.list.registry_list().count(1)
        count2 = self.list.product_list().count(1)
        while count1 > 0:
            self.test_registry_excel(stagemark)
            count1 = 0
        while count2 > 0:
            self.test_product_excel(stagemark)
            count2 = 0
        else:
            print("没有可运行的数据")

    @pytest.mark.skip
    def test_asset_pool_registry(self, get_registry, stagemark):
        self.asset_pool_registry = AssetPoolRegistry()
        assert self.asset_pool_registry.registry(get_registry)
        print(f"{sheet1}测试通过")
        self.asset_pool_registry.end()

    @pytest.mark.skip
    def test_product(self, stagemark):
        self.product = Product()
        assert self.product.product()
        print(f"{sheet2}测试通过")
        self.product.end()

    @pytest.mark.skip
    def test_registry_excel(self, stagemark):
        self.asset_pool_registry = AssetPoolRegistry()
        assert self.asset_pool_registry.registry_excel()
        print(f"{sheet1}自动化操作执行完毕")

    @pytest.mark.skip
    def test_product_excel(self, stagemark):
        self.product = Product()
        assert self.product.product_excel()
        print(f"{sheet2}自动化操作执行完毕")

    @pytest.mark.skip
    def test_valuation_excel(self, stagemark, menu, value):
        self.valuation = Valuation()
        assert self.valuation.valuation_excel(menu, value)
        print(f"{sheet4}自动化操作执行完毕")
