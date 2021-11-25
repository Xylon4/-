# 现金流缺口表(新)自动化测试用例
# 功能描述：统计投组头寸信息
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet24
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class CashGap(BasePageXams):
    # 模拟操作自动化案例
    def cash_gap_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu().get(menu[0]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu().get(f'{menu[0]}-{menu[1]}'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 2
        while n < l:
            if menu[n] == '导出':
                self.findxpath_click(self.base.sheet_xpath_dic(sheet24).get(menu[n]))
            elif menu[n] == '投组单元':
                if value[n] == '置空':
                    unit = self.findxpath(self.base.sheet_xpath_dic(sheet24).get(menu[n]))
                    unit.send_keys(Keys.CONTROL, 'a')
                    unit.send_keys(Keys.BACK_SPACE)
                else:
                    unit = self.findxpath(self.base.sheet_xpath_dic(sheet24).get(menu[n]))
                    unit.send_keys(Keys.CONTROL, 'a')
                    unit.send_keys(Keys.BACK_SPACE)
                    unit.send_keys(value[n])
                    sleep(1)
                    self.findxpath_click(self.base.sheet_xpath_dic(sheet24).get('投组下拉选择'))
            elif menu[n] == '开始日期':
                if value[n] == '置空':
                    startdate = self.findxpath(self.base.sheet_xpath_dic(sheet24).get(menu[n]))
                    startdate.send_keys(Keys.CONTROL, 'a')
                    startdate.send_keys(Keys.BACK_SPACE)
                else:
                    startdate = self.findxpath(self.base.sheet_xpath_dic(sheet24).get(menu[n]))
                    startdate.send_keys(Keys.CONTROL, 'a')
                    startdate.send_keys(Keys.BACK_SPACE)
                    startdate.send_keys(value[n])
            elif menu[n] == '结束日期':
                if value[n] == '置空':
                    enddate = self.findxpath(self.base.sheet_xpath_dic(sheet24).get(menu[n]))
                    enddate.send_keys(Keys.CONTROL, 'a')
                    enddate.send_keys(Keys.BACK_SPACE)
                else:
                    enddate = self.findxpath(self.base.sheet_xpath_dic(sheet24).get(menu[n]))
                    enddate.send_keys(Keys.CONTROL, 'a')
                    enddate.send_keys(Keys.BACK_SPACE)
                    enddate.send_keys(value[n])
            elif menu[n] == '搜索':
                self.findxpath_click(self.base.sheet_xpath_dic(sheet24).get(menu[n]))
                # sleep(1)  # 强制等待用来过渡到显式等待
                # wait = (By.XPATH, self.base.sheet_xpath_dic(sheet24).get('加载等待'))
                # self.wait_for_miss(120, wait)
            else:
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            n = n + 1
        return True