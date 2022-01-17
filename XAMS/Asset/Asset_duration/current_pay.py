# 活期账户提前收息自动化测试用例
# 功能描述：活期账户提前收息处理
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet40, Excel_basedata_tj
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class CurrentPay(BasePageXams):
    # 模拟操作自动化案例-天津
    def current_pay_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_tj, sheet40]
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
                if menu[n] in ['新增',
                               '删除',
                               '复核',
                               '撤销',
                               '搜索',
                               '搜索_勾选框',
                               '活期账户余额_搜索',
                               '活期账户余额_关闭',
                               '交易信息_保留未收利息',
                               '交易信息_返回',
                               '限额占用结果_返回'
                               ]:
                    findelement.click()
                elif menu[n] in ['投组单元', '活期账户余额_投组单元']:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                        sleep(1)
                        self.findxpath_click(targetsheet.get('投组下拉选择'))
                elif menu[n] in ['活期账户', '活期账户余额_活期账户']:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                        sleep(1)
                        findelement.send_keys(Keys.SPACE)
                        findelement.send_keys(Keys.BACK_SPACE)
                        findelement.send_keys(Keys.ARROW_DOWN)
                        findelement.send_keys(Keys.ENTER)
                # 所有操作为"输入"的元素
                elif menu[n] in ['交易日期', '交易信息_实收利息(元)', '交易信息_应收利息(元)']:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                elif menu[n] == '结算状态':
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    a.append('置空')
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    elif value[n] == '置空':
                        findelement.click()
                        selectall = self.findxpath('//div[contains(text(),"全部")]')
                        action = ActionChains(self.driver)
                        action.double_click(selectall).perform()
                        findelement.click()
                    elif value[n] == '全部':
                        findelement.click()
                        self.findxpath_click(f'//div[contains(text(),"{value[n]}")]')
                        findelement.click()
                    else:
                        findelement.click()
                        self.findxpath_click(f'//li[contains(text(),"{value[n]}")]')
                        findelement.click()
                elif menu[n] == '搜索':
                    findelement.click()
                    # sleep(1)  # 强制等待用来过渡到显式等待
                    self.wait_for_miss(120, wait)
                elif menu[n] in ['确认_是', '交易信息_保存']:
                    self.driver.execute_script("arguments[0].click();", findelement)
                    self.wait_for_miss(120, wait)
                    self.findxpath_click(targetsheet.get('成功_确定'))
                    # determine = self.findxpath(targetsheet.get('成功_确定'))
                    # self.driver.execute_script("arguments[0].click();", determine)
                elif menu[n] == '确认_否':
                    self.driver.execute_script("arguments[0].click();", findelement)
                elif menu[n] == '活期账户余额_提前收息':
                    # 勾选查询结果
                    self.findxpath_click(targetsheet.get('提前收息勾选'))
                    findelement.click()
            n = n + 1
        return True
