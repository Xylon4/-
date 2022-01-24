# 损益结转分录查询自动化测试用例
# 功能描述：查询损益结转分录
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet46, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams
import math


class ProfitCarryOverEntry(BasePageXams):
    # 模拟操作自动化案例-浙商
    def profit_carry_over_entry_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet46]
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
                               'Excel(当前页)',
                               'Excel(所有数据)',
                               '搜索'
                               ]:
                    findelement.click()
                    if menu[n] in ['搜索']:
                        self.wait_for_miss(120, wait)
                # 所有操作为"输入"的元素
                elif menu[n] in ['日期', '翻页']:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                    if menu[n] == '翻页':
                        findelement.send_keys(Keys.ENTER)
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['投组单元',
                                 '金融工具代码'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        sleep(1)
                        findelement.send_keys(value[n] + Keys.SPACE + Keys.BACK_SPACE)
                        sleep(1)
                        if menu[n] in ['投组单元']:
                            self.findxpath_click(targetsheet.get('投组下拉选择'))
                        elif menu[n] in ['金融工具代码']:
                            self.findxpath_click(f'//li[contains(text(),"{value[n]}")]')
            n = n + 1
        return True

    # 升级对比自动化案例-浙商
    def profit_carry_over_entry_compare(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet46]
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
                               'Excel(当前页)',
                               'Excel(所有数据)',
                               '搜索'
                               ]:
                    findelement.click()
                    if menu[n] in ['搜索']:
                        self.wait_for_miss(120, wait)
                # 所有操作为"输入"的元素
                elif menu[n] in ['日期', '翻页']:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                    if menu[n] == '翻页':
                        findelement.send_keys(Keys.ENTER)
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['投组单元',
                                 '金融工具代码'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        sleep(1)
                        findelement.send_keys(value[n] + Keys.SPACE + Keys.BACK_SPACE)
                        sleep(1)
                        if menu[n] in ['投组单元']:
                            self.findxpath_click(targetsheet.get('投组下拉选择'))
                        elif menu[n] in ['金融工具代码']:
                            self.findxpath_click(f'//li[contains(text(),"{value[n]}")]')
            n = n + 1
        # 触发判断定位点
        point = self.findxpath(targetsheet.get('搜索结果'))
        if point.is_selected():
            print('无搜索结果，请调整用例')
            return False
        else:
            # 统计搜索条数
            a = self.findxpath(targetsheet.get('数据统计'))
            sum = a.text.split(' ')[4]
            sum = int(sum)
            # 计算页数
            h = 20  # 单页行数为20
            b = sum / h
            page = math.ceil(b)
            # 计算最后一页的行数
            low = sum - (page - 1) * h
            # 旧环境的分录记录值
            d = 0
            q2 = {}  # 拼接路径字典
            x1 = {}  # 分录字典
            while d < page:
                if d + 1 == page:
                    q1 = self.base.splicing_dic(basedata[0], basedata[1], low, d + 1, h)
                    r = []
                    r.extend(q1)  # 将字典中的keys导入列表
                    s = len(r)
                    t = 0
                    xpath1 = '//span[text()="凭证号"]/../../../../../following-sibling::div/div/table/tbody/tr['
                    xpath2 = ']/td['
                    xpath3 = ']/div'
                    while t < s:
                        q2.setdefault(r[t], f'{xpath1}{q1.get(r[t])[0]}{xpath2}{q1.get(r[t])[1]}{xpath3}')
                        t = t + 1
                    # 通过路径字典生成值字典
                    u = 0
                    while u < s:
                        v = self.findxpath(q2.get(r[u])).text
                        x1.setdefault(r[u], v)
                        u = u + 1
                else:
                    q1 = self.base.splicing_dic(basedata[0], basedata[1], h, d + 1, h)
                    r = []
                    r.extend(q1)  # 将字典中的keys导入列表
                    s = len(r)
                    t = 0
                    xpath1 = '//span[text()="凭证号"]/../../../../../following-sibling::div/div/table/tbody/tr['
                    xpath2 = ']/td['
                    xpath3 = ']/div'
                    while t < s:
                        q2.setdefault(r[t], f'{xpath1}{q1.get(r[t])[0]}{xpath2}{q1.get(r[t])[1]}{xpath3}')
                        t = t + 1
                    # 通过路径字典生成值字典
                    u = 0
                    while u < s:
                        v = self.findxpath(q2.get(r[u])).text
                        x1.setdefault(r[u], v)
                        u = u + 1
                d = d + 1
                turn = self.findxpath(targetsheet.get('翻页'))
                turn.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                turn.send_keys(d + 1)
                turn.send_keys(Keys.ENTER)
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
                               'Excel(当前页)',
                               'Excel(所有数据)',
                               '搜索'
                               ]:
                    findelement.click()
                    if menu[n] in ['搜索']:
                        self.wait_for_miss(120, wait)
                # 所有操作为"输入"的元素
                elif menu[n] in ['日期', '翻页']:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                    if menu[n] == '翻页':
                        findelement.send_keys(Keys.ENTER)
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['投组单元',
                                 '金融工具代码'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        sleep(1)
                        findelement.send_keys(value[n] + Keys.SPACE + Keys.BACK_SPACE)
                        sleep(1)
                        if menu[n] in ['投组单元']:
                            self.findxpath_click(targetsheet.get('投组下拉选择'))
                        elif menu[n] in ['金融工具代码']:
                            self.findxpath_click(f'//li[contains(text(),"{value[n]}")]')
            n = n + 1
        # 新环境的分录记录值
        d = 0
        q2 = {}  # 拼接路径字典
        y1 = {}  # 分录字典
        while d < page:
            if d + 1 == page:
                q1 = self.base.splicing_dic(basedata[0], basedata[1], low, d + 1, h)
                r = []
                r.extend(q1)  # 将字典中的keys导入列表
                s = len(r)
                t = 0
                xpath1 = '//span[text()="凭证号"]/../../../../../following-sibling::div/div/table/tbody/tr['
                xpath2 = ']/td['
                xpath3 = ']/div'
                while t < s:
                    q2.setdefault(r[t], f'{xpath1}{q1.get(r[t])[0]}{xpath2}{q1.get(r[t])[1]}{xpath3}')
                    t = t + 1
                # 通过路径字典生成值字典
                u = 0
                while u < s:
                    v = self.findxpath(q2.get(r[u])).text
                    y1.setdefault(r[u], v)
                    u = u + 1
            else:
                q1 = self.base.splicing_dic(basedata[0], basedata[1], h, d + 1, h)
                r = []
                r.extend(q1)  # 将字典中的keys导入列表
                s = len(r)
                t = 0
                xpath1 = '//span[text()="凭证号"]/../../../../../following-sibling::div/div/table/tbody/tr['
                xpath2 = ']/td['
                xpath3 = ']/div'
                while t < s:
                    q2.setdefault(r[t], f'{xpath1}{q1.get(r[t])[0]}{xpath2}{q1.get(r[t])[1]}{xpath3}')
                    t = t + 1
                # 通过路径字典生成值字典
                u = 0
                while u < s:
                    v = self.findxpath(q2.get(r[u])).text
                    y1.setdefault(r[u], v)
                    u = u + 1
            d = d + 1
            turn = self.findxpath(targetsheet.get('翻页'))
            turn.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
            turn.send_keys(d + 1)
            turn.send_keys(Keys.ENTER)
        # 界面展示局部校验
        z = 0
        m = []
        m.extend(x1)
        p = len(m)
        if x1.get(m[z]) == y1.get(m[z]):
            # 界面展示全局校验
            t = 0
            while t < p:
                if x1.get(m[t]) == y1.get(m[t]):
                    t = t + 1
                else:
                    print(f'对比结果：{m[t]}：{x1.get(m[t])}数据核对不一致，请检查并联系开发')
                    return False
        else:
            print(f'对比结果：{m[z]}：{x1.get(m[z])}数据核对不一致，请检查并联系开发')
            return False
        print('对比结果：界面展示数据核对一致')
        return True
