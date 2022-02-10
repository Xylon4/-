import pytest

from XAMS.Product.Product.series import Series
from XAMS.Report.conftest import sheet54
from XAMS.Tool.test_excel import TestExcel


class TestProduct:
    # 万能导入用例
    def test_universal(self, stagemark, menu, value, test_goal, step):
        self.list = TestExcel()
        if test_goal == '模拟操作':
            second_menu = f'{menu[1]}-{menu[2]}'
            address = value[0]
            if second_menu == '产品管理-产品系列定义':
                self.test_series_excel(stagemark, menu, value, address, step)
            else:
                print("模拟操作案例：该估值暂不支持，请修改用例")
        elif test_goal == '升级对比':
            second_menu = f'{menu[2]}-{menu[3]}'
            address = value[0]
        else:
            print("该测试目的暂不支持，请修改用例")
            return False

    @pytest.mark.skip
    def test_series_excel(self, stagemark, menu, value, address, step):
        self.series = Series(address)
        assert self.series.series_excel(menu, value)
        if step is not None:
            self.series.end()
        print(f"{sheet54}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')
