import pytest

from FSFA.Trade.bond_trade import BondTrade
from FSFA.Trade.nonstandard_trade import NonstandardTrade


class TestTrade:
    def setup(self):
        pass

    def teardown(self):
        pass

    # @pytest.mark.skip
    def test_bond_trade1(self, get_bond, stagemark):
        self.bond_trade = BondTrade()
        assert self.bond_trade.bondtrade1(get_bond)
        self.bond_trade.end()

    # @pytest.mark.skip
    def test_bond_trade2(self, get_bond, stagemark):
        self.bond_trade = BondTrade()
        assert self.bond_trade.bondtrade2(get_bond)
        self.bond_trade.end()

    # @pytest.mark.skip
    def test_bond_trade3(self, get_bond, stagemark):
        self.bond_trade = BondTrade()
        assert self.bond_trade.bondtrade3(get_bond)
        self.bond_trade.end()

    @pytest.mark.skip
    def test_nonstandard_trade1(self, get_nonstandard, stagemark):
        self.nonstandard_trade = NonstandardTrade()
        assert self.nonstandard_trade.nonstandardtrade1(get_nonstandard)
        self.nonstandard_trade.end()

    @pytest.mark.skip
    def test_nonstandard_trade2(self, get_nonstandard, stagemark):
        self.nonstandard_trade = NonstandardTrade()
        assert self.nonstandard_trade.nonstandardtrade2(get_nonstandard)
        self.nonstandard_trade.end()

    # 因为元素属性不正确导致判断函数失败，所以需要针对用例不同做区分对待，影响代码的完整性
    # 当非标和债券使用相同的账套进行操作时，费用摊销步骤只需要执行一次
    # 以上两个问题已解决
    @pytest.mark.skip
    def test_nonstandard_trade3(self, get_nonstandard, stagemark):
        self.nonstandard_trade = NonstandardTrade()
        assert self.nonstandard_trade.nonstandardtrade3(get_nonstandard)
        self.nonstandard_trade.end()
