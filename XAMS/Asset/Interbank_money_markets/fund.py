# 货币基金自动化测试用例
# 功能描述：货币基金条款维护
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet43, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class Fund(BasePageXams):
    # 模拟操作自动化案例-浙商
    def fund_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet43]
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
                               '新增',
                               '修改',
                               '删除',
                               '复核',
                               '附件上传',
                               '监管信息维护',
                               '查看变更日志',
                               '搜索',
                               '搜索_全选框',
                               '确认_是',
                               '确认_否',
                               '基本信息_匹配基金',
                               '资产条款信息_保存',
                               '资产条款信息_重置',
                               '资产条款信息_返回',
                               '匹配基本信息_搜索',
                               '基金列表_勾选框',
                               '基金列表_匹配',
                               '基金列表_返回'
                               ]:
                    if menu[n] in ['确认_是', '基金列表_匹配', '资产条款信息_保存']:
                        self.driver.execute_script("arguments[0].click();", findelement)
                        self.wait_for_miss(120, wait)
                        determine = self.findxpath(targetsheet.get('成功_确定'))
                        self.driver.execute_script("arguments[0].click();", determine)
                    else:
                        findelement.click()
                    if menu[n] in ['搜索']:
                        self.wait_for_miss(120, wait)
                # 所有操作为"输入"的元素
                elif menu[n] in ['资产名称(代码)',
                                 '基本信息_基金名称',
                                 '基本信息_特殊授信编号',
                                 '基本信息_备注',
                                 '资产条款信息_成立日',
                                 '匹配基本信息_金融工具代码'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['基本信息_基金管理人',
                                 '基本信息_额度主体'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        sleep(1)
                        findelement.send_keys(value[n] + Keys.SPACE + Keys.BACK_SPACE)
                        sleep(1)
                        self.findxpath_click(f'/html/body/div[last()-2]//li[contains(text(),"{value[n]}")]')
                # 所有操作为"点击后选择"的元素
                elif menu[n] in ['资产状态',
                                 '基本信息_币种',
                                 '基本信息_应税属性',
                                 '资产条款信息_收益计算方式',
                                 '资产条款信息_是否分行推荐',
                                 '资产条款信息_所属分行机构'
                                 ]:
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    else:
                        findelement.click()
                        self.findxpath_click(f'//li[text()="{value[n]}"]')
            n = n + 1
        return True
