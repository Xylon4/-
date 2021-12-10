# 债券类资产(新)自动化测试用例
# 功能描述：债券条款维护
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet29, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class Bond(BasePageXams):
    # 模拟操作自动化案例
    def bond_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        basepagewait = (By.XPATH, self.base.sheet_xpath_dic(Excel_basedata_zs, sheet29).get('首页加载等待'))
        self.wait_for_visit(120, basepagewait)
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu().get(menu[0]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu().get(f'{menu[0]}-{menu[1]}'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 2
        while n < l:
            targetsheet = self.base.sheet_xpath_dic(Excel_basedata_zs, sheet29)
            findelement = self.findxpath(targetsheet.get(menu[n]))
            wait = (By.XPATH, targetsheet.get('加载等待'))
            if menu[n] == '导出':
                findelement.click()
            elif menu[n] == 'Excel(当前页)':
                findelement.click()
            elif menu[n] == 'Excel(所有数据)':
                findelement.click()
            elif menu[n] == '新增':
                findelement.click()
            elif menu[n] == '修改':
                findelement.click()
            elif menu[n] == '删除':
                findelement.click()
            elif menu[n] == '复核':
                findelement.click()
            elif menu[n] == '计算现金流':
                findelement.click()
            elif menu[n] == '刷新金融工具':
                findelement.click()
            elif menu[n] == '市场计算':
                findelement.click()
            elif menu[n] == '资产状态':
                if value[n] not in ['已生效', '未生效']:
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
                else:
                    findelement.click()
                    self.findxpath_click(targetsheet.get(value[n]))
                    sleep(1)  # 点击后立即生效查询
            elif menu[n] == '代码':
                if value[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(value[n])
            elif menu[n] == '产品分类':
                if value[n] == '置空':
                    findelement.click()
                    selectall = self.findxpath(targetsheet.get('全选'))
                    action = ActionChains(self.driver)
                    action.double_click(selectall).perform()
                    findelement.click()  # 收起下拉框
                else:
                    findelement.click()
                    self.findxpath_click(targetsheet.get(value[n]))
                    findelement.click()  # 收起下拉框
            elif menu[n] == '条款是否完整':
                if value[n] not in ['完整', '不完整', '置空']:
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
                elif value[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(value[n])
            elif menu[n] == '搜索':
                findelement.click()
                # self.wait_for_miss(120, wait)
                sleep(1)
            # 所有操作为"输入"的元素
            elif menu[n] in ['基本信息_代码',
                             '基本信息_银行间代码',
                             '基本信息_上交所代码',
                             '基本信息_深交所代码',
                             '基本信息_报盘代码',
                             '基本信息_全称',
                             '基本信息_简称',
                             '基本信息_上市日期',
                             '含权信息_实际行权日',
                             '含权信息_行权价格(元)',
                             '美式:行权开始日期',
                             '美式:行权结束日期',
                             '利率补偿(%)',
                             '行权意向开始日',
                             '行权意向结束日',
                             '欧式:行权日期',
                             '提前兑付及赎回事件_公布日期',
                             '提前兑付及赎回事件_提前终止日期',
                             '提前兑付及赎回事件_提前终止支付日期',
                             '提前兑付及赎回事件_兑付净价',
                             '提前兑付及赎回事件_兑付利息',
                             '其他管理信息_oCode',
                             '其他管理信息_特殊授信编号',
                             '其他管理信息_资金投向行业',
                             '备注信息_备注一',
                             '备注信息_备注二',
                             '备注信息_备注三',
                             '备注信息_备注四',
                             '备注信息_备注五',
                             '备注信息_备注六',
                             '备注信息_备注七',
                             '备注信息_备注八',
                             '备注信息_备注九',
                             '备注信息_备注十',
                             '计息信息_发行日期',
                             '计息信息_发行价格(元)',
                             '计息信息_起息日',
                             '计息信息_到期日',
                             '计息信息_首次付息日',
                             '计息信息_利率(%)',
                             '计息信息_利差(BP)',
                             '计息信息_浮动利率乘数',
                             '计息信息_首规则起息日',
                             '计息信息_首周期定息日',
                             '计息信息_首周期定息值(%)',
                             '计息信息_浮动上限(%)',
                             '计息信息_浮动下线(%)',
                             '评级信息_债项发行评级机构（外部）',
                             '利率调整_利率（%）',
                             '利率调整_利率调整日_固定',
                             '利率调整_利率调整日_浮动',
                             '利率调整_利差（BP）',
                             '利率调整_利率乘数',
                             '本金序列_还款日期',
                             '本金序列_本次偿还本金',
                             '批量新增不规则计息区间_期数',
                             '不规则计息区间_计息结束日',
                             '不规则计息区间_本次偿还本金(元)',
                             '不规则计息区间_利率(%)',
                             '不规则计息区间_重置日',
                             '不规则计息区间_乘数',
                             '不规则计息区间_利差(BP)',
                             '不规则计息区间_浮动上限(%)',
                             '不规则计息区间_浮动下限(%)',
                             '不规则计息区间_支付日期'
                             ]:
                if value[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(value[n])
            # 所有操作为"下拉选择"的元素
            elif menu[n] in ['基本信息_币种',
                             '基本信息_产品类型',
                             '基本信息_产品分类',
                             '基本信息_资产化类型',
                             '基本信息_报价方式',
                             '基本信息_清偿等级',
                             '基本信息_簿记场所',
                             '基本信息_发行方式(按对象划分)',
                             '含权信息_含权信息',
                             '含权信息_行权类型',
                             '其他管理信息_是否分行推荐',
                             '其他管理信息_推荐分行',
                             '其他管理信息_考核归属机构',
                             '其他管理信息_是否须配置分行个性化产品',
                             '其他管理信息_是否双计收益',
                             '其他管理信息_底层是否本行资产',
                             '其他管理信息_是否为我行主承',
                             '其他管理信息_风险分类',
                             '其他管理信息_是否永续债',
                             '其他管理信息_是否权益类',
                             '其他管理信息_是否通过SPPI测试',
                             '其他管理信息_是否不良',
                             '其他管理信息_是否城投债',
                             '计息信息_发行方式',
                             '计息信息_到期收益率计息基准',
                             '计息信息_交易计息基准',
                             '计息信息_后台到期收益率计息基准',
                             '计息信息_后台计息基准',
                             '计息信息_计息区间',
                             '计息信息_息票类型',
                             '计息信息_计息频率',
                             '计息信息_计息调整规则',
                             '计息信息_付息频率',
                             '计息信息_支付调整',
                             '计息信息_重置日调整规则',
                             '计息信息_重置频率',
                             '计息信息_定盘日调整规则',
                             '评级信息_债项当前评级（外部）',
                             '评级信息_债项评级机构（外部）',
                             '评级信息_债项评级(内部)',
                             '评级信息_评级是否负面',
                             '担保信息维护_担保方式',
                             '不规则计息区间_是否还本',
                             '不规则计息区间_重置调整',
                             '不规则计息区间_定盘日调整规则',
                             '不规则计息区间_定盘日调整方式',
                             '不规则计息区间_支付调整'
                             ]:
                elementlist = targetsheet.keys()
                if value[n] not in elementlist:
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
                else:
                    findelement.click()
                    self.findxpath_click(targetsheet.get(value[n]))
            # 所有操作为"点击"或"勾选"的元素
            elif menu[n] in ['基本信息_发行量(亿元)',
                             '债券发行量_新增',
                             '债券发行量_删除',
                             '债券发行量_保存',
                             '债券发行量_返回',
                             '基本信息_是否资讯覆盖',
                             '基本信息_是否提前兑付及赎回',
                             '基本信息_是否含权',
                             '自定义含权日期_新增',
                             '自定义含权日期_一键清空',
                             '担保信息_新增',
                             '担保信息_修改',
                             '担保信息_删除',
                             '担保信息_勾选框',
                             '担保信息维护_保存',
                             '担保信息维护_取消',
                             '利率调整_新增',
                             '利率调整_修改',
                             '利率调整_删除',
                             '利率调整_勾选框',
                             '利率调整_确定_固定',
                             '利率调整_取消_固定',
                             '利率调整_确定_浮动',
                             '利率调整_取消_浮动',
                             '本金序列_新增',
                             '本金序列_修改',
                             '本金序列_删除',
                             '本金序列_勾选框',
                             '本金序列_确定',
                             '本金序列_取消',
                             '不规则计息区间_新增',
                             '不规则计息区间_批量新增',
                             '批量新增不规则计息区间_确定',
                             '批量新增不规则计息区间_取消',
                             '不规则计息区间_修改',
                             '不规则计息区间_删除',
                             '不规则计息区间_勾选框',
                             '不规则计息区间_确定',
                             '不规则计息区间_取消',
                             '重置',
                             '返回',
                             '搜索_勾选框',
                             '删除_是',
                             '删除_否',
                             '复核_是',
                             '复核_否'
                             ]:
                findelement.click()
            elif menu[n] == '债券发行量_发行量(亿元)':
                circulation = value[n].split(',')
                begdate = self.findxpath(targetsheet.get('债券发行量_发行开始日期'))
                findelement.send_keys(Keys.CONTROL, 'a')
                findelement.send_keys(Keys.BACK_SPACE)
                findelement.send_keys(circulation[0])
                begdate.send_keys(Keys.CONTROL, 'a')
                begdate.send_keys(Keys.BACK_SPACE)
                begdate.send_keys(circulation[1])
                self.findxpath_click(targetsheet.get('债券发行量_确定'))
            elif menu[n] == '保存':
                findelement.click()
                # self.wait_for_miss(60, wait)
                sleep(2)
                self.findxpath_click(targetsheet.get('确定'))
            elif menu[n] in ['基本信息_发行机构', '担保信息维护_担保机构']:
                findelement.send_keys(value[n])
                findelement.send_keys(Keys.SPACE)
                findelement.send_keys(Keys.BACK_SPACE)
                sleep(1)
                findelement.send_keys(Keys.ARROW_DOWN)
                findelement.send_keys(Keys.ENTER)
            elif menu[n] == '自定义含权日期_自定义日期':
                customvalue = value[n].split(',')
                compensation = self.findxpath(targetsheet.get('自定义含权日期_利率补偿(%)'))
                findelement.click()
                findelement.send_keys(customvalue[0])
                compensation.click()
                compensation.send_keys(customvalue[1])
            elif menu[n] in ['计息信息_期限', '计息信息_定盘日偏移', '不规则计息区间_定盘日偏移-不规则', '批量新增不规则计息区间_频率']:  # 注意命名规范：模块名_字段名
                droplist = menu[n].split('_')
                timevalue = value[n].split(',')
                findelement.send_keys(Keys.CONTROL, 'a')
                findelement.send_keys(Keys.BACK_SPACE)
                findelement.send_keys(timevalue[0])
                self.findxpath_click(targetsheet.get(f'{droplist[1]}_下拉框'))
                self.findxpath_click(targetsheet.get(timevalue[1]))
            elif menu[n] == '基本信息_市场类型':
                marketvalue = value[n].split(',')
                if marketvalue[0] == '市场类型_上交所' and marketvalue[1] != '托管场所_中国证券登记公司上海分公司':
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
                elif marketvalue[0] == '市场类型_深交所' and marketvalue[1] != '托管场所_中国证券登记公司深圳分公司':
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
                elif marketvalue[0] == '市场类型_其他' and marketvalue[1] != '托管场所_其他':
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
                elif marketvalue[0] == '市场类型_柜台' and marketvalue[1] != '托管场所_其他':
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
                elif marketvalue[0] in ['市场类型_银行间', '市场类型_其他市场', '市场类型_中证报价系统'] and marketvalue[1] not in [
                    '托管场所_中央国债登记结算有限责任公司', '托管场所_银行间市场清算所股份有限公司']:
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
                else:
                    findelement.click()
                    self.findxpath_click(targetsheet.get(marketvalue[0]))
                    self.findxpath_click(targetsheet.get('基本信息_托管场所'))
                    self.findxpath_click(targetsheet.get(marketvalue[1]))
            else:
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            n = n + 1
        return True
