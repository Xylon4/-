# 待审批任务自动化测试用例
# 功能描述：待审批任务处理
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet41, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class TodoTasks(BasePageXams):
    # 模拟操作自动化案例-浙商
    def todo_tasks_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet41]
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
                if menu[n] in ['刷新',
                               '审批通过',
                               '审批拒绝',
                               '审批回退',
                               '搜索',
                               '搜索折叠',
                               '搜索_单选勾选框',
                               '搜索_全选勾选框',
                               '处理',
                               '流程处理_业务信息',
                               '流程处理_限额信息',
                               '流程处理_附件信息',
                               '流程处理_流程信息',
                               '流程处理_清算信息',
                               '流程处理_放大缩小',
                               '流程处理_关闭',
                               '流程处理_同意',
                               '流程处理_拒绝',
                               '流程处理_回退到上一步',
                               '确认_是',
                               '确认_否'
                               ]:
                    if menu[n] == '确认_是':
                        self.driver.execute_script("arguments[0].click();", findelement)
                        self.wait_for_miss(120, wait)
                        self.findxpath_click(targetsheet.get('成功_确定'))
                    else:
                        findelement.click()
                # 所有操作为"输入"的元素
                elif menu[n] in ['产品代码',
                                 '产品名称',
                                 '审批单名称',
                                 '当前批复信息'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
            n = n + 1
        return True
