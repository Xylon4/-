# 净值型产品信息管理自动化测试用例
# 功能描述：维护净值型产品信息
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet57, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams
import math


class ValuationProduct(BasePageXams):
    # 模拟操作自动化案例-浙商
    def valuation_product_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basedata = [Excel_basedata_zs, sheet57]
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
                               '计算现金流',
                               '附件上传',
                               '收益型产品信息导入',
                               '收益型产品信息导入模板',
                               '搜索',
                               '搜索_单选框',
                               '搜索_全选框',
                               '高级查询',
                               '高级查询_查询',
                               '高级查询_重置',
                               '高级查询_返回',
                               '收益支付信息_按实际支付日期计息:是',
                               '收益支付信息_按实际支付日期计息:否',
                               '收益支付信息_按实际支付日期计息:是',
                               '收益支付信息_按实际支付日期计息:否',
                               '理财费用信息',
                               '理财费用信息_新增',
                               '理财费用信息_修改',
                               '理财费用信息_删除',
                               '理财费用信息_费率调整',
                               '理财费用信息_单选框',
                               '理财费用信息_全选框',
                               '费用设置_保存',
                               '费用设置_取消',
                               '归集账户信息',
                               '归集账户信息_新增',
                               '归集账户信息_修改',
                               '归集账户信息_删除',
                               '归集账户信息维护_是否自动生成产品清算指令:是',
                               '归集账户信息维护_是否自动生成产品清算指令:否',
                               '归集账户信息维护_保存',
                               '归集账户信息维护_取消',
                               '保存',
                               '重置',
                               '返回',
                               '利率调整',
                               '利率调整_新增',
                               '利率调整_删除',
                               '利率调整_确定',
                               '利率调整_取消',
                               '利率调整_关闭',
                               '净值周期维护',
                               '净值产品导入',
                               '净值产品模板下载',
                               '查看变更日志',
                               '费用设置_与产品一起到期:是',
                               '费用设置_与产品一起到期:否',
                               '分红方案设置',
                               '分红方案设置_新增',
                               '分红方案设置_修改',
                               '分红方案设置_删除',
                               '分红方案设置_保存',
                               '分红方案设置_重置',
                               '分红方案设置_返回',
                               '分红方案设置_删除02',
                               '分红方案设置_全选框',
                               '业绩比较基准',
                               '业绩比较基准_新增',
                               '业绩比较基准_修改',
                               '业绩比较基准_删除',
                               '基准设置_新增',
                               '基准设置_删除',
                               '基准设置_保存',
                               '基准设置_撤销',
                               '业绩比较基准_确定',
                               '业绩比较基准_取消',
                               '业绩比较基准_全选框',
                               '业绩比较基准_单选框',
                               '净值周期维护',
                               '周期日历规则_生成日历',
                               '周期日历_导出',
                               '周期日历_清空',
                               '周期日历_导入',
                               '周期日历_下载模板',
                               '周期净值产品日历维护_保存',
                               '周期净值产品日历维护_返回'
                               ]:
                    if menu[n] in ['确认_是', '确认_否', '利率调整_确定', '利率调整_取消']:
                        self.driver.execute_script("arguments[0].click();", findelement)
                        if menu[n] == '确认_是':
                            sleep(1)
                            recheck_wait = (By.XPATH, targetsheet.get('复核加载等待'))
                            self.wait_for_miss(120, recheck_wait)
                            determine = self.findxpath(targetsheet.get('成功_确定'))
                            visit = determine.is_displayed()
                            if visit:
                                self.driver.execute_script("arguments[0].click();", determine)
                    else:
                        findelement.click()
                        if menu[n] in ['搜索', '高级查询_返回']:
                            self.wait_for_miss(120, wait)
                        if menu[n] in ['保存']:
                            save_wait = (By.XPATH, targetsheet.get('保存加载等待'))
                            self.wait_for_miss(120, save_wait)
                            determine = self.findxpath(targetsheet.get('成功_确定'))
                            self.driver.execute_script("arguments[0].click();", determine)
                # 所有操作为"输入"的元素
                elif menu[n] in ['高级查询_起息日从',
                                 '高级查询_起息日止',
                                 '高级查询_到期日从',
                                 '高级查询_到期日止',
                                 '高级查询_支付日从',
                                 '高级查询_支付日止',
                                 '产品公共要素_产品代码',
                                 '产品公共要素_产品名称',
                                 '产品公共要素_产品全称',
                                 '收益支付信息_首次付息日',
                                 '收益支付信息_滚动频率:值',
                                 '个性要素_客户周期(天)',
                                 '发行信息_实际募集起始日',
                                 '发行信息_实际募集结束日',
                                 '发行信息_起息日',
                                 '发行信息_预计到期日',
                                 '发行信息_计划募集金额(元)',
                                 '发行信息_最低募集金额(元)',
                                 '发行信息_预期收益率(%)',
                                 '发行信息_收益区间(起)%',
                                 '发行信息_收益区间(止)%',
                                 '发行信息_实际到期日',
                                 '费用设置_当前费用利率(%)',
                                 '费用设置_计息开始日期',
                                 '费用设置_备注',
                                 '利率调整_调整时间',
                                 '利率调整_利率(%)',
                                 '发行信息_实际终止日',
                                 '分红方案设置_分红除权日期',
                                 '分红方案设置_单位回归净值',
                                 '基准设置_生效日期',
                                 '基准设置_基准利率乘数',
                                 '基准设置_基准更新频率:值',
                                 '业绩比较基准_业绩基准(%)',
                                 '业绩比较基准_银行超额分成比例(%)',
                                 '周期日历规则_顺延天数',
                                 '周期日历规则_开始日',
                                 '周期日历规则_频率:值',
                                 '周期日历规则_结束日'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        findelement.send_keys(value[n])
                # 所有操作为"输入后选择"的元素
                elif menu[n] in ['产品报备名称或代码',
                                 '产品名称或代码',
                                 '高级查询_产品报备名称或代码',
                                 '高级查询_产品名称或代码',
                                 '产品公共要素_产品报备名称',
                                 '归集账户信息维护_资金账号',
                                 '基准设置_基准利率'
                                 ]:
                    if value[n] == '置空':
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                    else:
                        findelement.send_keys(Keys.CONTROL, 'a' + Keys.BACK_SPACE)
                        sleep(1)
                        findelement.send_keys(value[n] + Keys.SPACE + Keys.BACK_SPACE)
                        sleep(1)
                        findelement.send_keys(Keys.ARROW_DOWN)
                        findelement.send_keys(Keys.ENTER)
                    if menu[n] in ['高级查询_产品报备名称或代码']:
                        self.findxpath_click('//span[text()="高级查询"and contains(@id,"window")]')
                # 所有操作为"点击后选择"的元素
                elif menu[n] in ['状态',
                                 '同步状态',
                                 '高级查询_状态',
                                 '高级查询_产品状态',
                                 '高级查询_交易方式',
                                 '高级查询_销售对象',
                                 '高级查询_是否代销',
                                 '高级查询_是否分行推荐产品',
                                 '高级查询_所属分行',
                                 '产品公共要素_交易方式',
                                 '产品公共要素_收益支付频率',
                                 '产品公共要素_收益计算基准',
                                 '产品公共要素_收益支付日调整规则',
                                 '产品公共要素_投资性质',
                                 '产品公共要素_是否代销',
                                 '产品公共要素_是否分行推荐产品',
                                 '产品公共要素_销售渠道',
                                 '产品公共要素_交易日历',
                                 '产品公共要素_销售对象',
                                 '产品公共要素_销售数据对接方式',
                                 '产品公共要素_募集币种',
                                 '收益支付信息_支付日期:月',
                                 '收益支付信息_支付日期:日',
                                 '收益支付信息_周期是否规则',
                                 '收益支付信息_滚动频率:单位',
                                 '个性要素_产品模板',
                                 '理财费用信息_状态',
                                 '费用设置_费用类别',
                                 '费用设置_费用基数',
                                 '费用设置_费用层次',
                                 '费用设置_基数来源',
                                 '费用设置_计提规则',
                                 '费用设置_计息基准',
                                 '费用设置_日历代码',
                                 '费用设置_计息调整规则',
                                 '费用设置_支付频率',
                                 '费用设置_支付调整规则',
                                 '费用设置_计息规则',
                                 '费用设置_支付日期:月',
                                 '费用设置_支付日期:日',
                                 '归集账户信息维护_账户分类',
                                 '归集账户信息维护_产品业务类型',
                                 '产品公共要素_所属分行',
                                 '产品公共要素_运作模式',
                                 '产品公共要素_平行分级',
                                 '分红方案设置_分红模式',
                                 '分红方案设置_分红方式',
                                 '业绩比较基准_状态',
                                 '基准设置_业绩基准类型',
                                 '基准设置_结转方式',
                                 '基准设置_计提频率',
                                 '基准设置_是否回拨',
                                 '基准设置_基准更新日调整规则',
                                 '基准设置_基准更新频率:单位',
                                 '周期日历规则_非工作日顺延',
                                 '周期日历规则_频率:单位'
                                 ]:
                    a = self.base.enumeration_list2(basedata[0], basedata[1], menu[n])
                    if menu[n] in ['同步状态',
                                   '高级查询_产品状态',
                                   '高级查询_交易方式',
                                   '高级查询_销售对象',
                                   '高级查询_所属分行',
                                   '产品公共要素_销售对象',
                                   '归集账户信息维护_产品业务类型',
                                   '分红方案设置_分红方式'
                                   ]:
                        a.append('置空')
                    if value[n] not in a:
                        print(f'值"{value[n]}"输入错误，请检查')
                        return False
                    elif value[n] == '置空':
                        findelement.click()
                        e = menu[n].__contains__('_')
                        if e:
                            select = f"{menu[n].split('_')[1]}_全选"
                        else:
                            select = f'{menu[n]}_全选'
                        selectall = self.findxpath(targetsheet.get(select))
                        action = ActionChains(self.driver)
                        action.double_click(selectall).perform()
                        findelement.click()
                    elif value[n] == '全选':
                        findelement.click()
                        e = menu[n].__contains__('_')
                        if e:
                            select = f"{menu[n].split('_')[1]}_全选"
                        else:
                            select = f'{menu[n]}_全选'
                        self.findxpath_click(targetsheet.get(select))
                        findelement.click()
                    else:
                        findelement.click()
                        if menu[n] in ['同步状态',
                                       '高级查询_产品状态',
                                       '高级查询_交易方式',
                                       '高级查询_销售对象',
                                       '高级查询_所属分行',
                                       '产品公共要素_销售对象',
                                       '归集账户信息维护_产品业务类型'
                                       ]:
                            self.findxpath_click(f'/html/body/div[last()]//li[text()=" {value[n]}"]')
                            findelement.click()
                        else:
                            self.findxpath_click(f'/html/body/div[last()]//li[text()="{value[n]}"]')
                elif menu[n] == '高级查询_代销机构':
                    findelement.click()
                    self.findxpath_click(f'/html/body/div[last()]//li[text()=" {value[n]}"]')
                    findelement.click()
                elif menu[n] == '产品公共要素_代销机构':
                    findelement.click()
                    self.findxpath_click(f'/html/body/div[last()]//li[text()="{value[n]}"]')
            n = n + 1
        return True
