from FSFA.Valuation.valuation import Valuation


class TestValuation:
    def setup(self):
        self.valuation = Valuation()

    def teardown(self):
        self.valuation.end()

    def test_valuation(self, stagemark):
        assert self.valuation.valuation1()
        assert self.valuation.valuation2()
