import pytest
import xlrd
from XAMS.Report.Financial.Asset_pool_registry import AssetPoolRegistry
from XAMS.Report.Financial.product import Product
from XAMS.Report.conftest import Excel_report, sheet1, sheet2, sheet3
from XAMS.Tool.test_excel import TestExcel
from XAMS.conftest import stagemark


class TestReport:
    # 定义根据excel导入内容选择执行案例的方法
    def test_option(self):
        # 打开excel文件
        excel = xlrd.open_workbook(Excel_report)
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
