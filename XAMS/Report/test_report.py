import pytest

from XAMS.Report.CBRC.asset_registration import AssetRegistration
from XAMS.Report.CBRC.deal_registration import DealRegistration
from XAMS.Report.CBRC.interbank_counterparty import InterbankCounterparty
from XAMS.Report.CBRC.monthly_statistics import MonthlyStatistics
from XAMS.Report.CBRC.product_duration_registration import ProductDurationRegistration
from XAMS.Report.CBRC.table_asset import TableAsset
from XAMS.Report.CBRC.table_term_cost import TableTermCost
from XAMS.Report.Combinatorial_analysis.asset_detail import AssetDetail
from XAMS.Report.Combinatorial_analysis.asset_detail_penetration import AssetDetailPenetration
from XAMS.Report.Combinatorial_analysis.asset_structure import AssetStructure
from XAMS.Report.Combinatorial_analysis.cash_flow import CashFlow
from XAMS.Report.Combinatorial_analysis.cash_gap import CashGap
from XAMS.Report.Combinatorial_analysis.profit_loss import ProfitLoss
from XAMS.Report.Combinatorial_analysis.valuation_detail import ValuationDetail
from XAMS.Report.Finance.account_balance import AccountBalance
from XAMS.Report.Finance.balance import Balance
from XAMS.Report.Finance.income import Income
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
from XAMS.Report.conftest import sheet1, sheet2, sheet3, sheet4, sheet5, sheet6, sheet7, sheet8, \
    sheet9, \
    sheet10, sheet11, sheet12, sheet13, sheet14, sheet15, sheet16, sheet17, sheet18, sheet19, sheet20, sheet21, sheet22, \
    sheet23, sheet24, sheet25, sheet26, sheet27, sheet28, sheet30, sheet37, sheet38, sheet39, sheet44, sheet45, sheet46, \
    sheet47, sheet48, sheet49
from XAMS.Report.iWallet.day_entry import DayEntry
from XAMS.Report.iWallet.periodic_entry import PeriodicEntry
from XAMS.Report.iWallet.profit_carry_over_entry import ProfitCarryOverEntry
from XAMS.Tool.test_excel import TestExcel


