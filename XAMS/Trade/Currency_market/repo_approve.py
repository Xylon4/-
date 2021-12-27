# 质押式回购审批自动化测试用例
# 功能描述：质押式回购审批
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet35, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class RepoApprove(BasePageXams):
    # 模拟操作自动化案例
    def repo_approve_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet35]
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
                               '打印',
                               '交易指令查看',
                               '高级查询',
                               '高级查询_查询',
                               '高级查询_重置',
                               '高级查询_返回',
                               '搜索_勾选框',
                               '确认_否',
                               '清算速度_T + 0',
                               '清算速度_T + 1',
                               '质押券_新增',
                               '质押券_修改',
                               '质押券_删除',
                               '质押券_勾选框',
                               '选择质押券_搜索',
                               '选择质押券_返回',
                               '新建',
                               '重置',
                               '返回',
                               '选择工作流_取消',
                               '限额占用结果_返回'
                               ]:
                    findelement.click()
                # 所有操作为"下拉选择"的元素
                elif menu[n] in ['业务种类&币种_业务种类',
                                 '交易基本信息_交易市场',
                                 '交易基本信息_执行市场',
                                 '交易要素_计息基准',
                                 '交易要素_清算方式'
                                 ]:
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    else:
                        findelement.click()
                        self.findxpath_click(f'//li[text()="{value[n]}"]')
                # 所有操作为"输入"的元素
                elif menu[n] in ['交易员',
                                 '交易日期起',
                                 '交易日期止',
                                 '高级查询_交易单号',
                                 '高级查询_交易日期起',
                                 '高级查询_交易日期止',
                                 '高级查询_审批单号',
                                 '高级查询_外部成交编号',
                                 '交易基本信息_交易日期',
                                 '交易基本信息_成交编号',
                                 '交易要素_回购期限(天)',
                                 '交易要素_资产名称',
                                 '交易要素_回购利率(%)',
                                 '选择质押券_质押券券面总额(万元)',
                                 '选择质押券_折算比例(%)',
                                 '首期结算要素_交易金额(元)',
                                 '到期结算要素_结算日期',
                                 '到期结算要素_结算金额(元)',
                                 '银行间交易费用信息_交易费(元)',
                                 '银行间交易费用信息_结算费(元)',
                                 '银行间交易费用信息_清算费(元)',
                                 '交易备注信息_备注'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                elif menu[n] == '交易对手信息_银行账户':
                    findelement.click()
                    self.findxpath_click(f'//li[text()="{value[n]}"]')
                elif menu[n] in ['投组', '投组单元_投组单元', '选择质押券_投组单元']:
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
                elif menu[n] == '选择工作流_勾选':
                    self.findxpath_click(f'/html/body/div[last()-2]//td[3]/div[contains(text(),"{value[n]}")]')
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['高级查询_交易对手',
                                 '本方账户信息_资金账户',
                                 '交易对手信息_外部交易',
                                 '选择质押券_外部券账户',
                                 '选择质押券_代码'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a')
                        findelement.send_keys(Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                        findelement.send_keys(Keys.SPACE)
                        findelement.send_keys(Keys.BACK_SPACE)
                        sleep(1)
                        findelement.send_keys(Keys.ARROW_DOWN)
                        findelement.send_keys(Keys.ENTER)
                elif menu[n] in ['审批状态', '高级查询_审批状态', '高级查询_业务种类', '高级查询_交易状态', '选择质押券_产品分类']:
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
                elif menu[n] in ['保存', '保存并提交']:
                    findelement.click()
                    remind = self.findxpath(targetsheet.get('提醒_继续'))
                    self.driver.execute_script("arguments[0].click();", remind)
                    # self.findxpath_click(targetsheet.get('成功_确定'))
                    determine = self.findxpath(targetsheet.get('成功_确定'))
                    self.driver.execute_script("arguments[0].click();", determine)
                    sleep(2)  # 使用时存在因为机器性能较低而延长
                    if menu[n] == '保存并提交':
                        # self.findxpath_click(targetsheet.get('成功_确定'))
                        self.driver.execute_script("arguments[0].click();", determine)
                elif menu[n] in ['确认_是', '提交']:
                    self.driver.execute_script("arguments[0].click();", findelement)
                    self.wait_for_miss(120, wait)
                    # self.findxpath_click(targetsheet.get('成功_确定'))
                    determine = self.findxpath(targetsheet.get('成功_确定'))
                    self.driver.execute_script("arguments[0].click();", determine)
                elif menu[n] in ['选择质押券_确定', '选择工作流_确定']:
                    findelement.click()
                    self.findxpath_click(targetsheet.get('成功_确定'))
                    sleep(1)
                elif menu[n] in ['强制通过_是', '强制通过_否']:
                    self.driver.execute_script("arguments[0].click();", findelement)
                elif menu[n] == '模板新建':
                    self.findxpath_click(targetsheet.get('新建_倒三角'))
                    findelement.click()
                elif menu[n] == '搜索':
                    findelement.click()
                    self.wait_for_miss(120, wait)
                elif menu[n] == '高级查询_交易品种':
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    else:
                        findelement.send_keys(value[n])
                        findelement.send_keys(Keys.SPACE)
                        self.findxpath_click(f'//li[text()="{value[n]}"]')
            n = n + 1
        return True
