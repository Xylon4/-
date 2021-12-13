# 投组单元资产明细表(穿透)自动化测试用例
# 功能描述：统计投组资产及底层资产信息
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet22, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class AssetDetailPenetration(BasePageXams):
    # 模拟操作自动化案例
    def asset_detail_penetration_excel(self, menu, findelementue):
        print(menu)
        print(findelementue)
        self.base = TestExcel()
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu(Excel_basedata_zs).get(menu[1]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu(Excel_basedata_zs).get(f'{menu[1]}-{menu[2]}'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 3
        while n < l:
            targetsheet = self.base.sheet_xpath_dic(Excel_basedata_zs, sheet22)
            findelement = self.findxpath(targetsheet.get(menu[n]))
            wait = (By.XPATH, targetsheet.get('加载等待'))
            if menu[n] == '导出':
                findelement.click()
            elif menu[n] == 'Excel(当前页)':
                findelement.click()
                self.wait_for_miss(120, wait)
            elif menu[n] == 'Excel(所有数据)':
                findelement.click()
                self.wait_for_miss(120, wait)
            elif menu[n] == '资产代码':
                if findelementue[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(findelementue[n])
                    sleep(1)
                    findelement.send_keys(Keys.ARROW_DOWN)
                    findelement.send_keys(Keys.ENTER)
            elif menu[n] == '资产类型':
                if findelementue[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(findelementue[n])
                    sleep(1)
                    self.findxpath_click(targetsheet.get('资产类型选择'))
            elif menu[n] == '开始日期':
                if findelementue[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(findelementue[n])
            elif menu[n] == '结束日期':
                if findelementue[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(findelementue[n])
            elif menu[n] == '是否穿透':
                if findelementue[n] not in ['是', '否']:
                    print(f'值"{findelementue[n]}"输入错误，请检查')
                    return False
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(findelementue[n])
            elif menu[n] == '投组单元':
                if findelementue[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(findelementue[n])
                    sleep(1)
                    self.findxpath_click(targetsheet.get('投组下拉选择'))
            elif menu[n] == '估值偏离度符号':
                if findelementue[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                elif findelementue[n] == '<':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(findelementue[n])
                    self.findxpath_click(targetsheet.get('符号下拉选择'))
                elif findelementue[n] == '=':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(findelementue[n])
                    self.findxpath_click(targetsheet.get('符号下拉选择'))
                elif findelementue[n] == '>':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(findelementue[n])
                    self.findxpath_click(targetsheet.get('符号下拉选择'))
                else:
                    print(f'值"{findelementue[n]}"输入错误，请检查')
                    return False
            elif menu[n] == '估值偏离度数值':
                if findelementue[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(findelementue[n])
            elif menu[n] == '搜索':
                findelement.click()
                sleep(1)  # 强制等待用来过渡到显式等待
                self.wait_for_miss(120, wait)
            else:
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            n = n + 1
        return True
