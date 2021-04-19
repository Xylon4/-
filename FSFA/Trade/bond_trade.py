# 理财估值核算系统产品端自动化测试用例
# 银行间债券交易(二级市场)-买入及成交确认
from time import sleep

from selenium.webdriver.common.keys import Keys

from FSFA.basepage_FSFA import BasePageFsfa


class BondTrade(BasePageFsfa):
    # 新增债券交易买入及成交确认
    def bondtrade1(self):
        I_CODE = "FB0419"
        Counterparties = "杭州银行股份有限公司"
        BOND_CODE = "autotest_bond"
        AMONUT = "10000"
        YTM = "7.9"
        # 点击交易管理
        self.findxpath_click('//*[@id="navId"]/li[5]/a')
        # 点击银行间债券交易(二级市场)
        self.findxpath_click('//*[@id="floatMenu"]/dl[1]/dd[1]/a')
        # 点击新增
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div/div[1]/span/div/div[1]/div/div/a[2]/span/span/span[1]')
        # 选择账套单元
        self.findxpath_sendkey('//*[@name="package_code"]', I_CODE)
        sleep(1)
        self.findxpath_click('//div[3]/div/table/tbody/tr[2]/td/div/span')
        # 选择交易对手
        self.findxpath_sendkey('//*[@name="partyId"]', Counterparties)
        sleep(1)
        party_id = self.findxpath('//*[@name="partyId"]')
        party_id.send_keys(Keys.SPACE)
        sleep(2)
        party_id.send_keys(Keys.ARROW_DOWN)
        party_id.send_keys(Keys.ENTER)
        # 选择债券
        self.findxpath_sendkey('//fieldset[6]/div/span/div/div[1]/span/div/table[1]/tbody/tr/td[2]/table/tbody/tr/td[1]/input', BOND_CODE)
        sleep(1)
        bond_code1 = self.findxpath('//fieldset[6]/div/span/div/div[1]/span/div/table[1]/tbody/tr/td[2]/table/tbody/tr/td[1]/input')
        bond_code1.send_keys(Keys.ARROW_DOWN)
        bond_code1.send_keys(Keys.ENTER)
        # 输入券面总额
        self.findxpath_sendkey('//*[@name="countWrap"]', AMONUT)
        # 输入到期收益率
        self.findxpath_sendkey('//*[@name="mtrYtmWrap"]', YTM)
        sleep(1)
        # 点击保存
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div/a[2]')
        # self.findxpath_click('//div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div/a[2]/span/span/span[1]')
        sleep(5)
        # 点击确定
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        # 点击复核
        self.findxpath_click('/html/body/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div/a[5]')
        sleep(3)
        # 点击确定
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        # 定位交易
        # self.findxpath_sendkey('//*[@name="code"]', BOND_CODE)
        # bond_code2 = self.findxpath('//*[@name="code"]')
        # bond_code2.send_keys(Keys.ARROW_DOWN)
        # bond_code2.send_keys(Keys.ENTER)
        # self.findxpath_click('//div[3]/div[2]/div[3]/div/div/div[1]/span/div/div[3]/div/div/a[1]')
        # sleep(1)
        # self.findxpath_click('/html/body/div[3]/div[2]/div[3]/div/div/div[3]/div/table/tbody/tr/td[4]/div')
        return True

    # 结算债券首期交易
    def bondtrade2(self):
        BOND_CODE = "autotest_bond"
        # 点击清算管理
        self.findxpath_click('//*[@id="navId"]/li[6]/a')
        # 点击待复核交易指令
        self.findxpath_click('//*[@id="floatMenu"]/dl[1]/dd[1]/a')
        # 定位交易
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div/div[1]/a/span/span/span[2]')
        self.findxpath_click('//div[7]/div/div[2]/div[2]/div[2]/a')
        self.findxpath_click('//div[2]/span/div/div[2]/span/div/table[4]/tbody/tr/td[2]/table/tbody/tr/td[1]/input')
        sleep(1)
        self.findxpath_sendkey('//div[2]/span/div/div[2]/span/div/table[4]/tbody/tr/td[2]/table/tbody/tr/td[1]/input', BOND_CODE)
        sleep(1)
        bond_code = self.findxpath(
            '//div[2]/span/div/div[2]/span/div/table[4]/tbody/tr/td[2]/table/tbody/tr/td[1]/input')
        bond_code.send_keys(Keys.ARROW_DOWN)
        bond_code.send_keys(Keys.ENTER)
        sleep(1)
        self.findxpath_click('//div[3]/div/div/a[1]')
        sleep(1)
        self.findxpath_click('//div[3]/div/div/a[2]')
        sleep(2)
        self.findxpath_click('//div/div/div[3]/div/table/tbody/tr/td[2]/div')
        # 点击复核
        self.findxpath_click('/html/body/div[3]/div[2]//div/div/div[1]/div/div/a[2]')
        # 点击弹窗中的是
        self.findxpath_click('//*[@id="button-1006-btnIconEl"]')
        # 点击确定
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        return True

    # 银行间费用摊销复核
    def bondtrade3(self):
        I_CODE = "FB0419"
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