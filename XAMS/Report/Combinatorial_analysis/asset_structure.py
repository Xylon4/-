# 资产结构分析表自动化测试用例
# 功能描述：统计投组资产结构分布
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet27
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class AssetStructure(BasePageXams):
    # 模拟操作自动化案例
    def asset_structure_excel(self, menu, value):
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
            wait = (By.XPATH, self.base.sheet_xpath_dic(sheet27).get('加载等待'))
            if menu[n] == '导出':
                self.findxpath_click(self.base.sheet_xpath_dic(sheet27).get(menu[n]))
            elif menu[n] == 'Excel(当前页)':
                self.findxpath_click(self.base.sheet_xpath_dic(sheet27).get(menu[n]))
                self.wait_for_miss(120, wait)
            elif menu[n] == 'Excel(所有数据)':
                self.findxpath_click(self.base.sheet_xpath_dic(sheet27).get(menu[n]))
                self.wait_for_miss(120, wait)
            elif menu[n] == '全部展开':
                tree = self.findxpath(self.base.sheet_xpath_dic(sheet27).get(menu[n]))
                if tree.get_attribute('textContent') == menu[n]:
                    tree.click()
                    self.wait_for_miss(120, wait)
                else:
                    print(f'请检查当前按钮显示是否为"{menu[n]}"，若显示一致，请联系测试开发')
                    return False
            elif menu[n] == '一键收起':
                tree = self.findxpath(self.base.sheet_xpath_dic(sheet27).get(menu[n]))
                if tree.get_attribute('textContent') == menu[n]:
                    tree.click()
                    self.wait_for_miss(120, wait)
                else:
                    print(f'请检查当前按钮显示是否为"{menu[n]}"，若显示一致，请联系测试开发')
                    return False
            elif menu[n] == '是否穿透':
                if value[n] not in ['是', '否']:
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
                else:
                    penetration = self.findxpath(self.base.sheet_xpath_dic(sheet27).get(menu[n]))
                    penetration.send_keys(Keys.CONTROL, 'a')
                    penetration.send_keys(Keys.BACK_SPACE)
                    penetration.send_keys(value[n])
            elif menu[n] == '所属投组':
                if value[n] == '置空':
                    unit = self.findxpath(self.base.sheet_xpath_dic(sheet27).get(menu[n]))
                    unit.send_keys(Keys.CONTROL, 'a')
                    unit.send_keys(Keys.BACK_SPACE)
                else:
                    unit = self.findxpath(self.base.sheet_xpath_dic(sheet27).get(menu[n]))
                    unit.send_keys(Keys.CONTROL, 'a')
                    unit.send_keys(Keys.BACK_SPACE)
                    unit.send_keys(value[n])
                    sleep(1)
                    self.findxpath_click(self.base.sheet_xpath_dic(sheet27).get('投组下拉选择'))
            elif menu[n] == '开始日期':
                if value[n] == '置空':
                    startdate = self.findxpath(self.base.sheet_xpath_dic(sheet27).get(menu[n]))
                    startdate.send_keys(Keys.CONTROL, 'a')
                    startdate.send_keys(Keys.BACK_SPACE)
                else:
                    startdate = self.findxpath(self.base.sheet_xpath_dic(sheet27).get(menu[n]))
                    startdate.send_keys(Keys.CONTROL, 'a')
                    startdate.send_keys(Keys.BACK_SPACE)
                    startdate.send_keys(value[n])
            elif menu[n] == '结束日期':
                if value[n] == '置空':
                    startdate = self.findxpath(self.base.sheet_xpath_dic(sheet27).get(menu[n]))
                    startdate.send_keys(Keys.CONTROL, 'a')
                    startdate.send_keys(Keys.BACK_SPACE)
                else:
                    startdate = self.findxpath(self.base.sheet_xpath_dic(sheet27).get(menu[n]))
                    startdate.send_keys(Keys.CONTROL, 'a')
                    startdate.send_keys(Keys.BACK_SPACE)
                    startdate.send_keys(value[n])
            elif menu[n] == '数据来源':
                self.findxpath_click(self.base.sheet_xpath_dic(sheet27).get(menu[n]))
                if value[n] == '估值核算':
                    self.findxpath_click(self.base.sheet_xpath_dic(sheet27).get(value[n]))
                elif value[n] == '理财资管':
                    self.findxpath_click(self.base.sheet_xpath_dic(sheet27).get(value[n]))
                else:
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
            elif menu[n] == '搜索':
                self.findxpath_click(self.base.sheet_xpath_dic(sheet27).get(menu[n]))
                # 搜索结束判断依据缺失，产品要改
            elif menu[n] == '图形展示':
                self.findxpath_click(self.base.sheet_xpath_dic(sheet27).get(menu[n]))
                if value[n][1] == '查询':
                    searchdate = self.findxpath(self.base.sheet_xpath_dic(sheet27).get('查询日期'))
                    searchdate.send_keys(Keys.CONTROL, 'a')
                    searchdate.send_keys(Keys.BACK_SPACE)
                    searchdate.send_keys(value[n][0])
                    self.findxpath_click(self.base.sheet_xpath_dic(sheet27).get(value[n][1]))
                    sleep(1)
                elif value[n][1] == '返回':
                    searchdate = self.findxpath(self.base.sheet_xpath_dic(sheet27).get('查询日期'))
                    searchdate.send_keys(Keys.CONTROL, 'a')
                    searchdate.send_keys(Keys.BACK_SPACE)
                    searchdate.send_keys(value[n][0])
                    self.findxpath_click(self.base.sheet_xpath_dic(sheet27).get(value[n][1]))
                else:
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
            else:
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            n = n + 1
        return True
