import pytest

from XAMS.Liquidation.transactions_review import TransactionsReview
from XAMS.Report.conftest import sheet42
from XAMS.Tool.test_excel import TestExcel


class TestLiquidation:
    # 万能导入用例
    def test_universal(self, stagemark, menu, value, test_goal, step):
        self.list = TestExcel()
        if test_goal == '模拟操作':
            second_menu = f'{menu[1]}-{menu[2]}'
            address = value[0]
            if second_menu == '清算管理-待复核交易指令列表':
                self.test_transactions_review_excel(stagemark, menu, value, address, step)
            else:
                print("模拟操作案例：该资产暂不支持，请修改用例")
        elif test_goal == '升级对比':
            second_menu = f'{menu[2]}-{menu[3]}'
            address = value[0]
        else:
            print("该测试目的暂不支持，请修改用例")
            return False

    @pytest.mark.skip
    def test_transactions_review_excel(self, stagemark, menu, value, address, step):
        self.transactions_review = TransactionsReview(address)
        assert self.transactions_review.transactions_review_excel(menu, value)
        if step is not None:
            self.transactions_review.end()
        print(f"{sheet42}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')
