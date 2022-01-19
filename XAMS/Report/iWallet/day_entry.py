# 日间分录查询自动化测试用例
# 功能描述：查询日间分录
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet44, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class DayEntry(BasePageXams):
    # 模拟操作自动化案例-浙商
    def day_entry_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet44]
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
                        self.findxpath_click('//span[text()="指令号"]/../../../../../following-sibling::div//td[1]/div')
                    findelement.click()
                    if menu[n] in ['搜索', '高级查询_返回']:
                        self.wait_for_miss(120, wait)
                # 所有操作为"输入"的元素
                elif menu[n] in ['开始日期',
                                 '结束日期',
                                 '指令号',
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
                                 '客户名称',
                                 '高级查询_投组单元',
                                 '高级查询_产品类型',
                                 '高级查询_金融工具代码',
                                 '高级查询_客户名称'
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
                            elif menu[n] in ['金融工具代码', '高级查询_金融工具代码', '客户名称', '高级查询_客户名称']:
                                self.findxpath_click(f'/html/body/div[last()-2]//li[contains(text(),"{value[n]}")]')
                # 所有操作为"点击后选择"的元素
                elif menu[n] in ['会计分类',
                                 '高级查询_投资类型',
                                 '高级查询_会计分类',
                                 '高级查询_包含抹账分录'
                                 ]:
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    if menu[n] == '高级查询_投资类型':
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
    def day_entry_compare(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet44]
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
                        self.findxpath_click('//span[text()="指令号"]/../../../../../following-sibling::div//td[1]/div')
                    findelement.click()
                    if menu[n] in ['搜索', '高级查询_返回']:
                        self.wait_for_miss(120, wait)
                # 所有操作为"输入"的元素
                elif menu[n] in ['开始日期',
                                 '结束日期',
                                 '指令号',
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
                                 '客户名称',
                                 '高级查询_投组单元',
                                 '高级查询_产品类型',
                                 '高级查询_金融工具代码',
                                 '高级查询_客户名称'
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
                            elif menu[n] in ['金融工具代码', '高级查询_金融工具代码', '客户名称', '高级查询_客户名称']:
                                self.findxpath_click(f'/html/body/div[last()-2]//li[contains(text(),"{value[n]}")]')
                # 所有操作为"点击后选择"的元素
                elif menu[n] in ['会计分类',
                                 '高级查询_投资类型',
                                 '高级查询_会计分类',
                                 '高级查询_包含抹账分录'
                                 ]:
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    if menu[n] == '高级查询_投资类型':
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
        m = self.base.checkpoint_list(basedata[0], basedata[1])
        point = self.findxpath(self.base.checkpoint_dic(basedata[0], basedata[1]).get(m[0]))
        a = point.text.split(' ')[4]  # 搜索结果条数
        if a is not 1:
            print('当前搜索结果不唯一，请调整用例')
            return False
        else:
            return True
