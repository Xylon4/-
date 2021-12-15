import pytest

from XAMS.Report.conftest import sheet31
from XAMS.Tool.test_excel import TestExcel
from XAMS.Trade.Bond.exchange_bond_approve import ExchangeBondApprove


class TestTrade:
    # 万能导入用例
    def test_universal(self, stagemark, menu, value, test_goal, step):
        self.list = TestExcel()
        if test_goal == '模拟操作':
            second_menu = f'{menu[1]}-{menu[2]}'
            address = value[0]
            if second_menu == '交易管理-交易所债券审批':
                self.test_exchange_bond_approve_excel(stagemark, menu, value, address, step)
            else:
                print("模拟操作案例：该报表暂不支持，请修改用例")
        else:
            print("该测试目的暂不支持，请修改用例")
            return False

    @pytest.mark.skip
    def test_exchange_bond_approve_excel(self, stagemark, menu, value, address, step):
        self.exchange_bond_approve = ExchangeBondApprove(address)
        assert self.exchange_bond_approve.exchange_bond_approve_excel(menu, value)
        if step is not None:
            self.exchange_bond_approve.end()
        print(f"{sheet31}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')
