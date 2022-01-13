# 待复核交易指令自动化测试用例
# 功能描述：待复核交易指令处理
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet42, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class TransactionsReview(BasePageXams):
    # 模拟操作自动化案例-浙商
    def transactions_review_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet42]
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu(basedata[0]).get(menu[1]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu(basedata[0]).get(f'{menu[1]}-{menu[2]}'))
        targetsheet = self.base.sheet_xpath_dic(basedata[0], basedata[1])
        wait = (By.XPATH, targetsheet.get('加载等待'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 3
        while n < l:
            if menu[n] not in self.base.operable_list(basedata[0], basedata[1]):
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            else:
                findelement = self.findxpath(targetsheet.get(menu[n]))
                # 所有操作为"点击"或"勾选"的元素
                if menu[n] in ['导出',
                               'Excel(当前页)',
                               'Excel(所有数据)',
                               '复核',
                               '继续',
                               '抹账',
                               '提醒交易员',
                               '交易轧差',
                               '查看轧差交易',
                               '删除轧差交易',
                               '查看交易详情',
                               '可视化流程',
                               '搜索',
                               '搜索_单选框',
                               '搜索_全选框',
                               '高级查询',
                               '高级查询_查询',
                               '高级查询_重置',
                               '高级查询_返回',
                               '确认_是',
                               '确认_否'
                               ]:
                    findelement.click()
                # 所有操作为"输入"的元素
                elif menu[n] in ['指令号',
                                 '结算日期',
                                 '高级查询_结算开始日',
                                 '高级查询_结算结束日',
                                 '高级查询_交易单号'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['资产类型',
                                 '高级查询_资产类型',
                                 '高级查询_业务类型',
                                 '高级查询_资产代码',
                                 '高级查询_投组单元'
                                 ]:
                    findelement.send_keys(value[n])
            n = n + 1
        return True
