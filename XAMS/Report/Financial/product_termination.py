# 产品终止信息表自动化测试用例
# 功能描述：统计投组产品终止数据
from time import sleep

from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet18, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class ProductTermination(BasePageXams):
    # 模拟操作自动化案例
    def product_termination_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet18]
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu(basedata[0]).get(menu[1]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu(basedata[0]).get(f'{menu[1]}-{menu[2]}'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 3
        while n < l:
            if menu[n] not in self.base.operable_list(basedata[0], basedata[1]):
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            else:
                targetsheet = self.base.sheet_xpath_dic(basedata[0], basedata[1])
                findelement = self.findxpath(targetsheet.get(menu[n]))
                if menu[n] == '导出':
                    findelement.click()
                elif menu[n] == '批量导出':
                    findelement.click()
                elif menu[n] == '投组':
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                        sleep(1)
                        self.findxpath_click(targetsheet.get('投组下拉选择'))
                elif menu[n] == '产品名称/代码':
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                elif menu[n] == '搜索':
                    findelement.click()
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
            n = n + 1
        return True
