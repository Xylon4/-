# 资产要素登记自动化测试用例
# 功能描述：统计资产信息
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet20, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class AssetRegistration(BasePageXams):
    # 模拟操作自动化案例
    def asset_registration_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu(Excel_basedata_zs).get(menu[0]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu(Excel_basedata_zs).get(f'{menu[0]}-{menu[1]}'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 2
        while n < l:
            targetsheet = self.base.sheet_xpath_dic(Excel_basedata_zs, sheet20)
            findelement = self.findxpath(targetsheet.get(menu[n]))
            wait = (By.XPATH, targetsheet.get('加载等待'))
            if menu[n] == '导出':
                findelement.click()
                self.wait_for_miss(120, wait)
            elif menu[n] == '行内资产/负债编码':
                if value[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(value[n])
                    sleep(1)
                    findelement.send_keys(Keys.ARROW_DOWN)
                    findelement.send_keys(Keys.ENTER)
            elif menu[n] == '开始日期':
                if value[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(value[n])
            elif menu[n] == '结束日期':
                if value[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(value[n])
            elif menu[n] == '搜索':
                findelement.click()
                sleep(1)  # 强制等待用来过渡到显式等待
                wait = (By.XPATH, targetsheet.get('加载等待'))
                self.wait_for_miss(120, wait)
            else:
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            n = n + 1
        return True
