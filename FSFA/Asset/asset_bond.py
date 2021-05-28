# 理财估值核算系统资产端自动化测试用例
# 债券新增及复核
from FSFA.basepage_FSFA import BasePageFsfa
from selenium.webdriver.common.keys import Keys


class AssetBond(BasePageFsfa):
    def assetbond1(self):
        I_CODE = 'bond20210528'
        B_NAME1 = '银行债20210528'
        B_NAME2 = '商业银行债20210528'
        P_CLASS = '商业银行债-直接投资'
        # 点击资产管理
        self.findxpath_click('//*[@id="navId"]/li[4]/a')
        # 点击债券类资产
        self.findxpath_click('//*[@id="floatMenu"]/dl[1]/dd[1]/a')
        # 点击新增按钮
        self.findxpath_click('/html/body/div[3]/div[2]/div[2]//div[1]/div[1]/span/div/div[1]//a[2]/span/span/span[1]')
        # 输入债券代码
        self.findxpath_sendkey('//*[@name="iCode"]', I_CODE)
        # 选择市场类型
        self.findxpath_click(
            '//div[3]//div[2]//div[2]//div[1]/span/div/fieldset[1]//table[2]/tbody/tr/td[2]//tr/td[1]/input')
        M_TYPE = self.findxpath('//div[3]//div[2]//div[2]//div[1]/span/div/fieldset[1]//table[2]/tbody/tr/td[2]//tr/td[1]/input')
        M_TYPE.send_keys(Keys.ARROW_DOWN)
        M_TYPE.send_keys(Keys.ARROW_DOWN)
        M_TYPE.send_keys(Keys.ARROW_DOWN)
        M_TYPE.send_keys(Keys.ENTER)
        # 输入简称
        self.findxpath_sendkey('//*[@name="bName"]', B_NAME1)
        # 输入全称
        self.findxpath_sendkey('//*[@name="bNameFull"]', B_NAME2)
        # 选择资产三类
        self.findxpath_sendkey('//*[@name="pClass"]', P_CLASS)
        PCLASS = self.findxpath('//*[@name="pClass"]')
        PCLASS.send_keys(Keys.ARROW_DOWN)
        PCLASS.send_keys(Keys.ENTER)
