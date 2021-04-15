from FSFA.Valuation.valuation import Valuation


class TestValuation:
    def setup(self):
        self.valuation = Valuation()

    def teardown(self):
        # self.valuation.end()
        pass

    def test_valuation(self):
        assert self.valuation.valuation1()
        assert self.valuation.valuation2()
