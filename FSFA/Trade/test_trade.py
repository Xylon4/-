from FSFA.Trade.bond_trade import BondTrade


class TestTrade:
    def setup(self):
        self.bond_trade = BondTrade()

    def teardown(self):
        pass

    def test_bond_trade1(self, stagemark):
        assert self.bond_trade.bondtrade1()

    def test_bond_trade2(self, stagemark):
        assert self.bond_trade.bondtrade2()

    def test_bond_trade3(self, stagemark):
        assert self.bond_trade.bondtrade3()
