import pytest

from XAMS.Asset.Asset_duration.current_pay import CurrentPay
from XAMS.Asset.Bond.bond import Bond
from XAMS.Asset.Interbank_money_markets.fund import Fund
from XAMS.Report.conftest import sheet29, sheet40, sheet43
from XAMS.Tool.test_excel import TestExcel


class TestAsset:
    # 万能导入用例
    def test_universal(self, stagemark, menu, value, test_goal, step):
        self.list = TestExcel()
        if test_goal == '模拟操作':
            second_menu = f'{menu[1]}-{menu[2]}'
            address = value[0]
            if second_menu == '资产管理-债券类资产(新)':
                self.test_bond_excel(stagemark, menu, value, address, step)
            elif second_menu == '资产管理-活期账户提前收息':
                self.test_current_pay_excel(stagemark, menu, value, address, step)
            elif second_menu == '资产管理-货币基金':
                self.test_fund_excel(stagemark, menu, value, address, step)
            else:
                print("模拟操作案例：该资产暂不支持，请修改用例")
        elif test_goal == '升级对比':
            second_menu = f'{menu[2]}-{menu[3]}'
            address = value[0]
        else:
            print("该测试目的暂不支持，请修改用例")
            return False

    @pytest.mark.skip
    def test_bond_excel(self, stagemark, menu, value, address, step):
        self.bond = Bond(address)
        assert self.bond.bond_excel(menu, value)
        if step is not None:
            self.bond.end()
        print(f"{sheet29}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_current_pay_excel(self, stagemark, menu, value, address, step):
        self.current_pay = CurrentPay(address)
        assert self.current_pay.current_pay_excel(menu, value)
        if step is not None:
            self.current_pay.end()
        print(f"{sheet40}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')

    @pytest.mark.skip
    def test_fund_excel(self, stagemark, menu, value, address, step):
        self.fund = Fund(address)
        assert self.fund.fund_excel(menu, value)
        if step is not None:
            self.fund.end()
        print(f"{sheet43}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')
