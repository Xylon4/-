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
                               '保存布局',
                               '新增',
                               '修改',
                               '撤销审批',
                               '成交确认',
                               '撤销成交确认',
                               '注销审批单',
                               '撤销注销',
                               '删除',
                               '提交',
                               '打印',
                               '交易指令查看',
                               '高级查询',
                               '高级查询_查询',
                               '高级查询_重置',
                               '高级查询_返回'
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
                elif menu[n] in ['交易员',
                                 '交易日期起',
                                 '交易日期止',
                                 '高级查询_交易单号',
                                 '高级查询_交易日期起',
                                 '高级查询_交易日期止',
                                 '高级查询_审批单号',
                                 '高级查询_外部成交编号'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                elif menu[n] in ['投组']:
                    findelement.click()
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                        sleep(1)
                        self.findxpath_click(targetsheet.get('投组下拉选择'))
                elif menu[n] == '高级查询_投组单元':
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                        sleep(1)
                        self.findxpath_click(
                            f'//label[text()="投组单元:"]/../../../../../../../../../../../following-sibling::div/div[last()]//tr[last()]/td/div/span[contains(text(),"{value[n]}")]')
                elif menu[n] == '高级查询_资产类别':
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                        sleep(1)
                        self.findxpath_click(f'//span[text()="{value[n]}"]')
                elif menu[n] in ['高级查询_交易对手', '高级查询_债券代码']:
                    findelement.send_keys(value[n])
                    findelement.send_keys(Keys.SPACE)
                    findelement.send_keys(Keys.BACK_SPACE)
                    sleep(1)
                    findelement.send_keys(Keys.ARROW_DOWN)
                    findelement.send_keys(Keys.ENTER)
                    findelement.click()  # 尝试解决回车后无法正常过渡到下个元素定位的问题
                elif menu[n] in ['审批状态', '高级查询_审批状态', '高级查询_业务种类', '高级查询_交易状态']:
                    a = self.base.enumeration_list(basedata[0], basedata[1], menu[n])
                    a.append('置空')
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    elif value[n] == '置空':
                        findelement.click()
                        selectall = self.findxpath(targetsheet.get(f'{menu[n]}_全选'))
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
