# 产品报备管理自动化测试用例
# 功能描述：维护产品报备信息
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet55, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams
import math


class Filing(BasePageXams):
    # 模拟操作自动化案例-浙商
    def filing_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet55]
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
                               '确认_是',
                               '确认_否',
                               '查看变更日志',
                               '申报',
                               '申报成功',
                               '申报失败',
                               '报备通过未发行',
                               '发行失败',
                               '募集失败',
                               '补录报备代码',
                               '导入报备代码',
                               '下载报备代码模板',
                               '批量导入产品报备信息',
                               '下载产品报备信息导入模板',
                               '附件上传',
                               '搜索',
                               '搜索_单选框',
                               '搜索_全选框',
                               '高级查询',
                               '高级查询_查询',
                               '高级查询_重置',
                               '高级查询_返回',
                               '保存',
                               '重置',
                               '返回'
                               ]:
                    if menu[n] in ['确认_是', '确认_否']:
                        self.driver.execute_script("arguments[0].click();", findelement)
                        if menu[n] == '确认_是':
                            sleep(1)
                            determine = self.findxpath(targetsheet.get('成功_确定'))
                            self.driver.execute_script("arguments[0].click();", determine)
                    else:
                        findelement.click()
                        if menu[n] in ['搜索', '保存', '高级查询_返回']:
                            self.wait_for_miss(120, wait)
                        if menu[n] in ['保存']:
                            determine = self.findxpath(targetsheet.get('成功_确定'))
                            self.driver.execute_script("arguments[0].click();", determine)
                # 所有操作为"输入"的元素
                elif menu[n] in ['高级查询_实际起息日从',
                                 '高级查询_实际起息日止',
                                 '高级查询_实际到期日从',
                                 '高级查询_实际到期日止',
                                 '高级查询_募集起始日从',
                                 '高级查询_募集起始日止',
                                 '高级查询_募集终止日从',
                                 '高级查询_募集终止日止',
                                 '高级查询_申报日期从',
                                 '高级查询_申报日期止',
                                 '申报基本信息_产品报备代码',
                                 '申报基本信息_产品报备名称',
                                 '申报要素_产品期次',
                                 '申报要素_募集起始日期(从)',
                                 '申报要素_募集起始日期(到)',
                                 '申报要素_起点销售金额(元)',
                                 '申报要素_计划募集金额(元)',
                                 '申报要素_预计终止日',
                                 '申报要素_实际到期日',
                                 '公共监管要素_产品品牌',
                                 '公共监管要素_合作机构名称',
                                 '公共监管要素_预计客户最高年收益率%',
                                 '公共监管要素_发行机构代码',
                                 '公共监管要素_预计客户最低年收益率%:',
                                 '公共监管要素_境内托管机构代码',
                                 '公共监管要素_境外托管机构名称',
                                 '公共监管要素_备注',
                                 '理财登记托管中心监管信息_产品审批人姓名',
                                 '理财登记托管中心监管信息_产品审批人身份证号',
                                 '理财登记托管中心监管信息_产品设计人姓名',
                                 '理财登记托管中心监管信息_产品设计人身份证号',
                                 '理财登记托管中心监管信息_投资经理姓名',
                                 '理财登记托管中心监管信息_投资经理身份证号',
                                 '理财登记托管中心监管信息_业务联络人姓名',
                                 '理财登记托管中心监管信息_业务联络人邮箱',
                                 '理财登记托管中心监管信息_业务联络人座机',
                                 '理财登记托管中心监管信息_业务联络人手机',
                                 '理财登记托管中心监管信息_最短持有期限(天)',
                                 '理财登记托管中心监管信息_其他规律开放周期(天)',
                                 '理财登记托管中心监管信息_无规律开放说明',
                                 '理财登记托管中心监管信息_首次开放周期起始日',
                                 '理财登记托管中心监管信息_平均开放次数(年化)',
                                 '理财登记托管中心监管信息_开放期业务说明',
                                 '理财登记托管中心监管信息_投资资产种类及比例',
                                 '理财登记托管中心监管信息_业绩比较基准%',
                                 '理财登记托管中心监管信息_实际管理人名称',
                                 '理财登记托管中心监管信息_业绩比较基准上限%',
                                 '理财登记托管中心监管信息_销售手续费率%',
                                 '理财登记托管中心监管信息_业绩比较基准下限%',
                                 '理财登记托管中心监管信息_投资管理费率%',
                                 '理财登记托管中心监管信息_业绩比较基准说明',
                                 '理财登记托管中心监管信息_托管费率%',
                                 '理财登记托管中心监管信息_产品登记编码',
                                 '人行监管信息_产品对应资产池代码',
                                 '人行监管信息_人行代码'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['公共监管要素_产品增信机构类型',
                                 '理财登记托管中心监管信息_产品销售区域',
                                 '理财登记托管中心监管信息_资金托管账户',
                                 '理财登记托管中心监管信息_结构性产品挂钩标的',
                                 '产品报备名称或代码',
                                 '高级查询_产品报备名称或代码',
                                 '申报基本信息_产品系列模板'
                                 ]:
                    if menu[n] in ['理财登记托管中心监管信息_资金托管账户',
                                   '产品报备名称或代码',
                                   '高级查询_产品报备名称或代码',
                                   '申报基本信息_产品系列模板'
                                   ] and value[n] == '全选':
                        print('你不能钻空子，命名为"全选"，这会让下拉框中的全选很为难')
                        return False
                    else:
                        if menu[n] in ['公共监管要素_产品增信机构类型',
                                       '理财登记托管中心监管信息_产品销售区域',
                                       '理财登记托管中心监管信息_结构性产品挂钩标的']:
                            a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                            if value[n] not in a:
                                print(f'值"{value[n]}"输入错误，请检查')
                                return False
                        if value[n] == '置空':
                            findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        elif value[n] == '全选':
                            findelement.send_keys(value[n] + Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                            if menu[n] == '公共监管要素_产品增信机构类型':
                                self.findxpath_click('//li[text()=" 01 广义政府"]/../../preceding-sibling::div')
                                self.findxpath_click('//label[text()="产品增信机构类型:"]')
                            elif menu[n] == '理财登记托管中心监管信息_产品销售区域':
                                self.findxpath_click('//li[text()=" 110000 北京市"]/../../preceding-sibling::div')
                                self.findxpath_click('//label[text()="产品销售区域:"]')
                            elif menu[n] == '理财登记托管中心监管信息_结构性产品挂钩标的':
                                self.findxpath_click('//li[text()=" 01 利率"]/../../preceding-sibling::div')
                                self.findxpath_click('//label[text()="结构性产品挂钩标的:"]')
                        else:
                            findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                            sleep(1)
                            findelement.send_keys(value[n] + Keys.SPACE + Keys.BACK_SPACE)
                            sleep(1)
                            if menu[n] in ['公共监管要素_产品增信机构类型',
                                           '理财登记托管中心监管信息_产品销售区域',
                                           '理财登记托管中心监管信息_资金托管账户',
                                           '理财登记托管中心监管信息_结构性产品挂钩标的',
                                           '产品报备名称或代码',
                                           '高级查询_产品报备名称或代码',
                                           '申报基本信息_产品系列模板'
                                           ]:
                                findelement.send_keys(Keys.ARROW_DOWN)
                                findelement.send_keys(Keys.ENTER)
                                if menu[n] in ['公共监管要素_产品增信机构类型',
                                               '理财登记托管中心监管信息_产品销售区域',
                                               '理财登记托管中心监管信息_结构性产品挂钩标的']:
                                    self.findxpath_click('//label[text()="产品增信机构类型:"]')
                # 所有操作为"点击后选择"的元素
                elif menu[n] in ['状态',
                                 '高级查询_产品收益类型',
                                 '高级查询_客户类型',
                                 '高级查询_是否金融同业专属',
                                 '高级查询_产品募集方式',
                                 '高级查询_产品投资性质',
                                 '高级查询_新老产品标志',
                                 '公共监管要素_合作模式',
                                 '公共监管要素_产品增信标识',
                                 '公共监管要素_产品增信形式',
                                 '公共监管要素_资金投向地区',
                                 '公共监管要素_境内托管机构名称',
                                 '公共监管要素_产品投资国家或地区(境外)',
                                 '公共监管要素_境外托管机构国别',
                                 '公共监管要素_客户赎回权标识',
                                 '公共监管要素_兑付本金币种',
                                 '公共监管要素_兑付收益币种',
                                 '理财登记托管中心监管信息_是否设置最短持有期限',
                                 '理财登记托管中心监管信息_最短持有期后是否自由赎回',
                                 '理财登记托管中心监管信息_是否现金管理类',
                                 '理财登记托管中心监管信息_是否为结构化(分级)产品',
                                 '理财登记托管中心监管信息_规律开放周期',
                                 '理财登记托管中心监管信息_开放模式',
                                 '理财登记托管中心监管信息_节假日是否开放',
                                 '理财登记托管中心监管信息_开放期业务',
                                 '理财登记托管中心监管信息_产品管理模式',
                                 '理财登记托管中心监管信息_产品定价方式',
                                 '理财登记托管中心监管信息_投资者风险偏好',
                                 '理财登记托管中心监管信息_产品资产配置方式',
                                 '理财登记托管中心监管信息_发行机构提前终止权标识',
                                 '理财登记托管中心监管信息_投资收益到账日',
                                 '理财登记托管中心监管信息_理财业务服务模式',
                                 '理财登记托管中心监管信息_管理方式',
                                 '理财登记托管中心监管信息_产品风险等级',
                                 '理财登记托管中心监管信息_投资本金到账日',
                                 '人行监管信息_业务模式',
                                 '人行监管信息_管理方式',
                                 '人行监管信息_收益保障标识',
                                 '人行监管信息_产品类型',
                                 '人行监管信息_提前终止权标识',
                                 '人行监管信息_本金保障标识',
                                 '人行监管信息_受托职责',
                                 '人行监管信息_产品期限（人行）',
                                 '人行监管信息_客户类型（人行）',
                                 '人行监管信息_收益权转让产品标识',
                                 '人行监管信息_分级产品标识',
                                 '产品状态',
                                 '高级查询_产品状态',
                                 '高级查询_产品期限',
                                 '申报基本信息_产品种类',
                                 '申报基本信息_是否金融同业专属',
                                 '申报基本信息_客户类型',
                                 '申报基本信息_产品运作模式',
                                 '申报要素_产品收益类型',
                                 '申报要素_产品期限',
                                 '申报要素_产品投资性质',
                                 '申报要素_产品募集方式',
                                 '申报要素_新老产品标志',
                                 '申报要素_募集币种',
                                 '理财登记托管中心监管信息_是否完全符合《通知》要求',
                                 '人行监管信息_理财产品发起机构标识'
                                 ]:
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    if menu[n] in ['产品状态',
                                   '高级查询_产品状态',
                                   '高级查询_产品期限',
                                   '申报基本信息_客户类型',
                                   '高级查询_产品收益类型',
                                   '高级查询_客户类型',
                                   '高级查询_是否金融同业专属',
                                   '高级查询_产品募集方式',
                                   '高级查询_产品投资性质',
                                   '高级查询_新老产品标志',
                                   '公共监管要素_产品投资国家或地区(境外)',
                                   '公共监管要素_境外托管机构国别',
                                   '理财登记托管中心监管信息_投资者风险偏好',
                                   '人行监管信息_客户类型（人行）'
                                   ]:
                        a.append('置空')
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    elif value[n] == '置空':
                        findelement.click()
                        if menu[n] == '高级查询_产品收益类型':
                            selectall = self.findxpath('//li[text()=" 01 保证收益型"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                        elif menu[n] == '高级查询_客户类型':
                            selectall = self.findxpath(
                                '//li[text()=" 个人"and @class="x-boundlist-item"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                        elif menu[n] == '高级查询_是否金融同业专属':
                            selectall = self.findxpath('//li[text()=" 01 是"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                        elif menu[n] == '高级查询_产品募集方式':
                            selectall = self.findxpath('//li[text()=" 01 公募"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                        elif menu[n] == '高级查询_产品投资性质':
                            selectall = self.findxpath('//li[text()=" 01 固定收益类"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                        elif menu[n] == '高级查询_新老产品标志':
                            selectall = self.findxpath('//li[text()=" 01 新产品"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                        elif menu[n] == '申报基本信息_客户类型':
                            selectall = self.findxpath(
                                '//li[text()=" 个人"and contains(@class,"selected")]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                        elif menu[n] == '公共监管要素_产品投资国家或地区(境外)':
                            selectall = self.findxpath(
                                '/html/body/div[last()]//li[text()=" AUS 澳大利亚"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                        elif menu[n] == '公共监管要素_境外托管机构国别':
                            selectall = self.findxpath(
                                '/html/body/div[last()]//li[text()=" AUS 澳大利亚"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                        elif menu[n] == '理财登记托管中心监管信息_投资者风险偏好':
                            selectall = self.findxpath('//li[text()=" 01 保守型"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                        elif menu[n] == '人行监管信息_客户类型（人行）':
                            selectall = self.findxpath('//li[text()=" 住户"]/../../preceding-sibling::div')
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                        elif menu[n] in ['产品状态', '高级查询_产品状态']:
                            selectall = self.findxpath(targetsheet.get('产品状态_全选'))
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                        elif menu[n] == '高级查询_产品期限':
                            selectall = self.findxpath(targetsheet.get('产品期限_全选'))
                            action = ActionChains(self.driver)
                            action.double_click(selectall).perform()
                        findelement.click()
                    elif value[n] == '全选':
                        findelement.click()
                        if menu[n] == '高级查询_产品收益类型':
                            self.findxpath_click('//li[text()=" 01 保证收益型"]/../../preceding-sibling::div')
                        elif menu[n] == '高级查询_客户类型':
                            self.findxpath_click(
                                '//li[text()=" 个人"and @class="x-boundlist-item"]/../../preceding-sibling::div')
                        elif menu[n] == '高级查询_是否金融同业专属':
                            self.findxpath_click('//li[text()=" 01 是"]/../../preceding-sibling::div')
                        elif menu[n] == '高级查询_产品募集方式':
                            self.findxpath_click('//li[text()=" 01 公募"]/../../preceding-sibling::div')
                        elif menu[n] == '高级查询_产品投资性质':
                            self.findxpath_click('//li[text()=" 01 固定收益类"]/../../preceding-sibling::div')
                        elif menu[n] == '高级查询_新老产品标志':
                            self.findxpath_click('//li[text()=" 01 新产品"]/../../preceding-sibling::div')
                        elif menu[n] == '申报基本信息_客户类型':
                            self.findxpath_click(
                                '//li[text()=" 个人"and contains(@class,"selected")]/../../preceding-sibling::div')
                        elif menu[n] == '公共监管要素_产品投资国家或地区(境外)':
                            self.findxpath_click(
                                '/html/body/div[last()]//li[text()=" AUS 澳大利亚"]/../../preceding-sibling::div')
                        elif menu[n] == '公共监管要素_境外托管机构国别':
                            self.findxpath_click(
                                '/html/body/div[last()]//li[text()=" AUS 澳大利亚"]/../../preceding-sibling::div')
                        elif menu[n] == '理财登记托管中心监管信息_投资者风险偏好':
                            self.findxpath_click('//li[text()=" 01 保守型"]/../../preceding-sibling::div')
                        elif menu[n] == '人行监管信息_客户类型（人行）':
                            self.findxpath_click('//li[text()=" 住户"]/../../preceding-sibling::div')
                            self.findxpath_click('//label[text()="人行代码:"]')
                            # self.findxpath_click('//label[text()="客户类型（人行）:"]/../following-sibling::td//td[2]/div')
                        elif menu[n] in ['产品状态', '高级查询_产品状态']:
                            self.findxpath_click(targetsheet.get('产品状态_全选'))
                        elif menu[n] == '高级查询_产品期限':
                            self.findxpath_click(targetsheet.get('产品期限_全选'))
                        if menu[n] not in ['人行监管信息_客户类型（人行）']:
                            findelement.click()
                    else:
                        findelement.click()
                        if menu[n] in ['产品状态',
                                       '高级查询_产品状态',
                                       '高级查询_产品期限',
                                       '申报基本信息_客户类型',
                                       '高级查询_产品收益类型',
                                       '高级查询_客户类型',
                                       '高级查询_是否金融同业专属',
                                       '高级查询_产品募集方式',
                                       '高级查询_产品投资性质',
                                       '高级查询_新老产品标志',
                                       '公共监管要素_产品投资国家或地区(境外)',
                                       '公共监管要素_境外托管机构国别',
                                       '理财登记托管中心监管信息_投资者风险偏好',
                                       '人行监管信息_客户类型（人行）'
                                       ]:
                            self.findxpath_click(f'/html/body/div[last()]//li[text()=" {value[n]}"]')
                            if menu[n] in ['人行监管信息_客户类型（人行）']:
                                # self.findxpath_click('//label[text()="客户类型（人行）:"]/../following-sibling::td//td[2]/div')
                                self.findxpath_click('//label[text()="人行代码:"]')
                            else:
                                findelement.click()
                        else:
                            self.findxpath_click(f'/html/body/div[last()]//li[text()="{value[n]}"]')
            n = n + 1
        return True
