# 利润表自动化测试用例
# 功能描述：查询利润表
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet47, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams
import math


class ProfitCarryOverEntry(BasePageXams):
    # 模拟操作自动化案例-浙商
    def profit_carry_over_entry_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet47]
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
                               '搜索'
                               ]:
                    findelement.click()
                    if menu[n] in ['搜索']:
                        self.wait_for_miss(120, wait)
                # 所有操作为"输入"的元素
                elif menu[n] in ['查询日期',
                                 '查询起始日期',
                                 '查询结束日期'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['投组单元',
                                 '所在账户'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        sleep(1)
                        findelement.send_keys(value[n] + Keys.SPACE + Keys.BACK_SPACE)
                        sleep(1)
                        if menu[n] in ['投组单元', '所在账户']:
                            self.findxpath_click(targetsheet.get('投组下拉选择'))
                # 所有操作为"点击后选择"的元素
                elif menu[n] in ['查询方式',
                                 '查询频率'
                                 ]:
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    else:
                        findelement.click()
                        self.findxpath_click(f'//li[text()=" {value[n]}"]')
            n = n + 1
        return True

    # 升级对比自动化案例-浙商
    def profit_carry_over_entry_compare(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet47]
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu(basedata[0]).get(menu[2]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu(basedata[0]).get(f'{menu[2]}-{menu[3]}'))
        targetsheet = self.base.sheet_xpath_dic(basedata[0], basedata[1])
        wait = (By.XPATH, targetsheet.get('加载等待'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 4
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
                               '搜索'
                               ]:
                    findelement.click()
                    if menu[n] in ['搜索']:
                        self.wait_for_miss(120, wait)
                # 所有操作为"输入"的元素
                elif menu[n] in ['日期', '翻页']:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                    if menu[n] == '翻页':
                        findelement.send_keys(Keys.ENTER)
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['投组单元',
                                 '金融工具代码'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        sleep(1)
                        findelement.send_keys(value[n] + Keys.SPACE + Keys.BACK_SPACE)
                        sleep(1)
                        if menu[n] in ['投组单元']:
                            self.findxpath_click(targetsheet.get('投组下拉选择'))
                        elif menu[n] in ['金融工具代码']:
                            self.findxpath_click(f'//li[contains(text(),"{value[n]}")]')
            n = n + 1
        # 触发判断定位点
