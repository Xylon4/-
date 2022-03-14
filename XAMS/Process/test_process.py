import pytest

from XAMS.Process.Trade_process.bond_trade_process import BondTradeProcess


class TestProcess:
    # 万能导入用例
    def test_universal(self, stagemark, code, menu, value, test_goal):
        if test_goal == '流程自动化':
            address = value[0]
            if value[1] == '银行间现券买入':
                self.test_bond_trade_process(stagemark, code, menu, value, address)
            else:
                print("流程自动化案例：该流程暂不支持，请修改用例")
                return False
        else:
            print("该测试目的暂不支持，请修改用例")
            return False

    @pytest.mark.skip
    def test_bond_trade_process(self, stagemark, code, menu, value, address):
        self.bond_trade_process = BondTradeProcess(address)
        assert self.bond_trade_process.bond_trade_process(code, menu, value)
        print("现券交易流程自动化执行完毕")
        print('-----------------------这是案例分割线-----------------------')
