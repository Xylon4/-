# 估值表自动化测试用例
# 功能描述：投组每日估值对账数据
from time import sleep

from selenium.webdriver.common.keys import Keys

from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageFsfa


class Valuation(BasePageFsfa):
    # 自动化测试工具案例
    def valuation_excel(self, menu, value):
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
                self.findxpath_click(self.base.valuation_xpath().get(menu[n]))
            elif menu[n] == 'Excel(当前页)':
                self.findxpath_click(self.base.valuation_xpath().get(menu[n]))
            elif menu[n] == 'Excel(所有数据)':
                self.findxpath_click(self.base.valuation_xpath().get(menu[n]))
            elif menu[n] == '批量导出':
                self.findxpath_click(self.base.valuation_xpath().get(menu[n]))
            elif menu[n] == '生成估值表':
                self.findxpath_click(self.base.valuation_xpath().get(menu[n]))
            elif menu[n] == '查询日期':
                if value[n] == '置空':
                    date = self.findxpath(self.base.valuation_xpath().get(menu[n]))
                    date.send_keys(Keys.CONTROL, 'a')
                    date.send_keys(Keys.BACK_SPACE)
                else:
                    date = self.findxpath(self.base.valuation_xpath().get(menu[n]))
                    date.send_keys(Keys.CONTROL, 'a')
                    date.send_keys(Keys.BACK_SPACE)
                    date.send_keys(value[n])
            elif menu[n] == '投组单元':
                self.findxpath_sendkey(self.base.valuation_xpath().get('投组单元'), value[n])
                sleep(1)
                self.findxpath_click(self.base.valuation_xpath().get('投组下拉选择'))
            elif menu[n] == '搜索':
                self.findxpath_click(self.base.valuation_xpath().get(menu[n]))
                sleep(1)
            n = n + 1
        return True
