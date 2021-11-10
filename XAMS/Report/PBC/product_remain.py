# 表1-1产品募集余额统计表自动化测试用例
# 功能描述：统计投组余额
from time import sleep

from selenium.webdriver.common.keys import Keys

from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class ProductRemain(BasePageXams):
    # 自动化测试工具案例
    def product_remain_excel(self, menu, value):
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
                self.findxpath_click(self.base.product_remain_xpath().get(menu[n]))
            elif menu[n] == '投组单元':
                if value[n] == '置空':
                    unit = self.findxpath(self.base.product_remain_xpath().get(menu[n]))
                    unit.send_keys(Keys.CONTROL, 'a')
                    unit.send_keys(Keys.BACK_SPACE)
                else:
                    self.findxpath_sendkey(self.base.product_remain_xpath().get('投组单元'), value[n])
                    sleep(1)
                    self.findxpath_click(self.base.product_remain_xpath().get('投组下拉选择'))
            elif menu[n] == '年':
                year = self.findxpath(self.base.product_remain_xpath().get(menu[n]))
                year.send_keys(Keys.CONTROL, 'a')
                year.send_keys(Keys.BACK_SPACE)
                year.send_keys(value[n])
            elif menu[n] == '月':
                self.findxpath_click(self.base.product_remain_xpath().get(menu[n]))
                if value[n] == '1':
                    self.findxpath_click(self.base.product_remain_xpath().get('一月'))
                elif value[n] == '2':
                    self.findxpath_click(self.base.product_remain_xpath().get('二月'))
                elif value[n] == '3':
                    self.findxpath_click(self.base.product_remain_xpath().get('三月'))
                elif value[n] == '4':
                    self.findxpath_click(self.base.product_remain_xpath().get('四月'))
                elif value[n] == '5':
                    self.findxpath_click(self.base.product_remain_xpath().get('五月'))
                elif value[n] == '6':
                    self.findxpath_click(self.base.product_remain_xpath().get('六月'))
                elif value[n] == '7':
                    self.findxpath_click(self.base.product_remain_xpath().get('七月'))
                elif value[n] == '8':
                    self.findxpath_click(self.base.product_remain_xpath().get('八月'))
                elif value[n] == '9':
                    self.findxpath_click(self.base.product_remain_xpath().get('九月'))
                elif value[n] == '10':
                    self.findxpath_click(self.base.product_remain_xpath().get('十月'))
                elif value[n] == '11':
                    self.findxpath_click(self.base.product_remain_xpath().get('十一月'))
                elif value[n] == '12':
                    self.findxpath_click(self.base.product_remain_xpath().get('十二月'))
            elif menu[n] == '查询':
                self.findxpath_click(self.base.product_remain_xpath().get(menu[n]))
            n = n + 1
        return True

    # 数据对比自动化案例
    def product_remain_compare(self, menu, value):
        print(menu)
        print(value)
        print(value[0])
        self.start(value[1])
        return True
