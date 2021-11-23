# 投组单元资产明细表(穿透)自动化测试用例
# 功能描述：统计投组资产及底层资产信息
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet22
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class AssetDetailPenetration(BasePageXams):
    # 模拟操作自动化案例
    def asset_detail_penetration_excel(self, menu, value):
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
                self.findxpath_click(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
            elif menu[n] == 'Excel(当前页)':
                self.findxpath_click(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                wait = (By.XPATH, self.base.sheet_xpath_dic(sheet22).get('加载等待'))
                self.wait_for_miss(120, wait)
            elif menu[n] == 'Excel(所有数据)':
                self.findxpath_click(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                wait = (By.XPATH, self.base.sheet_xpath_dic(sheet22).get('加载等待'))
                self.wait_for_miss(120, wait)
            elif menu[n] == '资产代码':
                if value[n] == '置空':
                    asset = self.findxpath(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                    asset.send_keys(Keys.CONTROL, 'a')
                    asset.send_keys(Keys.BACK_SPACE)
                else:
                    asset = self.findxpath(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                    asset.send_keys(Keys.CONTROL, 'a')
                    asset.send_keys(Keys.BACK_SPACE)
                    asset.send_keys(value[n])
                    sleep(1)
                    asset.send_keys(Keys.ARROW_DOWN)
                    asset.send_keys(Keys.ENTER)
            elif menu[n] == '资产类型':
                if value[n] == '置空':
                    assettype = self.findxpath(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                    assettype.send_keys(Keys.CONTROL, 'a')
                    assettype.send_keys(Keys.BACK_SPACE)
                else:
                    assettype = self.findxpath(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                    assettype.send_keys(Keys.CONTROL, 'a')
                    assettype.send_keys(Keys.BACK_SPACE)
                    assettype.send_keys(value[n])
                    sleep(1)
                    self.findxpath_click(self.base.sheet_xpath_dic(sheet22).get('资产类型选择'))
            elif menu[n] == '开始日期':
                if value[n] == '置空':
                    asset = self.findxpath(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                    asset.send_keys(Keys.CONTROL, 'a')
                    asset.send_keys(Keys.BACK_SPACE)
                else:
                    asset = self.findxpath(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                    asset.send_keys(Keys.CONTROL, 'a')
                    asset.send_keys(Keys.BACK_SPACE)
                    asset.send_keys(value[n])
            elif menu[n] == '结束日期':
                if value[n] == '置空':
                    asset = self.findxpath(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                    asset.send_keys(Keys.CONTROL, 'a')
                    asset.send_keys(Keys.BACK_SPACE)
                else:
                    asset = self.findxpath(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                    asset.send_keys(Keys.CONTROL, 'a')
                    asset.send_keys(Keys.BACK_SPACE)
                    asset.send_keys(value[n])
            elif menu[n] == '是否穿透':
                if value[n] not in ['是', '否']:
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
                else:
                    penetration = self.findxpath(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                    penetration.send_keys(Keys.CONTROL, 'a')
                    penetration.send_keys(Keys.BACK_SPACE)
                    penetration.send_keys(value[n])
            elif menu[n] == '投组单元':
                if value[n] == '置空':
                    unit = self.findxpath(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                    unit.send_keys(Keys.CONTROL, 'a')
                    unit.send_keys(Keys.BACK_SPACE)
                else:
                    unit = self.findxpath(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                    unit.send_keys(Keys.CONTROL, 'a')
                    unit.send_keys(Keys.BACK_SPACE)
                    unit.send_keys(value[n])
                    sleep(1)
                    self.findxpath_click(self.base.sheet_xpath_dic(sheet22).get('投组下拉选择'))
            elif menu[n] == '估值偏离度符号':
                input = self.findxpath(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                if value[n] == '置空':
                    input.send_keys(Keys.CONTROL, 'a')
                    input.send_keys(Keys.BACK_SPACE)
                elif value[n] == '<':
                    input.send_keys(Keys.CONTROL, 'a')
                    input.send_keys(Keys.BACK_SPACE)
                    input.send_keys(value[n])
                    self.findxpath_click(self.base.sheet_xpath_dic(sheet22).get('符号下拉选择'))
                elif value[n] == '=':
                    input.send_keys(Keys.CONTROL, 'a')
                    input.send_keys(Keys.BACK_SPACE)
                    input.send_keys(value[n])
                    self.findxpath_click(self.base.sheet_xpath_dic(sheet22).get('符号下拉选择'))
                elif value[n] == '>':
                    input.send_keys(Keys.CONTROL, 'a')
                    input.send_keys(Keys.BACK_SPACE)
                    input.send_keys(value[n])
                    self.findxpath_click(self.base.sheet_xpath_dic(sheet22).get('符号下拉选择'))
                else:
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
            elif menu[n] == '估值偏离度数值':
                if value[n] == '置空':
                    val = self.findxpath(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                    val.send_keys(Keys.CONTROL, 'a')
                    val.send_keys(Keys.BACK_SPACE)
                else:
                    val = self.findxpath(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                    val.send_keys(Keys.CONTROL, 'a')
                    val.send_keys(Keys.BACK_SPACE)
                    val.send_keys(value[n])
            elif menu[n] == '搜索':
                self.findxpath_click(self.base.sheet_xpath_dic(sheet22).get(menu[n]))
                sleep(1)  # 强制等待用来过渡到显式等待
                wait = (By.XPATH, self.base.sheet_xpath_dic(sheet22).get('加载等待'))
                self.wait_for_miss(120, wait)
            else:
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            n = n + 1
        return True
