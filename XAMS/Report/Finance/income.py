# 利润表自动化测试用例
# 功能描述：查询利润表
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet47, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams
import math


class Income(BasePageXams):
    # 模拟操作自动化案例-浙商
    def income_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet47]
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu(basedata[0]).get(menu[1]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu(basedata[0]).get(f'{menu[1]}-{menu[2]}'))
        targetsheet = self.base.sheet_xpath_dic(basedata[0], basedata[1])
        wait = (By.XPATH, targetsheet.get('加载等待'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 3
        while n < l:
            if menu[n] not in self.base.operable_list(basedata[0], basedata[1]):
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            else:
                findelement = self.findxpath(targetsheet.get(menu[n]))
                # 所有操作为"点击"或"勾选"的元素
                if menu[n] in ['导出',
                               '搜索'
                               ]:
                    findelement.click()
                    if menu[n] in ['搜索']:
                        self.wait_for_miss(120, wait)
                # 所有操作为"输入"的元素
                elif menu[n] in ['查询日期',
                                 '查询起始日期',
                                 '查询结束日期'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['投组单元',
                                 '所在账户'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        sleep(1)
                        findelement.send_keys(value[n] + Keys.SPACE + Keys.BACK_SPACE)
                        sleep(1)
                        if menu[n] in ['投组单元', '所在账户']:
                            self.findxpath_click(targetsheet.get('投组下拉选择'))
                # 所有操作为"点击后选择"的元素
                elif menu[n] in ['查询方式',
                                 '查询频率',
                                 '年份',
                                 '半年',
                                 '季度'
                                 ]:
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    else:
                        findelement.click()
                        if menu[n] in ['查询方式',
                                       '查询频率',
                                       '半年',
                                       '季度'
                                       ]:
                            self.findxpath_click(f'//li[text()="{value[n]}"]')
                        elif menu[n] in ['年份']:
                            self.findxpath_click(f'/html/body/div[last()]//a[text()="{value[n]}"]')
                            determine = self.findxpath(targetsheet.get('年份_确认'))
                            self.driver.execute_script("arguments[0].click();", determine)
                elif menu[n] == '月份':
                    findelement.click()
                    a = value[n].split('_')[0]
                    b = value[n].split('_')[1]
                    self.findxpath_click(f'/html/body/div[last()]//a[text()="{a}"]')
                    self.findxpath_click(f'//a[text()="{b}"and starts-with(@style,"margin")]')
                    determine = self.findxpath(targetsheet.get('月份_确定'))
                    self.driver.execute_script("arguments[0].click();", determine)
            n = n + 1
        return True

    # 升级对比自动化案例-浙商
    def income_compare(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet47]
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu(basedata[0]).get(menu[2]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu(basedata[0]).get(f'{menu[2]}-{menu[3]}'))
        targetsheet = self.base.sheet_xpath_dic(basedata[0], basedata[1])
        wait = (By.XPATH, targetsheet.get('加载等待'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 4
        while n < l:
            if menu[n] not in self.base.operable_list(basedata[0], basedata[1]):
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            else:
                findelement = self.findxpath(targetsheet.get(menu[n]))
                # 所有操作为"点击"或"勾选"的元素
                if menu[n] in ['导出',
                               '搜索'
                               ]:
                    findelement.click()
                    if menu[n] in ['搜索']:
                        self.wait_for_miss(120, wait)
                # 所有操作为"输入"的元素
                elif menu[n] in ['查询日期',
                                 '查询起始日期',
                                 '查询结束日期'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['投组单元',
                                 '所在账户'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        sleep(1)
                        findelement.send_keys(value[n] + Keys.SPACE + Keys.BACK_SPACE)
                        sleep(1)
                        if menu[n] in ['投组单元', '所在账户']:
                            self.findxpath_click(targetsheet.get('投组下拉选择'))
                # 所有操作为"点击后选择"的元素
                elif menu[n] in ['查询方式',
                                 '查询频率',
                                 '年份',
                                 '半年',
                                 '季度'
                                 ]:
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    else:
                        findelement.click()
                        if menu[n] in ['查询方式',
                                       '查询频率',
                                       '半年',
                                       '季度'
                                       ]:
                            self.findxpath_click(f'//li[text()="{value[n]}"]')
                        elif menu[n] in ['年份']:
                            self.findxpath_click(f'/html/body/div[last()]//a[text()="{value[n]}"]')
                            determine = self.findxpath(targetsheet.get('年份_确认'))
                            self.driver.execute_script("arguments[0].click();", determine)
                elif menu[n] == '月份':
                    findelement.click()
                    a = value[n].split('_')[0]
                    b = value[n].split('_')[1]
                    self.findxpath_click(f'/html/body/div[last()]//a[text()="{a}"]')
                    self.findxpath_click(f'//a[text()="{b}"and starts-with(@style,"margin")]')
                    determine = self.findxpath(targetsheet.get('月份_确定'))
                    self.driver.execute_script("arguments[0].click();", determine)
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
                o = self.findxpath(self.base.checkpoint_dic(basedata[0], basedata[1]).get(m[i])).get_attribute(
                    'textContent')
                x.setdefault(m[i], o)
                i = i + 1
        else:
            print('案例最终结果不存在查询数据，请合理调整步骤')
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
                findelement = self.findxpath(targetsheet.get(menu[n]))
                # 所有操作为"点击"或"勾选"的元素
                if menu[n] in ['导出',
                               '搜索'
                               ]:
                    findelement.click()
                    if menu[n] in ['搜索']:
                        self.wait_for_miss(120, wait)
                # 所有操作为"输入"的元素
                elif menu[n] in ['查询日期',
                                 '查询起始日期',
                                 '查询结束日期'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['投组单元',
                                 '所在账户'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        sleep(1)
                        findelement.send_keys(value[n] + Keys.SPACE + Keys.BACK_SPACE)
                        sleep(1)
                        if menu[n] in ['投组单元', '所在账户']:
                            self.findxpath_click(targetsheet.get('投组下拉选择'))
                # 所有操作为"点击后选择"的元素
                elif menu[n] in ['查询方式',
                                 '查询频率',
                                 '年份',
                                 '半年',
                                 '季度'
                                 ]:
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    else:
                        findelement.click()
                        if menu[n] in ['查询方式',
                                       '查询频率',
                                       '半年',
                                       '季度'
                                       ]:
                            self.findxpath_click(f'//li[text()="{value[n]}"]')
                        elif menu[n] in ['年份']:
                            self.findxpath_click(f'/html/body/div[last()]//a[text()="{value[n]}"]')
                            determine = self.findxpath(targetsheet.get('年份_确认'))
                            self.driver.execute_script("arguments[0].click();", determine)
                elif menu[n] == '月份':
                    findelement.click()
                    a = value[n].split('_')[0]
                    b = value[n].split('_')[1]
                    self.findxpath_click(f'/html/body/div[last()]//a[text()="{a}"]')
                    self.findxpath_click(f'//a[text()="{b}"and starts-with(@style,"margin")]')
                    determine = self.findxpath(targetsheet.get('月份_确定'))
                    self.driver.execute_script("arguments[0].click();", determine)
            n = n + 1
        # 新环境的记录值
        r = 0
        y = {}
        while r < p:
            s = self.findxpath(self.base.checkpoint_dic(basedata[0], basedata[1]).get(m[r])).get_attribute(
                'textContent')
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
