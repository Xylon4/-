# 现券审批自动化测试用例
# 功能描述：现券审批
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet32, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class BondApprove(BasePageXams):
    # 模拟操作自动化案例
    def bond_approve_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet32]
        basepagewait = (By.XPATH, self.base.sheet_xpath_dic(basedata[0], basedata[1]).get('首页加载等待'))
        self.wait_for_visit(120, basepagewait)
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
                # 所有操作为"点击"或"勾选"的元素
                if menu[n] in ['导出',
                               'Excel(当前页)',
                               'Excel(所有数据)',
                               '新增',
                               '复制',
                               '修改',
                               '撤销审批',
                               '成交确认',
                               '撤销成交确认',
                               '注销审批单',
                               '撤销注销',
                               '删除',
                               '详情',
                               '审批详情',
                               '交易指令查看'
                               ]:
                    findelement.click()
                # 所有操作为"下拉选择"的元素
                # elif menu[n] in ['审批状态'
                #                  ]:
                #     elementlist = targetsheet.keys()
                #     if value[n] not in elementlist:
                #         print(f'值"{value[n]}"输入错误，请检查')
                #         return False
                #     else:
                #         findelement.click()
                #         self.findxpath_click(targetsheet.get(value[n]))
                # 所有操作为"输入"的元素
                elif menu[n] in ['交易日期始',
                                 '交易日期止'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                elif menu[n] == '投组':
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                        sleep(1)
                        self.findxpath_click(targetsheet.get('投组下拉选择'))
                elif menu[n] == '交易员':
                    findelement.click()
                    self.findxpath_click(f'//li[text()=" {value[n]}"]')
                    findelement.click()
                elif menu[n] == '审批状态':
                    a = self.base.enumeration_list(basedata[0], basedata[1], menu[n])
                    a.append('置空')
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    elif value[n] == '置空':
                        findelement.click()
                        selectall = self.findxpath(targetsheet.get('审批状态_全选'))
                        action = ActionChains(self.driver)
                        action.double_click(selectall).perform()
                        findelement.click()  # 收起下拉框
                    else:
                        findelement.click()
                        self.findxpath_click(targetsheet.get(value[n]))
                        findelement.click()  # 收起下拉框
                elif menu[n] == '搜索':
                    findelement.click()
                    self.wait_for_miss(120, wait)
            n = n + 1
        return True
