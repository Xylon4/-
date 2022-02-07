# 日间跑批自动化测试用例
# 功能描述：执行日间跑批
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet53, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams
import math


class DaytimeBatch(BasePageXams):
    # 模拟操作自动化案例-浙商
    def daytime_batch_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet53]
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
                if menu[n] in ['轧账',
                               '日间跑批',
                               '全部勾选',
                               '清空所选项',
                               '包含SPV投组',
                               '搜索',
                               '搜索_全选框',
                               '搜索_单选框',
                               '轧账检查_正常轧账',
                               '轧账检查_撤销轧账',
                               '轧账检查_刷新',
                               '轧账检查_返回',
                               '日间跑批页面_开始跑批',
                               '日间跑批页面_撤销跑批',
                               '日间跑批页面_刷新',
                               '日间跑批页面_关闭'
                               ]:
                    findelement.click()
                    if menu[n] in ['搜索', '轧账检查_返回', '轧账']:
                        self.wait_for_miss(120, wait)
                    if menu[n] in ['轧账检查_正常轧账', '轧账检查_撤销轧账']:
                        rolling_wait = (By.XPATH, targetsheet.get('轧账等待'))
                        self.wait_for_miss(120, rolling_wait)
                    if menu[n] in ['日间跑批页面_开始跑批']:
                        status = (By.XPATH, targetsheet.get('跑批完成'))
                        self.wait_for_visit(300, status)
                    if menu[n] in ['日间跑批页面_撤销跑批']:
                        status = (By.XPATH, targetsheet.get('跑批撤销'))
                        self.wait_for_visit(300, status)
                    if menu[n] in ['日间跑批页面_开始跑批', '日间跑批页面_撤销跑批', '轧账检查_正常轧账', '轧账检查_撤销轧账']:
                        determine = self.findxpath(targetsheet.get('成功_确定'))
                        self.driver.execute_script("arguments[0].click();", determine)
                # 所有操作为"输入"的元素
                elif menu[n] in ['业务日期']:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['投组单元']:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        sleep(1)
                        findelement.send_keys(value[n] + Keys.SPACE + Keys.BACK_SPACE)
                        sleep(1)
                        if menu[n] in ['投组单元']:
                            self.findxpath_click(targetsheet.get('投组下拉选择'))
                # 所有操作为"点击后选择"的元素
                elif menu[n] in ['清算路径',
                                 '轧账状态',
                                 '跑批状态',
                                 ]:
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    a.append('置空')
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    elif value[n] == '置空':
                        findelement.click()
                        if menu[n] == '轧账状态':
                            selectall = self.findxpath('//li[text()=" 未轧账"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                        elif menu[n] == '跑批状态':
                            selectall = self.findxpath('//li[text()=" 未跑批"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                        findelement.click()
                    elif value[n] == '全选':
                        findelement.click()
                        if menu[n] == '轧账状态':
                            self.findxpath_click('//li[text()=" 未轧账"]/../../preceding-sibling::div')
                        elif menu[n] == '跑批状态':
                            self.findxpath_click('//li[text()=" 未跑批"]/../../preceding-sibling::div')
                        findelement.click()
                    else:
                        findelement.click()
                        if menu[n] in ['清算路径',
                                       '轧账状态',
                                       '跑批状态'
                                       ]:
                            self.findxpath_click(f'//li[text()=" {value[n]}"]')
                        findelement.click()
                elif menu[n] in ['日间跑批页面_撤销至']:
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    else:
                        findelement.click()
                        self.findxpath_click(f'//li[text()="{value[n]}"]')
            n = n + 1
        return True
