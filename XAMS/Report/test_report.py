import pytest
import xlrd

from XAMS.Report.CBRC.asset_registration import AssetRegistration
from XAMS.Report.CBRC.deal_registration import DealRegistration
from XAMS.Report.CBRC.product_duration_registration import ProductDurationRegistration
from XAMS.Report.Combinatorial_analysis.asset_detail import AssetDetail
from XAMS.Report.Combinatorial_analysis.asset_detail_penetration import AssetDetailPenetration
from XAMS.Report.Combinatorial_analysis.asset_structure import AssetStructure
from XAMS.Report.Combinatorial_analysis.cash_flow import CashFlow
from XAMS.Report.Combinatorial_analysis.cash_gap import CashGap
from XAMS.Report.Combinatorial_analysis.profit_loss import ProfitLoss
from XAMS.Report.Finance.valuation import Valuation
from XAMS.Report.Financial.asset_liability import AssetLiability
from XAMS.Report.Financial.asset_pool_registry import AssetPoolRegistry
from XAMS.Report.Financial.product import Product
from XAMS.Report.Financial.product_termination import ProductTermination
from XAMS.Report.PBC.asset_usufruct import AssetUsufruct
from XAMS.Report.PBC.enterprise_bond import EnterpriseBond
from XAMS.Report.PBC.loan_region import LoanRegion
from XAMS.Report.PBC.loan_statistics import LoanStatistics
from XAMS.Report.PBC.new_product_contract import NewProductContract
from XAMS.Report.PBC.product_amount import ProductAmount
from XAMS.Report.PBC.product_assets import ProductAssets
from XAMS.Report.PBC.last_product_contract import LastProductContract
from XAMS.Report.PBC.product_delay import ProductDelay
from XAMS.Report.PBC.product_quantity import ProductQuantity
from XAMS.Report.PBC.product_remain import ProductRemain
from XAMS.Report.PBC.product_term import ProductTerm
from XAMS.Report.PBC.product_unpaid import ProductUnpaid
from XAMS.Report.conftest import Excel_basedata, sheet1, sheet2, sheet3, sheet4, sheet5, sheet6, sheet7, sheet8, sheet9, \
    sheet10, sheet11, sheet12, sheet13, sheet14, sheet15, sheet16, sheet17, sheet18, sheet19, sheet20, sheet21, sheet22, \
    sheet23, sheet24, sheet25, sheet26, sheet27
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
                elif second_menu == '综合管理-表2-5企业债券分行业及企业规模统计表':
                    self.test_enterprise_bond_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-表3-1存续产品分合同期限募集余额统计表':
                    self.test_last_product_contract_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-表3-2新发产品分合同期限募集金额统计表':
                    self.test_new_product_contract_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-表3-3资管产品资产负债剩余期限统计表':
                    self.test_product_term_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-产品终止信息表':
                    self.test_product_termination_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-产品信息表':
                    self.test_product_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-资负信息注册(浙商)':
                    self.test_asset_liability_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-交易登记':
                    self.test_deal_registration_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-资产要素登记':
                    self.test_asset_registration_excel(stagemark, menu, value, address)
                elif second_menu == '综合管理-产品存续期登记':
                    self.test_product_duration_registration_excel(stagemark, menu, value, address)
                elif second_menu == '投组管理-投组单元资产明细表(穿透)':
                    self.test_asset_detail_penetration_excel(stagemark, menu, value, address)
                elif second_menu == '投组管理-投组单元资产明细表':
                    self.test_asset_detail_excel(stagemark, menu, value, address)
                elif second_menu == '投组管理-现金流缺口表(新)':
                    self.test_cash_gap_excel(stagemark, menu, value, address)
                elif second_menu == '投组管理-现金流明细表(新)':
                    self.test_cash_flow_excel(stagemark, menu, value, address)
                elif second_menu == '投组管理-损益分析表':
                    self.test_profit_loss_excel(stagemark, menu, value, address)
                elif second_menu == '投组管理-资产结构分析表':
                    self.test_asset_structure_excel(stagemark, menu, value, address)
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
                elif second_menu == '综合管理-表2-5企业债券分行业及企业规模统计表':
                    self.test_enterprise_bond_compare(stagemark, menu, value, address)
                elif second_menu == '综合管理-表3-1存续产品分合同期限募集余额统计表':
                    self.test_last_product_contract_compare(stagemark, menu, value, address)
                elif second_menu == '综合管理-表3-2新发产品分合同期限募集金额统计表':
                    self.test_new_product_contract_compare(stagemark, menu, value, address)
                elif second_menu == '综合管理-表3-3资管产品资产负债剩余期限统计表':
                    self.test_product_term_compare(stagemark, menu, value, address)
                elif second_menu == '综合管理-资负信息注册(浙商)':
                    self.test_asset_liability_compare(stagemark, menu, value, address)
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

    @pytest.mark.skip
    def test_enterprise_bond_excel(self, stagemark, menu, value, address):
        self.enterprise_bond = EnterpriseBond(address)
        assert self.enterprise_bond.enterprise_bond_excel(menu, value)
        print(f"{sheet14}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_enterprise_bond_compare(self, stagemark, menu, value, address):
        self.enterprise_bond_compare = EnterpriseBond(address)
        assert self.enterprise_bond_compare.enterprise_bond_compare(menu, value)
        self.enterprise_bond_compare.end()
        print(f"{sheet14}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_last_product_contract_excel(self, stagemark, menu, value, address):
        self.last_product_contract = LastProductContract(address)
        assert self.last_product_contract.last_product_contract_excel(menu, value)
        print(f"{sheet15}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_last_product_contract_compare(self, stagemark, menu, value, address):
        self.last_product_contract_compare = LastProductContract(address)
        assert self.last_product_contract_compare.last_product_contract_compare(menu, value)
        self.last_product_contract_compare.end()
        print(f"{sheet15}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_new_product_contract_excel(self, stagemark, menu, value, address):
        self.new_product_contract = NewProductContract(address)
        assert self.new_product_contract.new_product_contract_excel(menu, value)
        print(f"{sheet16}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_new_product_contract_compare(self, stagemark, menu, value, address):
        self.new_product_contract_compare = NewProductContract(address)
        assert self.new_product_contract_compare.new_product_contract_compare(menu, value)
        self.new_product_contract_compare.end()
        print(f"{sheet16}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_term_excel(self, stagemark, menu, value, address):
        self.product_term = ProductTerm(address)
        assert self.product_term.product_term_excel(menu, value)
        print(f"{sheet17}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_term_compare(self, stagemark, menu, value, address):
        self.product_term_compare = ProductTerm(address)
        assert self.product_term_compare.product_term_compare(menu, value)
        self.product_term_compare.end()
        print(f"{sheet17}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_termination_excel(self, stagemark, menu, value, address):
        self.product_termination = ProductTermination(address)
        assert self.product_termination.product_termination_excel(menu, value)
        print(f"{sheet18}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_excel(self, stagemark, menu, value, address):
        self.product = Product(address)
        assert self.product.product_excel(menu, value)
        print(f"{sheet2}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_asset_liability_excel(self, stagemark, menu, value, address):
        self.asset_liability = AssetLiability(address)
        assert self.asset_liability.asset_liability_excel(menu, value)
        print(f"{sheet3}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_asset_liability_compare(self, stagemark, menu, value, address):
        self.asset_liability_compare = AssetLiability(address)
        assert self.asset_liability_compare.asset_liability_compare(menu, value)
        self.asset_liability_compare.end()
        print(f"{sheet3}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_deal_registration_excel(self, stagemark, menu, value, address):
        self.deal_registration = DealRegistration(address)
        assert self.deal_registration.deal_registration_excel(menu, value)
        print(f"{sheet19}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_asset_registration_excel(self, stagemark, menu, value, address):
        self.asset_registration = AssetRegistration(address)
        assert self.asset_registration.asset_registration_excel(menu, value)
        print(f"{sheet20}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_duration_registration_excel(self, stagemark, menu, value, address):
        self.product_duration_registration = ProductDurationRegistration(address)
        assert self.product_duration_registration.product_duration_registration_excel(menu, value)
        print(f"{sheet21}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_asset_detail_penetration_excel(self, stagemark, menu, value, address):
        self.asset_detail_penetration = AssetDetailPenetration(address)
        assert self.asset_detail_penetration.asset_detail_penetration_excel(menu, value)
        print(f"{sheet22}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_asset_detail_excel(self, stagemark, menu, value, address):
        self.asset_detail = AssetDetail(address)
        assert self.asset_detail.asset_detail_excel(menu, value)
        print(f"{sheet23}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_cash_gap_excel(self, stagemark, menu, value, address):
        self.cash_gap = CashGap(address)
        assert self.cash_gap.cash_gap_excel(menu, value)
        print(f"{sheet24}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_cash_flow_excel(self, stagemark, menu, value, address):
        self.cash_flow = CashFlow(address)
        assert self.cash_flow.cash_flow_excel(menu, value)
        print(f"{sheet25}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_profit_loss_excel(self, stagemark, menu, value, address):
        self.profit_loss = ProfitLoss(address)
        assert self.profit_loss.profit_loss_excel(menu, value)
        print(f"{sheet26}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_asset_structure_excel(self, stagemark, menu, value, address):
        self.asset_structure = AssetStructure(address)
        assert self.asset_structure.asset_structure_excel(menu, value)
        print(f"{sheet27}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')