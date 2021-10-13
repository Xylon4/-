# 理财估值核算系统产品端自动化测试用例
# 产品现金流新增及复核
from time import sleep

from selenium.webdriver.common.keys import Keys

from FSFA.basepage_FSFA import BasePageFsfa


class CashFlow(BasePageFsfa):
    def cashflow1(self, get_cash_flow):
        I_CODE = get_cash_flow[0]
        REAL_AMOUNT = get_cash_flow[1]
        REAL_CP = get_cash_flow[1]
        # 点击账套管理
        self.findxpath_click('//*[@id="navId"]/li[3]/a')
        # 点击产品现金流管理
        self.findxpath_click('//*[@id="floatMenu"]/dl[3]/dd[1]/a')
        sleep(2)
        # 点击新增
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div/div[1]/span/div/div[1]/div/div/a[2]')
        # 选择产品代码
        self.findxpath_sendkey('//*[@name="wmpsProductCombox-1254-inputEl"]', I_CODE)
        sleep(1)
        i_code = self.findxpath('//*[@name="wmpsProductCombox-1254-inputEl"]')
        i_code.send_keys(Keys.ARROW_DOWN)
        i_code.send_keys(Keys.ENTER)
        # 选择业务类型
        self.findxpath_click('//*[@name="trdType"]')
        trd_type = self.findxpath('//*[@name="trdType"]')
        # trd_type.send_keys(Keys.ARROW_DOWN)
        trd_type.send_keys(Keys.ENTER)
        # 输入份额、本金
        self.findxpath_sendkey('//*[@name="realAmount"]', REAL_AMOUNT)
        self.findxpath_sendkey('//*[@name="realCp"]', REAL_CP)
        # 点击保存
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div[2]/div[3]/div/div/a[1]')
        # 点击确定
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        # 点击返回
        self.findxpath_click('/html/body/div[3]/div[2]/div[2]/div/div[2]/div[3]/div/div/a[3]')
        # 定位现金流
        self.findxpath_sendkey('//*[@name="fuzzCondi"]', I_CODE)
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div[1]/div[1]/span/div/div[3]/div/div/a[1]')
        sleep(3)
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/table/tbody/tr/td[2]/div')
        # 点击复核按钮
        self.findxpath_click('/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/span/div/div[1]/div/div/a[8]')
        # 点击确定按钮
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        return True