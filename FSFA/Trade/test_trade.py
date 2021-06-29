from FSFA.Trade.bond_trade import BondTrade
from FSFA.Trade.nonstandard_trade import NonstandardTrade


class TestTrade:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_bond_trade1(self, stagemark):
        self.bond_trade = BondTrade()
        assert self.bond_trade.bondtrade1()
        self.bond_trade.end()

    def test_bond_trade2(self, stagemark):
        self.bond_trade = BondTrade()
        assert self.bond_trade.bondtrade2()
        self.bond_trade.end()

    def test_bond_trade3(self, stagemark):
        self.bond_trade = BondTrade()
        assert self.bond_trade.bondtrade3()
        self.bond_trade.end()

    def test_nonstandard_trade1(self, stagemark):
        self.nonstandard_trade = NonstandardTrade()
        assert self.nonstandard_trade.nonstandardtrade1()
        self.nonstandard_trade.end()

    def test_nonstandard_trade2(self, stagemark):
        self.nonstandard_trade = NonstandardTrade()
        assert self.nonstandard_trade.nonstandardtrade2()
        self.nonstandard_trade.end()

    def test_nonstandard_trade3(self, stagemark):
        self.nonstandard_trade = NonstandardTrade()
        assert self.nonstandard_trade.nonstandardtrade3()
        self.nonstandard_trade.end()
