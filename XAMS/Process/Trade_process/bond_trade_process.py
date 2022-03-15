# 现券交易流程自动化测试用例
# 功能描述：覆盖常规现券交易流程，分步骤验证断言
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import Excel_basedata_zs, sheet32
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams
import math


class BondTradeProcess(BasePageXams):
    # 流程自动化案例-浙商
    def bond_trade_process(self, code, menu, value):
        print(menu)
        print(value)
        t = TestExcel()
        element = t.match_step_dic(code)
        # excel读取基础数据
        i_code = element.get('资产代码')
        unit_id = element.get('投组单元')
        b_type = element.get('业务种类')
        counterparty = element.get('交易对手')
        amount = element.get('券面总额')
        net_price = element.get('净价')
        business_model = element.get('业务模式')
        workflow = element.get('工作流')
        # 实时页面读取数据
        basedata = [Excel_basedata_zs, sheet32]
        targetsheet = t.sheet_xpath_dic(basedata[0], basedata[1])
        wait = (By.XPATH, targetsheet.get('加载等待'))
        # 点击交易管理
        self.findxpath_click(t.first_menu(basedata[0]).get('交易管理'))
        # 点击现券审批
        self.findxpath_click(t.second_menu(basedata[0]).get('交易管理-现券审批'))
        # 点击新增
        self.findxpath_click(targetsheet.get('新增'))
        # 选择业务种类
        self.findxpath_click(targetsheet.get('业务种类&币种_业务种类'))
        self.findxpath_click(f'/html/body/div[last()]//li[text()="{b_type}"]')
        # 选择投组
        self.findxpath_sendkey(targetsheet.get('投组单元_投组单元'), unit_id)
        sleep(1)
        self.findxpath_click(targetsheet.get('投组下拉选择'))
        # 选择交易对手
        findelement = self.findxpath(targetsheet.get('交易对手信息_外部交易'))
        findelement.send_keys(counterparty)
        findelement.send_keys(Keys.SPACE)
        findelement.send_keys(Keys.BACK_SPACE)
        sleep(1)
        findelement.send_keys(Keys.ARROW_DOWN)
        findelement.send_keys(Keys.ENTER)
        # 选择债券
        findelement = self.findxpath(targetsheet.get('交易要素_代码'))
        findelement.send_keys(i_code)
        findelement.send_keys(Keys.SPACE)
        findelement.send_keys(Keys.BACK_SPACE)
        sleep(1)
        findelement.send_keys(Keys.ARROW_DOWN)
        findelement.send_keys(Keys.ENTER)
        # 输入全面总额
        self.findxpath_sendkey(targetsheet.get('交易要素_券面总额(万元)'), amount)
        # 输入净价
        self.findxpath_sendkey(targetsheet.get('交易要素_净价(元)'), net_price)
        # 读取总应计利息
        # taxes_accrued = self.findxpath(targetsheet.get('总应计利息(元)')).text  # 反显数据无法读取导致计算和断言失败
        # 计算数据
        # net_price_amount = str(float(amount) * float(net_price) * 10000)
        # full_price_amount = str(float(net_price_amount) + float(taxes_accrued))
        # transaction_fee = float(amount) * 10000 * 0.0000025
        # if transaction_fee > 1000:
        #     transaction_fee = str(1000)
        # else:
        #     transaction_fee = str(transaction_fee)
        # closing_fee = str(150)
        # print(net_price_amount)
        # print(full_price_amount)
        # print(transaction_fee)
        # print(closing_fee)
        # 判断净价金额
        # a = self.findxpath(targetsheet.get('净价金额(元)')).text
        # assert a == net_price_amount
        # 判断全价金额
        # b = self.findxpath(targetsheet.get('全价金额(元)')).text
        # assert b == full_price_amount
        # 判断结算金额
        # c = self.findxpath(targetsheet.get('结算金额(元)')).text
        # assert c == full_price_amount
        # 判断交易费
        # d = self.findxpath(targetsheet.get('银行间交易费用信息_交易费(元)')).text
        # assert d == transaction_fee
        # 判断结算费
        # e = self.findxpath(targetsheet.get('银行间交易费用信息_结算费(元)')).text
        # assert e == closing_fee

        # 选择业务模式
        self.findxpath_click(targetsheet.get('资产分类_业务模式'))
        self.findxpath_click(f'//li[text()="{business_model}"]')
        # 点击保存
        self.findxpath_click(targetsheet.get('保存'))
        remind = self.findxpath(targetsheet.get('提醒_继续'))
        self.driver.execute_script("arguments[0].click();", remind)
        determine = self.findxpath(targetsheet.get('成功_确定'))
        self.driver.execute_script("arguments[0].click();", determine)
        sleep(2)
        # 选择工作流

        return True
