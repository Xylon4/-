from FSFA.Valuation.valuation import Valuation


class TestValuation:
    def setup(self):
        self.valuation = Valuation()

    def teardown(self):
        self.valuation.end()
        # pass

    def test_valuation1(self, get_batch, stagemark):
        assert self.valuation.valuation1(get_batch)
        assert self.valuation.valuation2(get_batch)

    # 估值回历史独立执行，解决多个页签情况下回历史按钮不可点击问题
    def test_valuation2(self, get_batch, stagemark):
        assert self.valuation.valuation3(get_batch)
