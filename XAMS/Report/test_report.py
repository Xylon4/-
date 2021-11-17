import pytest
import xlrd

from XAMS.Report.Finance.valuation import Valuation
from XAMS.Report.Financial.Asset_pool_registry import AssetPoolRegistry
from XAMS.Report.Financial.product import Product
from XAMS.Report.PBC.asset_usufruct import AssetUsufruct
from XAMS.Report.PBC.loan_region import LoanRegion
from XAMS.Report.PBC.loan_statistics import LoanStatistics
from XAMS.Report.PBC.product_amount import ProductAmount
from XAMS.Report.PBC.product_assets import ProductAssets
from XAMS.Report.PBC.product_delay import ProductDelay
from XAMS.Report.PBC.product_quantity import ProductQuantity
from XAMS.Report.PBC.product_remain import ProductRemain
from XAMS.Report.PBC.product_unpaid import ProductUnpaid
from XAMS.Report.conftest import Excel_basedata, sheet1, sheet2, sheet3, sheet4, sheet5, sheet6, sheet7, sheet8, sheet9, \
    sheet10, sheet11, sheet12, sheet13
from XAMS.Tool.test_excel import TestExcel


class TestReport:
    # 万能导入用例
    def test_universal(self, stagemark):
        self.list = TestExcel()
        count = len(self.list.code_list())
        n = 0
        while n < count:
            code = self.list.code_list()[n]
            menu = self.list.group_ele_dic().get(code)
            value = self.list.group_value_dic().get(code)
            test_goal = self.list.group_goal_dic().get(code)
            if test_goal == '模拟操作':
                second_menu = f'{menu[0]}-{menu[1]}'
                address = None
                if second_menu == '估值管理-估值表':
                    self.test_valuation_excel(stagemark, menu, value)
                elif second_menu == '综合管理-表1-1产品募集余额统计表':
                    self.test_product_remain_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-表1-2产品募集兑付统计表':
                    self.test_product_amount_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-表1-3产品只数情况统计表':
                    self.test_product_quantity_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-表1-5产品提前延期兑付统计表':
                    self.test_product_delay_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-表1-6产品到期未兑付统计表':
                    self.test_product_unpaid_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-表2-1产品资产负债统计表':
                    self.test_product_assets_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-表2-2贷款分行业及企业规模统计表':
                    self.test_loan_statistics_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-表2-3贷款分地区统计表':
                    self.test_loan_region_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-表2-4资产收益权投向分类统计表':
                    self.test_asset_usufruct_excel(stagemark, menu, value, address)
                else:
                    print("模拟操作案例：该报表暂不支持，请修改用例")
            elif test_goal == '升级对比':
                second_menu = f'{menu[2]}-{menu[3]}'
                address = value[0]
                if second_menu == '综合管理-表1-1产品募集余额统计表':
                    self.test_product_remain_compare(stagemark, menu, value, address)
                elif second_menu == '综合管理-表1-2产品募集兑付统计表':
                    self.test_product_amount_compare(stagemark, menu, value, address)
                elif second_menu == '综合管理-表1-3产品只数情况统计表':
                    self.test_product_quantity_compare(stagemark, menu, value, address)
                elif second_menu == '综合管理-表1-5产品提前延期兑付统计表':
                    self.test_product_delay_compare(stagemark, menu, value, address)
                elif second_menu == '综合管理-表1-6产品到期未兑付统计表':
                    self.test_product_unpaid_compare(stagemark, menu, value, address)
                elif second_menu == '综合管理-表2-1产品资产负债统计表':
                    self.test_product_assets_compare(stagemark, menu, value, address)
                elif second_menu == '综合管理-表2-2贷款分行业及企业规模统计表':
                    self.test_loan_statistics_compare(stagemark, menu, value, address)
                elif second_menu == '综合管理-表2-3贷款分地区统计表':
                    self.test_loan_region_compare(stagemark, menu, value, address)
                elif second_menu == '综合管理-表2-4资产收益权投向分类统计表':
                    self.test_asset_usufruct_compare(stagemark, menu, value, address)
                else:
                    print("升级对比案例：该报表暂不支持，请修改用例")
            n = n + 1
        print(f'自动化案例执行完毕，共{count}条')

    @pytest.mark.skip
    # 根据excel导入内容选择执行案例
    def test_option(self, stagemark):
        # 打开excel文件
        # excel = xlrd.open_workbook(Excel_basedata)
        # 获取sheet，通过Excel表格名称()获取工作表
        # S1 = excel.sheet_by_name(f'{sheet1}')
        # S2 = excel.sheet_by_name(f'{sheet2}')
        # S3 = excel.sheet_by_name(f'{sheet3}')
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
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product(self, stagemark):
        self.product = Product()
        assert self.product.product()
        print(f"{sheet2}测试通过")
        self.product.end()
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_registry_excel(self, stagemark):
        self.asset_pool_registry = AssetPoolRegistry()
        assert self.asset_pool_registry.registry_excel()
        print(f"{sheet1}自动化操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_excel(self, stagemark):
        self.product = Product()
        assert self.product.product_excel()
        print(f"{sheet2}自动化操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_valuation_excel(self, stagemark, menu, value):
        self.valuation = Valuation()
        assert self.valuation.valuation_excel(menu, value)
        print(f"{sheet4}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_remain_excel(self, stagemark, menu, value, address):
        self.product_remain = ProductRemain(address)
        assert self.product_remain.product_remain_excel(menu, value)
        print(f"{sheet5}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_remain_compare(self, stagemark, menu, value, address):
        self.product_remain_compare = ProductRemain(address)
        assert self.product_remain_compare.product_remain_compare(menu, value)
        self.product_remain_compare.end()
        print(f"{sheet5}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_amount_excel(self, stagemark, menu, value, address):
        self.product_amount = ProductAmount(address)
        assert self.product_amount.product_amount_excel(menu, value)
        print(f"{sheet6}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_amount_compare(self, stagemark, menu, value, address):
        self.product_amount_compare = ProductAmount(address)
        assert self.product_amount_compare.product_amount_compare(menu, value)
        self.product_amount_compare.end()
        print(f"{sheet6}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_quantity_excel(self, stagemark, menu, value, address):
        self.product_quantity = ProductQuantity(address)
        assert self.product_quantity.product_quantity_excel(menu, value)
        print(f"{sheet7}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_quantity_compare(self, stagemark, menu, value, address):
        self.product_quantity_compare = ProductQuantity(address)
        assert self.product_quantity_compare.product_quantity_compare(menu, value)
        self.product_quantity_compare.end()
        print(f"{sheet7}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_delay_excel(self, stagemark, menu, value, address):
        self.product_delay = ProductDelay(address)
        assert self.product_delay.product_delay_excel(menu, value)
        print(f"{sheet8}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_delay_compare(self, stagemark, menu, value, address):
        self.product_delay_compare = ProductDelay(address)
        assert self.product_delay_compare.product_delay_compare(menu, value)
        self.product_delay_compare.end()
        print(f"{sheet8}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_unpaid_excel(self, stagemark, menu, value, address):
        self.product_unpaid = ProductUnpaid(address)
        assert self.product_unpaid.product_unpaid_excel(menu, value)
        print(f"{sheet9}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_unpaid_compare(self, stagemark, menu, value, address):
        self.product_unpaid_compare = ProductUnpaid(address)
        assert self.product_unpaid_compare.product_unpaid_compare(menu, value)
        self.product_unpaid_compare.end()
        print(f"{sheet9}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_assets_excel(self, stagemark, menu, value, address):
        self.product_assets = ProductAssets(address)
        assert self.product_assets.product_assets_excel(menu, value)
        print(f"{sheet10}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_assets_compare(self, stagemark, menu, value, address):
        self.product_assets_compare = ProductAssets(address)
        assert self.product_assets_compare.product_assets_compare(menu, value)
        self.product_assets_compare.end()
        print(f"{sheet10}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_loan_statistics_excel(self, stagemark, menu, value, address):
        self.loan_statistics = LoanStatistics(address)
        assert self.loan_statistics.loan_statistics_excel(menu, value)
        print(f"{sheet11}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_loan_statistics_compare(self, stagemark, menu, value, address):
        self.loan_statistics_compare = LoanStatistics(address)
        assert self.loan_statistics_compare.loan_statistics_compare(menu, value)
        self.loan_statistics_compare.end()
        print(f"{sheet11}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_loan_region_excel(self, stagemark, menu, value, address):
        self.loan_region = LoanRegion(address)
        assert self.loan_region.loan_region_excel(menu, value)
        print(f"{sheet12}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_loan_region_compare(self, stagemark, menu, value, address):
        self.loan_region_compare = LoanRegion(address)
        assert self.loan_region_compare.loan_region_compare(menu, value)
        self.loan_region_compare.end()
        print(f"{sheet12}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_asset_usufruct_excel(self, stagemark, menu, value, address):
        self.asset_usufruct = AssetUsufruct(address)
        assert self.asset_usufruct.asset_usufruct_excel(menu, value)
        print(f"{sheet13}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_asset_usufruct_compare(self, stagemark, menu, value, address):
        self.asset_usufruct_compare = AssetUsufruct(address)
        assert self.asset_usufruct_compare.asset_usufruct_compare(menu, value)
        self.asset_usufruct_compare.end()
        print(f"{sheet13}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')
