# 表七同业交易对手情况表自动化测试用例
# 功能描述：统计同业交易对手情况
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet39, Excel_basedata_nj
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class InterbankCounterparty(BasePageXams):
    # 模拟操作自动化案例-南京
    def interbank_counterparty_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_nj, sheet39]
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu(basedata[0]).get(menu[1]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu(basedata[0]).get(f'{menu[1]}-{menu[2]}'))
        targetsheet = self.base.sheet_xpath_dic(basedata[0], basedata[1])
        wait = (By.XPATH, targetsheet.get('加载等待'))
        # 点击需要核对的页签，保证核对正常
        self.findxpath_click(targetsheet.get('同业交易对手情况表'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 3
        while n < l:
            if menu[n] not in self.base.operable_list(basedata[0], basedata[1]):
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            else:
                findelement = self.findxpath(targetsheet.get(menu[n]))
                if menu[n] == '投组单元':
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                        sleep(1)
                        self.findxpath_click(targetsheet.get('投组下拉选择'))
                elif menu[n] == '年':
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                elif menu[n] == '季度':
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    a.append('置空')
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    elif value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                elif menu[n] == '查询':
                    findelement.click()
                    # sleep(1)  # 强制等待用来过渡到显式等待
                    self.wait_for_miss(120, wait)
                elif menu[n] == '导出':
                    findelement.click()
                    sleep(2)
            n = n + 1
        return True

    # 升级对比自动化案例-南京
    def interbank_counterparty_compare(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_nj, sheet39]
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu(basedata[0]).get(menu[2]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu(basedata[0]).get(f'{menu[2]}-{menu[3]}'))
        targetsheet = self.base.sheet_xpath_dic(basedata[0], basedata[1])
        wait = (By.XPATH, targetsheet.get('加载等待'))
        # 点击需要核对的页签，保证核对正常
        self.findxpath_click(targetsheet.get('同业交易对手情况表'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 4
        while n < l:
            if menu[n] not in self.base.operable_list(basedata[0], basedata[1]):
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            else:
                findelement = self.findxpath(targetsheet.get(menu[n]))
                if menu[n] == '投组单元':
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                        sleep(1)
                        self.findxpath_click(targetsheet.get('投组下拉选择'))
                elif menu[n] == '年':
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                elif menu[n] == '季度':
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    a.append('置空')
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    elif value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                elif menu[n] == '查询':
                    findelement.click()
                    # sleep(1)  # 强制等待用来过渡到显式等待
                    self.wait_for_miss(120, wait)
                elif menu[n] == '导出':
                    findelement.click()
                    sleep(2)
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
        # 点击需要核对的页签，保证核对正常
        self.findxpath_click(targetsheet.get('同业交易对手情况表'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 4
        while n < l:
            if menu[n] not in self.base.operable_list(basedata[0], basedata[1]):
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            else:
                findelement = self.findxpath(targetsheet.get(menu[n]))
                if menu[n] == '投组单元':
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                        sleep(1)
                        self.findxpath_click(targetsheet.get('投组下拉选择'))
                elif menu[n] == '年':
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                elif menu[n] == '季度':
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    a.append('置空')
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    elif value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                elif menu[n] == '查询':
                    findelement.click()
                    # sleep(1)  # 强制等待用来过渡到显式等待
                    self.wait_for_miss(120, wait)
                elif menu[n] == '导出':
                    findelement.click()
                    sleep(2)
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
