# 周期分录查询自动化测试用例
# 功能描述：查询周期分录
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet45, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class PeriodicEntry(BasePageXams):
    # 模拟操作自动化案例-浙商
    def periodic_entry_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet45]
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
                               '分录导出',
                               '搜索',
                               '高级查询',
                               '高级查询_查询',
                               '高级查询_重置',
                               '高级查询_返回'
                               ]:
                    if menu[n] == '分录导出':
                        self.findxpath_click('//span[text()="投组单元"]/../../../../../following-sibling::div/div/table/tbody/tr/td[2]/div')
                    findelement.click()
                    if menu[n] in ['搜索', '高级查询_返回']:
                        self.wait_for_miss(120, wait)
                # 所有操作为"输入"的元素
                elif menu[n] in ['开始日期',
                                 '结束日期',
                                 '高级查询_开始日期',
                                 '高级查询_结束日期'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['投组单元',
                                 '金融工具代码',
                                 '高级查询_投组单元',
                                 '高级查询_产品类型',
                                 '高级查询_金融工具代码'
                                 ]:
                    if menu[n] == '高级查询_产品类型':
                        a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                        a.append('置空')
                        if value[n] not in a:
                            print(f'值"{value[n]}"输入错误，请检查')
                            return False
                        elif value[n] == '置空':
                            findelement.click()
                            selectall = self.findxpath('//li[text()=" 保险公司债"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                            self.findxpath_click('//table[4]//label[text()="开始日期:"]')  # 收起列表
                        elif value[n] == '全选':
                            findelement.click()
                            self.findxpath_click('//li[text()=" 保险公司债"]/../../preceding-sibling::div')
                            self.findxpath_click('//table[4]//label[text()="开始日期:"]')  # 收起列表
                        else:
                            findelement.click()
                            self.findxpath_click(f'//li[text()=" {value[n]}"]')
                            self.findxpath_click('//table[4]//label[text()="开始日期:"]')  # 收起列表
                    else:
                        if value[n] == '置空':
                            findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        else:
                            findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                            sleep(1)
                            findelement.send_keys(value[n] + Keys.SPACE + Keys.BACK_SPACE)
                            sleep(1)
                            if menu[n] in ['投组单元', '高级查询_投组单元']:
                                self.findxpath_click(targetsheet.get('投组下拉选择'))
                            elif menu[n] in ['金融工具代码', '高级查询_金融工具代码']:
                                self.findxpath_click(f'/html/body/div[last()-2]//li[contains(text(),"{value[n]}")]')
                # 所有操作为"点击后选择"的元素
                elif menu[n] in ['投资类型',
                                 '会计分类',
                                 '高级查询_投资类型',
                                 '高级查询_会计分类',
                                 '高级查询_包含抹账分录'
                                 ]:
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    if menu[n] in ['投资类型', '高级查询_投资类型']:
                        a.append('置空')
                        if value[n] not in a:
                            print(f'值"{value[n]}"输入错误，请检查')
                            return False
                        elif value[n] == '置空':
                            findelement.click()
                            selectall = self.findxpath('//li[text()=" 应收款项类"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                            findelement.click()  # 收起列表
                        elif value[n] == '全选':
                            findelement.click()
                            self.findxpath_click('//li[text()=" 应收款项类"]/../../preceding-sibling::div')
                            findelement.click()  # 收起列表
                        else:
                            findelement.click()
                            self.findxpath_click(f'//li[text()=" {value[n]}"]')
                            findelement.click()  # 收起列表
                    else:
                        if value[n] not in a:
                            print(f'值"{value[n]}"输入错误，请检查')
                            return False
                        else:
                            findelement.click()
                            if menu[n] in ['会计分类', '高级查询_会计分类']:
                                self.findxpath_click(f'//div[last()]/div/ul/li[text()="{value[n]}"]')
                            elif menu[n] in ['高级查询_包含抹账分录']:
                                self.findxpath_click(f'//li[text()=" {value[n]}"]')
            n = n + 1
        return True

    # 升级对比自动化案例-浙商
    def periodic_entry_compare(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet45]
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
                               '分录导出',
                               '搜索',
                               '高级查询',
                               '高级查询_查询',
                               '高级查询_重置',
                               '高级查询_返回'
                               ]:
                    if menu[n] == '分录导出':
                        self.findxpath_click(
                            '//span[text()="投组单元"]/../../../../../following-sibling::div/div/table/tbody/tr/td[2]/div')
                    findelement.click()
                    if menu[n] in ['搜索', '高级查询_返回']:
                        self.wait_for_miss(120, wait)
                # 所有操作为"输入"的元素
                elif menu[n] in ['开始日期',
                                 '结束日期',
                                 '高级查询_开始日期',
                                 '高级查询_结束日期'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['投组单元',
                                 '金融工具代码',
                                 '高级查询_投组单元',
                                 '高级查询_产品类型',
                                 '高级查询_金融工具代码'
                                 ]:
                    if menu[n] == '高级查询_产品类型':
                        a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                        a.append('置空')
                        if value[n] not in a:
                            print(f'值"{value[n]}"输入错误，请检查')
                            return False
                        elif value[n] == '置空':
                            findelement.click()
                            selectall = self.findxpath('//li[text()=" 保险公司债"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                            self.findxpath_click('//table[4]//label[text()="开始日期:"]')  # 收起列表
                        elif value[n] == '全选':
                            findelement.click()
                            self.findxpath_click('//li[text()=" 保险公司债"]/../../preceding-sibling::div')
                            self.findxpath_click('//table[4]//label[text()="开始日期:"]')  # 收起列表
                        else:
                            findelement.click()
                            self.findxpath_click(f'//li[text()=" {value[n]}"]')
                            self.findxpath_click('//table[4]//label[text()="开始日期:"]')  # 收起列表
                    else:
                        if value[n] == '置空':
                            findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        else:
                            findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                            sleep(1)
                            findelement.send_keys(value[n] + Keys.SPACE + Keys.BACK_SPACE)
                            sleep(1)
                            if menu[n] in ['投组单元', '高级查询_投组单元']:
                                self.findxpath_click(targetsheet.get('投组下拉选择'))
                            elif menu[n] in ['金融工具代码', '高级查询_金融工具代码']:
                                self.findxpath_click(f'/html/body/div[last()-2]//li[contains(text(),"{value[n]}")]')
                # 所有操作为"点击后选择"的元素
                elif menu[n] in ['投资类型',
                                 '会计分类',
                                 '高级查询_投资类型',
                                 '高级查询_会计分类',
                                 '高级查询_包含抹账分录'
                                 ]:
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    if menu[n] in ['投资类型', '高级查询_投资类型']:
                        a.append('置空')
                        if value[n] not in a:
                            print(f'值"{value[n]}"输入错误，请检查')
                            return False
                        elif value[n] == '置空':
                            findelement.click()
                            selectall = self.findxpath('//li[text()=" 应收款项类"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                            findelement.click()  # 收起列表
                        elif value[n] == '全选':
                            findelement.click()
                            self.findxpath_click('//li[text()=" 应收款项类"]/../../preceding-sibling::div')
                            findelement.click()  # 收起列表
                        else:
                            findelement.click()
                            self.findxpath_click(f'//li[text()=" {value[n]}"]')
                            findelement.click()  # 收起列表
                    else:
                        if value[n] not in a:
                            print(f'值"{value[n]}"输入错误，请检查')
                            return False
                        else:
                            findelement.click()
                            if menu[n] in ['会计分类', '高级查询_会计分类']:
                                self.findxpath_click(f'//div[last()]/div/ul/li[text()="{value[n]}"]')
                            elif menu[n] in ['高级查询_包含抹账分录']:
                                self.findxpath_click(f'//li[text()=" {value[n]}"]')
            n = n + 1
        # 触发判断定位点
        point = self.findxpath(targetsheet.get('数据统计'))
        a = point.text.split(' ')[4]  # 搜索结果条数
        if a is not '1':
            print('当前搜索结果不唯一，请调整用例')
            return False
        else:
            # 点击唯一数据，展示分录详情
            self.findxpath_click('//span[text()="投组单元"]/../../../../../following-sibling::div/div/table/tbody/tr/td[2]/div')
            # 读取分录最大行数
            b = self.findxpath('//span[text()="记账步骤"]/../../../../../following-sibling::div//tr[last()]/td[1]/div')
            low = int(b.text)
            # 旧环境的界面展示记录值
            m = self.base.checkpoint_list2(basedata[0], basedata[1])
            p = len(m)
            i = 0
            x1 = {}
            while i < p:
                o = self.findxpath(self.base.checkpoint_dic2(basedata[0], basedata[1]).get(m[i])).text
                x1.setdefault(m[i], o)
                i = i + 1
            # 旧环境的分录明细记录值
            q1 = self.base.splicing_dic(basedata[0], basedata[1], low)
            r = []
            r.extend(q1)  # 将字典中的keys导入列表
            s = len(r)
            t = 0
            q2 = {}  # 生成拼接路径字典
            xpath1 = '//span[text()="记账步骤"]/../../../../../following-sibling::div/div/table/tbody/tr['
            xpath2 = ']/td['
            xpath3 = ']/div'
            while t < s:
                q2.setdefault(r[t], f'{xpath1}{q1.get(r[t])[0]}{xpath2}{q1.get(r[t])[1]}{xpath3}')
                t = t + 1
            #
            u = 0
            x2 = {}  # 分录明细字典
            while u < s:
                v = self.findxpath(q2.get(r[u])).text
                x2.setdefault(r[u], v)
                u = u + 1
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
                               '分录导出',
                               '搜索',
                               '高级查询',
                               '高级查询_查询',
                               '高级查询_重置',
                               '高级查询_返回'
                               ]:
                    if menu[n] == '分录导出':
                        self.findxpath_click(
                            '//span[text()="投组单元"]/../../../../../following-sibling::div/div/table/tbody/tr/td[2]/div')
                    findelement.click()
                    if menu[n] in ['搜索', '高级查询_返回']:
                        self.wait_for_miss(120, wait)
                # 所有操作为"输入"的元素
                elif menu[n] in ['开始日期',
                                 '结束日期',
                                 '高级查询_开始日期',
                                 '高级查询_结束日期'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['投组单元',
                                 '金融工具代码',
                                 '高级查询_投组单元',
                                 '高级查询_产品类型',
                                 '高级查询_金融工具代码'
                                 ]:
                    if menu[n] == '高级查询_产品类型':
                        a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                        a.append('置空')
                        if value[n] not in a:
                            print(f'值"{value[n]}"输入错误，请检查')
                            return False
                        elif value[n] == '置空':
                            findelement.click()
                            selectall = self.findxpath('//li[text()=" 保险公司债"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                            self.findxpath_click('//table[4]//label[text()="开始日期:"]')  # 收起列表
                        elif value[n] == '全选':
                            findelement.click()
                            self.findxpath_click('//li[text()=" 保险公司债"]/../../preceding-sibling::div')
                            self.findxpath_click('//table[4]//label[text()="开始日期:"]')  # 收起列表
                        else:
                            findelement.click()
                            self.findxpath_click(f'//li[text()=" {value[n]}"]')
                            self.findxpath_click('//table[4]//label[text()="开始日期:"]')  # 收起列表
                    else:
                        if value[n] == '置空':
                            findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        else:
                            findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                            sleep(1)
                            findelement.send_keys(value[n] + Keys.SPACE + Keys.BACK_SPACE)
                            sleep(1)
                            if menu[n] in ['投组单元', '高级查询_投组单元']:
                                self.findxpath_click(targetsheet.get('投组下拉选择'))
                            elif menu[n] in ['金融工具代码', '高级查询_金融工具代码']:
                                self.findxpath_click(f'/html/body/div[last()-2]//li[contains(text(),"{value[n]}")]')
                # 所有操作为"点击后选择"的元素
                elif menu[n] in ['投资类型',
                                 '会计分类',
                                 '高级查询_投资类型',
                                 '高级查询_会计分类',
                                 '高级查询_包含抹账分录'
                                 ]:
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    if menu[n] in ['投资类型', '高级查询_投资类型']:
                        a.append('置空')
                        if value[n] not in a:
                            print(f'值"{value[n]}"输入错误，请检查')
                            return False
                        elif value[n] == '置空':
                            findelement.click()
                            selectall = self.findxpath('//li[text()=" 应收款项类"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                            findelement.click()  # 收起列表
                        elif value[n] == '全选':
                            findelement.click()
                            self.findxpath_click('//li[text()=" 应收款项类"]/../../preceding-sibling::div')
                            findelement.click()  # 收起列表
                        else:
                            findelement.click()
                            self.findxpath_click(f'//li[text()=" {value[n]}"]')
                            findelement.click()  # 收起列表
                    else:
                        if value[n] not in a:
                            print(f'值"{value[n]}"输入错误，请检查')
                            return False
                        else:
                            findelement.click()
                            if menu[n] in ['会计分类', '高级查询_会计分类']:
                                self.findxpath_click(f'//div[last()]/div/ul/li[text()="{value[n]}"]')
                            elif menu[n] in ['高级查询_包含抹账分录']:
                                self.findxpath_click(f'//li[text()=" {value[n]}"]')
            n = n + 1
        # 点击唯一数据，展示分录详情
        self.findxpath_click('//span[text()="投组单元"]/../../../../../following-sibling::div/div/table/tbody/tr/td[2]/div')
        # 新环境的界面展示记录值
        i = 0
        y1 = {}
        while i < p:
            o = self.findxpath(self.base.checkpoint_dic2(basedata[0], basedata[1]).get(m[i])).text
            y1.setdefault(m[i], o)
            i = i + 1
        # 新环境的分录明细记录值
        u = 0
        y2 = {}  # 分录明细字典
        while u < s:
            v = self.findxpath(q2.get(r[u])).text
            y2.setdefault(r[u], v)
            u = u + 1
        # 界面展示局部校验
        z = 0
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
        # 分录明细局部校验
        z = 0
        if x2.get(r[z]) == y2.get(r[z]):
            # 分录明细全局校验
            t = 0
            while t < s:
                if x2.get(r[t]) == y2.get(r[t]):
                    t = t + 1
                else:
                    print(f'对比结果：{r[t]}：{x2.get(r[t])}数据核对不一致，请检查并联系开发')
                    return False
        else:
            print(f'对比结果：{r[z]}：{x2.get(r[z])}数据核对不一致，请检查并联系开发')
            return False
        print('对比结果：分录明细数据核对一致')
        return True
