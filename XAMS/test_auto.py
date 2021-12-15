from XAMS.Asset.test_asset import TestAsset
from XAMS.Report.test_report import TestReport
from XAMS.Tool.test_excel import TestExcel
from XAMS.Trade.Bond.test_trade import TestTrade
from XAMS.conftest import report_list, asset_list, trade_list


class TestAuto:
    def test_auto(self, stagemark):
        self.list = TestExcel()
        self.report = TestReport()
        self.asset = TestAsset()
        self.trade = TestTrade()
        count = len(self.list.code_list())
        n = 0
        sum_report = 0
        sum_asset = 0
        sum_trade = 0
        sum_product = 0
        simulate = 0
        compare = 0
        while n < count:
            code = self.list.code_list()[n]
            menu = self.list.group_ele_dic().get(code)
            value = self.list.group_value_dic().get(code)
            step = self.list.group_step_dic().get(code)
            test_goal = self.list.group_goal_dic().get(code)
            if test_goal == '模拟操作':
                second_menu = f'{menu[1]}-{menu[2]}'
                simulate = simulate + 1
                if len(step[0]) > 0:
                    step = 1
                    if second_menu in report_list:
                        self.report.test_universal(stagemark, menu, value, test_goal, step)
                        sum_report = sum_report + 1
                    elif second_menu in asset_list:
                        self.asset.test_universal(stagemark, menu, value, test_goal, step)
                        sum_asset = sum_asset + 1
                    elif second_menu in trade_list:
                        self.trade.test_universal(stagemark, menu, value, test_goal, step)
                        sum_trade = sum_trade + 1
                    else:
                        print("该界面模拟操作暂不支持，请修改用例")
                        return False
                else:
                    step = None
                    if second_menu in report_list:
                        self.report.test_universal(stagemark, menu, value, test_goal, step)
                        sum_report = sum_report + 1
                    elif second_menu in asset_list:
                        self.asset.test_universal(stagemark, menu, value, test_goal, step)
                        sum_asset = sum_asset + 1
                    elif second_menu in trade_list:
                        self.trade.test_universal(stagemark, menu, value, test_goal, step)
                        sum_trade = sum_trade + 1
                    else:
                        print("该界面模拟操作暂不支持，请修改用例")
                        return False
            elif test_goal == '升级对比':
                second_menu = f'{menu[2]}-{menu[3]}'
                compare = compare + 1
                if second_menu in report_list:
                    self.report.test_universal(stagemark, menu, value, test_goal, step)
                    sum_report = sum_report + 1
                else:
                    print("该界面升级对比暂不支持，请修改用例")
                    return False
            else:
                print("该测试目的暂不支持，请修改用例")
                return False
            n = n + 1
        print(f'报表案例执行完毕，共{sum_report}条')
        print(f'资产案例执行完毕，共{sum_asset}条')
        print(f'交易案例执行完毕，共{sum_trade}条')
        print(f'自动化案例执行完毕，共{count}条，包含模拟操作{simulate}条，升级对比{compare}条')
