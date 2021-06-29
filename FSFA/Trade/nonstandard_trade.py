# 理财估值核算系统交易端自动化测试用例
# 利率型项目交易-买入及成交确认
from time import sleep

from selenium.webdriver.common.keys import Keys

from FSFA.basepage_FSFA import BasePageFsfa


class NonstandardTrade(BasePageFsfa):
    # 利率型项目交易买入及成交确认
    def nonstandardtrade1(self):
        UNIT_CODE = 'FB0618'
        I_CODE = 'LBS20210601'
        Counterparties = "杭州银行股份有限公司"
        # 点击交易管理
        self.findxpath_click('//*[@id="navId"]/li[5]/a')
        # 点击利率型项目交易
        self.findxpath_click('//*[@id="floatMenu"]/dl[5]/dd[1]/a')
        # 点击新增
        self.findxpath_click('//div[3]/div[2]/div[2]//div[1]/span/div/div[1]//a[2]/span/span/span[1]')
        # 选择账套
        self.findxpath_sendkey('//*[@name="package_code"]', UNIT_CODE)
        sleep(1)
        self.findxpath_click('//div[30]/div[3]/div/table/tbody/tr[2]/td/div/span')
        # 选择交易对手
        self.findxpath_sendkey('//*[@name="partyId"]', Counterparties)
        sleep(1)
        party_id = self.findxpath('//*[@name="partyId"]')
        party_id.send_keys(Keys.SPACE)
        sleep(2)
        party_id.send_keys(Keys.ARROW_DOWN)
        party_id.send_keys(Keys.ENTER)
        # 选择资产
        self.findxpath_sendkey('//*[@name="i_code"]', I_CODE)
        sleep(1)
        asset = self.findxpath('//*[@name="i_code"]')
        asset.send_keys(Keys.ARROW_DOWN)
        asset.send_keys(Keys.ENTER)
        # 点击保存
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div/a[2]/span/span/span[1]')
        sleep(5)
        # 点击确定
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        # 点击复核
        self.findxpath_click('/html/body/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div/a[5]')
        sleep(3)
        # 点击确定
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        return True

    # 结算非标首期交易
    def nonstandardtrade2(self):
        I_CODE = 'LBS20210601'
        # 点击清算管理
        self.findxpath_click('//*[@id="navId"]/li[6]/a')
        # 点击待复核交易指令
        self.findxpath_click('//*[@id="floatMenu"]/dl[1]/dd[1]/a')
        # 定位交易
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div/div[1]/a/span/span/span[2]')
        self.findxpath_click('//div[7]/div/div[2]/div[2]/div[2]/a')
        self.findxpath_click('//div[2]/span/div/div[2]/span/div/table[4]/tbody/tr/td[2]/table/tbody/tr/td[1]/input')
        sleep(1)
        self.findxpath_sendkey('//div[2]/span/div/div[2]/span/div/table[4]/tbody/tr/td[2]/table/tbody/tr/td[1]/input',
                               I_CODE)
        sleep(1)
        bond_code = self.findxpath(
            '//div[2]/span/div/div[2]/span/div/table[4]/tbody/tr/td[2]/table/tbody/tr/td[1]/input')
        bond_code.send_keys(Keys.ARROW_DOWN)
        bond_code.send_keys(Keys.ENTER)
        sleep(1)
        self.findxpath_click('//div[3]/div/div/a[1]')
        sleep(1)
        self.findxpath_click('//div[3]/div/div/a[2]')
        sleep(3)
        self.findxpath_click('//div/div/div[3]/div/table/tbody/tr/td[2]/div')
        # 点击复核
        self.findxpath_click('/html/body/div[3]/div[2]//div/div/div[1]/div/div/a[2]')
        # 点击弹窗中的是
        self.findxpath_click('//*[@id="button-1006-btnIconEl"]')
        # 点击确定
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        return True

    # 银行间费用摊销复核
    def nonstandardtrade3(self):
        I_CODE = "FB0618"
        # 点击交易管理
        self.findxpath_click('//*[@id="navId"]/li[5]/a')
        # 点击银行间费用摊销
        self.findxpath_click('//*[@id="floatMenu"]/dl[9]/dd[6]/a')
        # 定位账套
        self.findxpath_sendkey('//*[@name="wmsunitname$array"]', I_CODE)
        sleep(1)
        self.findxpath_click('//div[3]/div/table/tbody/tr[2]/td/div/span')
        self.findxpath_click('//div[3]/div[2]//div/div/div[1]/span/div/div[2]/div/div/a[1]')
        sleep(1)
        self.findxpath_click('//div[3]/div[2]//div/div/div[3]/div/table/tbody/tr/td[2]/div')
        # 点击复核
        self.findxpath_click('//div[3]/div[2]//div/div/div[1]/span/div/div[1]/div/div/a[6]')
        # 点击弹窗中的是
        self.findxpath_click('//*[@id="button-1006-btnIconEl"]')
        # 点击确定
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        return True
