from XAMS.Report.test_report import TestReport
from XAMS.Tool.test_excel import TestExcel
from XAMS.conftest import report_list


class TestAuto:
    def test_auto(self, stagemark):
        self.list = TestExcel()
        self.module = TestReport()
        count = len(self.list.code_list())
        n = 0
        sum_report = 0
        sum_asset = 0
        sum_trade = 0
        sum_product = 0
        while n < count:
            code = self.list.code_list()[n]
            menu = self.list.group_ele_dic().get(code)
            value = self.list.group_value_dic().get(code)
            test_goal = self.list.group_goal_dic().get(code)
            if test_goal == '模拟操作':
                second_menu = f'{menu[0]}-{menu[1]}'
                if second_menu in report_list:
                    self.module.test_universal(stagemark, menu, value, test_goal)
                    sum_report = sum_report + 1
                else:
                    print("该界面模拟操作暂不支持，请修改用例")
                    return False
            elif test_goal == '升级对比':
                second_menu = f'{menu[2]}-{menu[3]}'
                if second_menu in report_list:
                    self.module.test_universal(stagemark, menu, value, test_goal)
                    sum_report = sum_report + 1
                else:
                    print("该界面升级对比暂不支持，请修改用例")
                    return False
            else:
                print("该测试目的暂不支持，请修改用例")
                return False
            n = n + 1
        print(f'报表案例执行完毕，共{sum_report}条')
        print(f'自动化案例执行完毕，共{count}条')