class TestReport:
    # 万能导入用例
    def test_universal(self, stagemark, menu, value, test_goal, step):
        self.list = TestExcel()
        if test_goal == '模拟操作':
            second_menu = f'{menu[1]}-{menu[2]}'
            address = value[0]
            if second_menu == '估值管理-估值表':
                self.test_valuation_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表1-1产品募集余额统计表':
                self.test_product_remain_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表1-2产品募集兑付统计表':
                self.test_product_amount_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表1-3产品只数情况统计表':
                self.test_product_quantity_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表1-5产品提前延期兑付统计表':
                self.test_product_delay_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表1-6产品到期未兑付统计表':
                self.test_product_unpaid_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表2-1产品资产负债统计表':
                self.test_product_assets_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表2-2贷款分行业及企业规模统计表':
                self.test_loan_statistics_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表2-3贷款分地区统计表':
                self.test_loan_region_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表2-4资产收益权投向分类统计表':
                self.test_asset_usufruct_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表2-5企业债券分行业及企业规模统计表':
                self.test_enterprise_bond_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表3-1存续产品分合同期限募集余额统计表':
                self.test_last_product_contract_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表3-2新发产品分合同期限募集金额统计表':
                self.test_new_product_contract_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表3-3资管产品资产负债剩余期限统计表':
                self.test_product_term_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-产品终止信息表':
                self.test_product_termination_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-产品信息表':
                self.test_product_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-资负信息注册(浙商)':
                self.test_asset_liability_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-交易登记':
                self.test_deal_registration_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-资产要素登记':
                self.test_asset_registration_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-产品存续期登记':
                self.test_product_duration_registration_excel(stagemark, menu, value, address, step)
            elif second_menu == '投组管理-投组单元资产明细表(穿透)':
                self.test_asset_detail_penetration_excel(stagemark, menu, value, address, step)
            elif second_menu == '投组管理-投组单元资产明细表':
                self.test_asset_detail_excel(stagemark, menu, value, address, step)
            elif second_menu == '投组管理-现金流缺口表(新)':
                self.test_cash_gap_excel(stagemark, menu, value, address, step)
            elif second_menu == '投组管理-现金流明细表(新)':
                self.test_cash_flow_excel(stagemark, menu, value, address, step)
            elif second_menu == '投组管理-损益分析表':
                self.test_profit_loss_excel(stagemark, menu, value, address, step)
            elif second_menu == '投组管理-资产结构分析表':
                self.test_asset_structure_excel(stagemark, menu, value, address, step)
            elif second_menu == '投组管理-投组单元估值明细表':
                self.test_valuation_detail_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-产品情况月度统计表-资产':
                self.test_monthly_statistics_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表内外投资业务基础资产情况表':
                self.test_table_asset_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表内外投资业务期限结构及成本收益表':
                self.test_table_term_cost_excel(stagemark, menu, value, address, step)
            elif second_menu == '综合管理-表七同业交易对手情况表':
                self.test_interbank_counterparty_excel(stagemark, menu, value, address, step)
            elif second_menu == '估值管理-日间分录查询':
                self.test_day_entry_excel(stagemark, menu, value, address, step)
            elif second_menu == '估值管理-周期分录查询':
                self.test_periodic_entry_excel(stagemark, menu, value, address, step)
            elif second_menu == '估值管理-损益结转分录查询':
                self.test_profit_carry_over_entry_excel(stagemark, menu, value, address, step)
            elif second_menu == '估值管理-利润表(平台)':
                self.test_income_excel(stagemark, menu, value, address, step)
            elif second_menu == '估值管理-资产负债表(平台)':
                self.test_balance_excel(stagemark, menu, value, address, step)
            elif second_menu == '估值管理-科目余额表':
                self.test_account_balance_excel(stagemark, menu, value, address, step)
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
            elif second_menu == '综合管理-产品情况月度统计表-资产':
                self.test_monthly_statistics_compare(stagemark, menu, value, address)
            elif second_menu == '综合管理-表内外投资业务基础资产情况表':
                self.test_table_asset_compare(stagemark, menu, value, address)
            elif second_menu == '综合管理-表内外投资业务期限结构及成本收益表':
                self.test_table_term_cost_compare(stagemark, menu, value, address)
            elif second_menu == '综合管理-表七同业交易对手情况表':
                self.test_interbank_counterparty_compare(stagemark, menu, value, address)
            elif second_menu == '估值管理-日间分录查询':
                self.test_day_entry_compare(stagemark, menu, value, address)
            elif second_menu == '估值管理-周期分录查询':
                self.test_periodic_entry_compare(stagemark, menu, value, address)
            elif second_menu == '估值管理-损益结转分录查询':
                self.test_profit_carry_over_entry_compare(stagemark, menu, value, address)
            elif second_menu == '估值管理-利润表(平台)':
                self.test_income_compare(stagemark, menu, value, address)
            elif second_menu == '估值管理-资产负债表(平台)':
                self.test_balance_compare(stagemark, menu, value, address)
            else:
                print("升级对比案例：该报表暂不支持，请修改用例")
        else:
            print("该测试目的暂不支持，请修改用例")
            return False

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
    def test_valuation_excel(self, stagemark, menu, value, address, step):
        self.valuation = Valuation(address)
        assert self.valuation.valuation_excel(menu, value)
        if step is not None:
            self.valuation.end()
        print(f"{sheet4}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_remain_excel(self, stagemark, menu, value, address, step):
        self.product_remain = ProductRemain(address)
        assert self.product_remain.product_remain_excel(menu, value)
        if step is not None:
            self.product_remain.end()
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
    def test_product_amount_excel(self, stagemark, menu, value, address, step):
        self.product_amount = ProductAmount(address)
        assert self.product_amount.product_amount_excel(menu, value)
        if step is not None:
            self.product_amount.end()
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
    def test_product_quantity_excel(self, stagemark, menu, value, address, step):
        self.product_quantity = ProductQuantity(address)
        assert self.product_quantity.product_quantity_excel(menu, value)
        if step is not None:
            self.product_quantity.end()
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
    def test_product_delay_excel(self, stagemark, menu, value, address, step):
        self.product_delay = ProductDelay(address)
        assert self.product_delay.product_delay_excel(menu, value)
        if step is not None:
            self.product_delay.end()
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
    def test_product_unpaid_excel(self, stagemark, menu, value, address, step):
        self.product_unpaid = ProductUnpaid(address)
        assert self.product_unpaid.product_unpaid_excel(menu, value)
        if step is not None:
            self.product_unpaid.end()
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
    def test_product_assets_excel(self, stagemark, menu, value, address, step):
        self.product_assets = ProductAssets(address)
        assert self.product_assets.product_assets_excel(menu, value)
        if step is not None:
            self.product_assets.end()
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
    def test_loan_statistics_excel(self, stagemark, menu, value, address, step):
        self.loan_statistics = LoanStatistics(address)
        assert self.loan_statistics.loan_statistics_excel(menu, value)
        if step is not None:
            self.loan_statistics.end()
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
    def test_loan_region_excel(self, stagemark, menu, value, address, step):
        self.loan_region = LoanRegion(address)
        assert self.loan_region.loan_region_excel(menu, value)
        if step is not None:
            self.loan_region.end()
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
    def test_asset_usufruct_excel(self, stagemark, menu, value, address, step):
        self.asset_usufruct = AssetUsufruct(address)
        assert self.asset_usufruct.asset_usufruct_excel(menu, value)
        if step is not None:
            self.asset_usufruct.end()
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
    def test_enterprise_bond_excel(self, stagemark, menu, value, address, step):
        self.enterprise_bond = EnterpriseBond(address)
        assert self.enterprise_bond.enterprise_bond_excel(menu, value)
        if step is not None:
            self.enterprise_bond.end()
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
    def test_last_product_contract_excel(self, stagemark, menu, value, address, step):
        self.last_product_contract = LastProductContract(address)
        assert self.last_product_contract.last_product_contract_excel(menu, value)
        if step is not None:
            self.last_product_contract.end()
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
    def test_new_product_contract_excel(self, stagemark, menu, value, address, step):
        self.new_product_contract = NewProductContract(address)
        assert self.new_product_contract.new_product_contract_excel(menu, value)
        if step is not None:
            self.new_product_contract.end()
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
    def test_product_term_excel(self, stagemark, menu, value, address, step):
        self.product_term = ProductTerm(address)
        assert self.product_term.product_term_excel(menu, value)
        if step is not None:
            self.product_term.end()
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
    def test_product_termination_excel(self, stagemark, menu, value, address, step):
        self.product_termination = ProductTermination(address)
        assert self.product_termination.product_termination_excel(menu, value)
        if step is not None:
            self.product_termination.end()
        print(f"{sheet18}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_excel(self, stagemark, menu, value, address, step):
        self.product = Product(address)
        assert self.product.product_excel(menu, value)
        if step is not None:
            self.product.end()
        print(f"{sheet2}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_asset_liability_excel(self, stagemark, menu, value, address, step):
        self.asset_liability = AssetLiability(address)
        assert self.asset_liability.asset_liability_excel(menu, value)
        if step is not None:
            self.asset_liability.end()
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
    def test_deal_registration_excel(self, stagemark, menu, value, address, step):
        self.deal_registration = DealRegistration(address)
        assert self.deal_registration.deal_registration_excel(menu, value)
        if step is not None:
            self.deal_registration.end()
        print(f"{sheet19}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_asset_registration_excel(self, stagemark, menu, value, address, step):
        self.asset_registration = AssetRegistration(address)
        assert self.asset_registration.asset_registration_excel(menu, value)
        if step is not None:
            self.asset_registration.end()
        print(f"{sheet20}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_product_duration_registration_excel(self, stagemark, menu, value, address, step):
        self.product_duration_registration = ProductDurationRegistration(address)
        assert self.product_duration_registration.product_duration_registration_excel(menu, value)
        if step is not None:
            self.product_duration_registration.end()
        print(f"{sheet21}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_asset_detail_penetration_excel(self, stagemark, menu, value, address, step):
        self.asset_detail_penetration = AssetDetailPenetration(address)
        assert self.asset_detail_penetration.asset_detail_penetration_excel(menu, value)
        if step is not None:
            self.asset_detail_penetration.end()
        print(f"{sheet22}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_asset_detail_excel(self, stagemark, menu, value, address, step):
        self.asset_detail = AssetDetail(address)
        assert self.asset_detail.asset_detail_excel(menu, value)
        if step is not None:
            self.asset_detail.end()
        print(f"{sheet23}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_cash_gap_excel(self, stagemark, menu, value, address, step):
        self.cash_gap = CashGap(address)
        assert self.cash_gap.cash_gap_excel(menu, value)
        if step is not None:
            self.cash_gap.end()
        print(f"{sheet24}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_cash_flow_excel(self, stagemark, menu, value, address, step):
        self.cash_flow = CashFlow(address)
        assert self.cash_flow.cash_flow_excel(menu, value)
        if step is not None:
            self.cash_flow.end()
        print(f"{sheet25}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_profit_loss_excel(self, stagemark, menu, value, address, step):
        self.profit_loss = ProfitLoss(address)
        assert self.profit_loss.profit_loss_excel(menu, value)
        if step is not None:
            self.profit_loss.end()
        print(f"{sheet26}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_asset_structure_excel(self, stagemark, menu, value, address, step):
        self.asset_structure = AssetStructure(address)
        assert self.asset_structure.asset_structure_excel(menu, value)
        if step is not None:
            self.asset_structure.end()
        print(f"{sheet27}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_valuation_detail_excel(self, stagemark, menu, value, address, step):
        self.valuation_detail = ValuationDetail(address)
        assert self.valuation_detail.valuation_detail_excel(menu, value)
        if step is not None:
            self.valuation_detail.end()
        print(f"{sheet28}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_monthly_statistics_excel(self, stagemark, menu, value, address, step):
        self.monthly_statistics = MonthlyStatistics(address)
        assert self.monthly_statistics.monthly_statistics_excel(menu, value)
        if step is not None:
            self.monthly_statistics.end()
        print(f"{sheet30}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_monthly_statistics_compare(self, stagemark, menu, value, address):
        self.monthly_statistics_compare = MonthlyStatistics(address)
        assert self.monthly_statistics_compare.monthly_statistics_compare(menu, value)
        self.monthly_statistics_compare.end()
        print(f"{sheet30}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_table_asset_excel(self, stagemark, menu, value, address, step):
        self.table_asset = TableAsset(address)
        assert self.table_asset.table_asset_excel(menu, value)
        if step is not None:
            self.table_asset.end()
        print(f"{sheet37}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_table_asset_compare(self, stagemark, menu, value, address):
        self.table_asset_compare = TableAsset(address)
        assert self.table_asset_compare.table_asset_compare(menu, value)
        self.table_asset_compare.end()
        print(f"{sheet37}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_table_term_cost_excel(self, stagemark, menu, value, address, step):
        self.table_term_cost = TableTermCost(address)
        assert self.table_term_cost.table_term_cost_excel(menu, value)
        if step is not None:
            self.table_term_cost.end()
        print(f"{sheet38}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_table_term_cost_compare(self, stagemark, menu, value, address):
        self.table_term_cost_compare = TableTermCost(address)
        assert self.table_term_cost_compare.table_term_cost_compare(menu, value)
        self.table_term_cost_compare.end()
        print(f"{sheet38}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_interbank_counterparty_excel(self, stagemark, menu, value, address, step):
        self.interbank_counterparty = InterbankCounterparty(address)
        assert self.interbank_counterparty.interbank_counterparty_excel(menu, value)
        if step is not None:
            self.interbank_counterparty.end()
        print(f"{sheet39}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_interbank_counterparty_compare(self, stagemark, menu, value, address):
        self.interbank_counterparty_compare = InterbankCounterparty(address)
        assert self.interbank_counterparty_compare.interbank_counterparty_compare(menu, value)
        self.interbank_counterparty_compare.end()
        print(f"{sheet39}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_day_entry_excel(self, stagemark, menu, value, address, step):
        self.day_entry = DayEntry(address)
        assert self.day_entry.day_entry_excel(menu, value)
        if step is not None:
            self.day_entry.end()
        print(f"{sheet44}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_day_entry_compare(self, stagemark, menu, value, address):
        self.day_entry_compare = DayEntry(address)
        assert self.day_entry_compare.day_entry_compare(menu, value)
        self.day_entry_compare.end()
        print(f"{sheet44}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_periodic_entry_excel(self, stagemark, menu, value, address, step):
        self.periodic_entry = PeriodicEntry(address)
        assert self.periodic_entry.periodic_entry_excel(menu, value)
        if step is not None:
            self.periodic_entry.end()
        print(f"{sheet45}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_periodic_entry_compare(self, stagemark, menu, value, address):
        self.periodic_entry_compare = PeriodicEntry(address)
        assert self.periodic_entry_compare.periodic_entry_compare(menu, value)
        self.periodic_entry_compare.end()
        print(f"{sheet45}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_profit_carry_over_entry_excel(self, stagemark, menu, value, address, step):
        self.profit_carry_over_entry = ProfitCarryOverEntry(address)
        assert self.profit_carry_over_entry.profit_carry_over_entry_excel(menu, value)
        if step is not None:
            self.profit_carry_over_entry.end()
        print(f"{sheet46}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_profit_carry_over_entry_compare(self, stagemark, menu, value, address):
        self.profit_carry_over_entry_compare = ProfitCarryOverEntry(address)
        assert self.profit_carry_over_entry_compare.profit_carry_over_entry_compare(menu, value)
        self.profit_carry_over_entry_compare.end()
        print(f"{sheet46}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')
        
    @pytest.mark.skip
    def test_income_excel(self, stagemark, menu, value, address, step):
        self.income = Income(address)
        assert self.income.income_excel(menu, value)
        if step is not None:
            self.income.end()
        print(f"{sheet47}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_income_compare(self, stagemark, menu, value, address):
        self.income_compare = Income(address)
        assert self.income_compare.income_compare(menu, value)
        self.income_compare.end()
        print(f"{sheet47}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')
        
    @pytest.mark.skip
    def test_balance_excel(self, stagemark, menu, value, address, step):
        self.balance = Balance(address)
        assert self.balance.balance_excel(menu, value)
        if step is not None:
            self.balance.end()
        print(f"{sheet48}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_balance_compare(self, stagemark, menu, value, address):
        self.balance_compare = Balance(address)
        assert self.balance_compare.balance_compare(menu, value)
        self.balance_compare.end()
        print(f"{sheet48}升级对比执行完毕")
        print('-----------------------这是案例分割线-----------------------')
        
    @pytest.mark.skip
    def test_account_balance_excel(self, stagemark, menu, value, address, step):
        self.account_balance = AccountBalance(address)
        assert self.account_balance.account_balance_excel(menu, value)
        if step is not None:
            self.account_balance.end()
        print(f"{sheet49}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')
