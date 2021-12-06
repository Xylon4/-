import pytest

from XAMS.Asset.Bond.bond import Bond
from XAMS.Report.conftest import sheet29
from XAMS.Tool.test_excel import TestExcel


class TestAsset:
    # 万能导入用例
    def test_universal(self, stagemark, menu, value, test_goal):
        self.list = TestExcel()
        if test_goal == '模拟操作':
            second_menu = f'{menu[0]}-{menu[1]}'
            address = None
            if second_menu == '资产管理-债券类资产(新)':
                self.test_bond_excel(stagemark, menu, value, address)
            else:
                print("模拟操作案例：该报表暂不支持，请修改用例")
        elif test_goal == '升级对比':
            second_menu = f'{menu[2]}-{menu[3]}'
            address = value[0]
        else:
            print("该测试目的暂不支持，请修改用例")
            return False

    @pytest.mark.skip
    def test_bond_excel(self, stagemark, menu, value, address):
        self.bond = Bond(address)
        assert self.bond.bond_excel(menu, value)
        print(f"{sheet29}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')
