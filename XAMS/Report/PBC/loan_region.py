# 表2-3贷款分地区统计表自动化测试用例
# 功能描述：统计投组贷款地区分布
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet12, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class LoanRegion(BasePageXams):
    # 模拟操作自动化案例
    def loan_region_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet12]
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
                wait = (By.XPATH, targetsheet.get('加载等待'))
                if menu[n] == '导出':
                    findelement.click()
                elif menu[n] == '投组单元':
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        self.findxpath_sendkey(targetsheet.get('投组单元'), value[n])
                        sleep(1)
                        self.findxpath_click(targetsheet.get('投组下拉选择'))
                elif menu[n] == '年':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(value[n])
                elif menu[n] == '月':
                    findelement.click()
                    if value[n] == '1':
                        self.findxpath_click(targetsheet.get('一月'))
                    elif value[n] == '2':
                        self.findxpath_click(targetsheet.get('二月'))
                    elif value[n] == '3':
                        self.findxpath_click(targetsheet.get('三月'))
                    elif value[n] == '4':
                        self.findxpath_click(targetsheet.get('四月'))
                    elif value[n] == '5':
                        self.findxpath_click(targetsheet.get('五月'))
                    elif value[n] == '6':
                        self.findxpath_click(targetsheet.get('六月'))
                    elif value[n] == '7':
                        self.findxpath_click(targetsheet.get('七月'))
                    elif value[n] == '8':
                        self.findxpath_click(targetsheet.get('八月'))
                    elif value[n] == '9':
                        self.findxpath_click(targetsheet.get('九月'))
                    elif value[n] == '10':
                        self.findxpath_click(targetsheet.get('十月'))
                    elif value[n] == '11':
                        self.findxpath_click(targetsheet.get('十一月'))
                    elif value[n] == '12':
                        self.findxpath_click(targetsheet.get('十二月'))
                    else:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                elif menu[n] == '搜索':
                    findelement.click()
                elif menu[n] == '统计维度':
                    findelement.click()
                    if value[n] == '市值（不含应收未收利息、不含应收未收本金）':
                        self.findxpath_click(targetsheet.get(value[n]))
                    elif value[n] == '市值（含应收未收本金，不含应收未收利息）':
                        self.findxpath_click(targetsheet.get(value[n]))
                    else:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
            n = n + 1
        return True

    # 数据对比自动化案例
    def loan_region_compare(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet12]
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu(basedata[0]).get(menu[2]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu(basedata[0]).get(f'{menu[2]}-{menu[3]}'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 4
        while n < l:
            if menu[n] not in self.base.operable_list(basedata[0], basedata[1]):
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            else:
                targetsheet = self.base.sheet_xpath_dic(basedata[0], basedata[1])
                findelement = self.findxpath(targetsheet.get(menu[n]))
                wait = (By.XPATH, targetsheet.get('加载等待'))
                if menu[n] == '导出':
                    findelement.click()
                elif menu[n] == '投组单元':
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        self.findxpath_sendkey(targetsheet.get('投组单元'), value[n])
                        sleep(1)
                        self.findxpath_click(targetsheet.get('投组下拉选择'))
                elif menu[n] == '年':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(value[n])
                elif menu[n] == '月':
                    findelement.click()
                    if value[n] == '1':
                        self.findxpath_click(targetsheet.get('一月'))
                    elif value[n] == '2':
                        self.findxpath_click(targetsheet.get('二月'))
                    elif value[n] == '3':
                        self.findxpath_click(targetsheet.get('三月'))
                    elif value[n] == '4':
                        self.findxpath_click(targetsheet.get('四月'))
                    elif value[n] == '5':
                        self.findxpath_click(targetsheet.get('五月'))
                    elif value[n] == '6':
                        self.findxpath_click(targetsheet.get('六月'))
                    elif value[n] == '7':
                        self.findxpath_click(targetsheet.get('七月'))
                    elif value[n] == '8':
                        self.findxpath_click(targetsheet.get('八月'))
                    elif value[n] == '9':
                        self.findxpath_click(targetsheet.get('九月'))
                    elif value[n] == '10':
                        self.findxpath_click(targetsheet.get('十月'))
                    elif value[n] == '11':
                        self.findxpath_click(targetsheet.get('十一月'))
                    elif value[n] == '12':
                        self.findxpath_click(targetsheet.get('十二月'))
                    else:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                elif menu[n] == '搜索':
                    findelement.click()
                elif menu[n] == '统计维度':
                    findelement.click()
                    if value[n] == '市值（不含应收未收利息、不含应收未收本金）':
                        self.findxpath_click(targetsheet.get(value[n]))
                    elif value[n] == '市值（含应收未收本金，不含应收未收利息）':
                        self.findxpath_click(targetsheet.get(value[n]))
                    else:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
            n = n + 1
        # 触发判断定位点
        m = self.base.checkpoint_list(basedata[0], basedata[1])
        point = self.findxpath(self.base.checkpoint_dic(basedata[0], basedata[1]).get(m[0]))
        # 旧环境的记录值
        p = len(m)
        if point.is_displayed():
            i = 0
            x = {}
            while i < p:
                o = self.findxpath(self.base.checkpoint_dic(basedata[0], basedata[1]).get(m[i])).get_attribute('textContent')
                x.setdefault(m[i], o)
                i = i + 1
        else:
            print('案例最终结果不存在搜索数据，请合理调整步骤')
            return False
        # 关闭浏览器
        self.end()
        # 新环境重复操作
        self.start(value[1])
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu(basedata[0]).get(menu[2]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu(basedata[0]).get(f'{menu[2]}-{menu[3]}'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 4
        while n < l:
            if menu[n] not in self.base.operable_list(basedata[0], basedata[1]):
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            else:
                targetsheet = self.base.sheet_xpath_dic(basedata[0], basedata[1])
                findelement = self.findxpath(targetsheet.get(menu[n]))
                wait = (By.XPATH, targetsheet.get('加载等待'))
                if menu[n] == '导出':
                    findelement.click()
                elif menu[n] == '投组单元':
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        self.findxpath_sendkey(targetsheet.get('投组单元'), value[n])
                        sleep(1)
                        self.findxpath_click(targetsheet.get('投组下拉选择'))
                elif menu[n] == '年':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(value[n])
                elif menu[n] == '月':
                    findelement.click()
                    if value[n] == '1':
                        self.findxpath_click(targetsheet.get('一月'))
                    elif value[n] == '2':
                        self.findxpath_click(targetsheet.get('二月'))
                    elif value[n] == '3':
                        self.findxpath_click(targetsheet.get('三月'))
                    elif value[n] == '4':
                        self.findxpath_click(targetsheet.get('四月'))
                    elif value[n] == '5':
                        self.findxpath_click(targetsheet.get('五月'))
                    elif value[n] == '6':
                        self.findxpath_click(targetsheet.get('六月'))
                    elif value[n] == '7':
                        self.findxpath_click(targetsheet.get('七月'))
                    elif value[n] == '8':
                        self.findxpath_click(targetsheet.get('八月'))
                    elif value[n] == '9':
                        self.findxpath_click(targetsheet.get('九月'))
                    elif value[n] == '10':
                        self.findxpath_click(targetsheet.get('十月'))
                    elif value[n] == '11':
                        self.findxpath_click(targetsheet.get('十一月'))
                    elif value[n] == '12':
                        self.findxpath_click(targetsheet.get('十二月'))
                    else:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                elif menu[n] == '搜索':
                    findelement.click()
                elif menu[n] == '统计维度':
                    findelement.click()
                    if value[n] == '市值（不含应收未收利息、不含应收未收本金）':
                        self.findxpath_click(targetsheet.get(value[n]))
                    elif value[n] == '市值（含应收未收本金，不含应收未收利息）':
                        self.findxpath_click(targetsheet.get(value[n]))
                    else:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
            n = n + 1
        # 新环境的记录值
        r = 0
        y = {}
        while r < p:
            s = self.findxpath(self.base.checkpoint_dic(basedata[0], basedata[1]).get(m[r])).get_attribute('textContent')
            y.setdefault(m[r], s)
            r = r + 1
        # 局部校验
        z = 0
        if x.get(m[z]) == y.get(m[z]):
            # 全局校验
            t = 0
            while t < p:
                if x.get(m[t]) == y.get(m[t]):
                    t = t + 1
                else:
                    print(f'对比结果：{m[t]}：{x.get(m[t])}数据核对不一致，请检查并联系开发')
                    return False
        else:
            print(f'对比结果：{m[z]}：{x.get(m[z])}数据核对不一致，请检查并联系开发')
            return False
        print('对比结果：数据核对一致')
        return True