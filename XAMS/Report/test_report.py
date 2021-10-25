import pytest
import xlrd
from XAMS.Report.Financial.Asset_pool_registry import AssetPoolRegistry
from XAMS.Report.Financial.product import Product


class TestReport:
    # 定义根据excel导入内容选择执行案例的方法
    def test_option(self):
        # 打开excel文件
        excel = xlrd.open_workbook(r'C:\Users\1\Desktop\自动化读取报表.xlsx')
        # 获取sheet，通过Excel表格名称(rank)获取工作表
        sheet1 = excel.sheet_by_name('资产池注册表')
        sheet2 = excel.sheet_by_name('产品信息表')
        sheet3 = excel.sheet_by_name('资负信息注册(浙商)')
        # 校验工作表数据(统计操作列表中"1"的重复次数)


    @pytest.mark.skip
    def test_asset_pool_registry(self, get_registry, stagemark):
        self.asset_pool_registry = AssetPoolRegistry()
        assert self.asset_pool_registry.registry(get_registry)
        print("资产池注册表测试通过")
        self.asset_pool_registry.end()

    @pytest.mark.skip
    def test_product(self, stagemark):
        self.product = Product()
        assert self.product.product()
        print("产品信息表测试通过")
        self.product.end()

    def test_registry_excel(self, stagemark):
        self.asset_pool_registry = AssetPoolRegistry()
        assert self.asset_pool_registry.registry_excel()
        print("资产池注册表自动化操作执行完毕")