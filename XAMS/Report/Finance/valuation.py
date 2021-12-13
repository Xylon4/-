# 估值表自动化测试用例
# 功能描述：投组每日估值对账数据
from time import sleep

from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import Excel_basedata_zs, sheet4
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class Valuation(BasePageXams):
    # 自动化测试工具案例
    def valuation_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu(Excel_basedata_zs).get(menu[1]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu(Excel_basedata_zs).get(f'{menu[1]}-{menu[2]}'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 3
        while n < l:
            targetsheet = self.base.sheet_xpath_dic(Excel_basedata_zs, sheet4)
            findelement = self.findxpath(targetsheet.get(menu[n]))
            if menu[n] == '导出':
                findelement.click()
            elif menu[n] == 'Excel(当前页)':
                findelement.click()
            elif menu[n] == 'Excel(所有数据)':
                findelement.click()
            elif menu[n] == '批量导出':
                findelement.click()
            elif menu[n] == '生成估值表':
                findelement.click()
            elif menu[n] == '查询日期':
                if value[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(value[n])
            elif menu[n] == '投组单元':
                if value[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    self.findxpath_sendkey(targetsheet.get('投组单元'), value[n])
                    sleep(1)
                    self.findxpath_click(targetsheet.get('投组下拉选择'))
            elif menu[n] == '搜索':
                findelement.click()
                sleep(1)
            n = n + 1
        return True
