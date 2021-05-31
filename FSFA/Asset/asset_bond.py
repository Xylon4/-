# 理财估值核算系统资产端自动化测试用例
# 债券新增及复核
from time import sleep

from FSFA.basepage_FSFA import BasePageFsfa
from selenium.webdriver.common.keys import Keys


class AssetBond(BasePageFsfa):
    def assetbond1(self):
        I_CODE = 'bond20210528'
        B_NAME1 = '银行债20210528'
        B_NAME2 = '商业银行债20210528'
        P_CLASS = '商业银行债-直接投资'
        B_ISSUER = '国家开发银行'
        B_ISSUEDATE = '2020-03-03'
        B_STARTDATE = '2020-03-03'
        B_ENDDATE = '2023-03-03'
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
        M_TYPE = self.findxpath(
            '//div[3]//div[2]//div[2]//div[1]/span/div/fieldset[1]//table[2]/tbody/tr/td[2]//tr/td[1]/input')
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
        # 输入发行机构
        self.findxpath_sendkey('//*[@name="bIssuerCode"]', B_ISSUER)
        ISSUER = self.findxpath('//*[@name="bIssuerCode"]')
        ISSUER.send_keys(Keys.SPACE)
        ISSUER.send_keys(Keys.BACK_SPACE)
        sleep(1)
        # 选择托管场所
        self.findxpath_click('//*[@name="hostMarket"]')
        HOSTMARKET = self.findxpath('//*[@name="hostMarket"]')
        HOSTMARKET.send_keys(Keys.ARROW_DOWN)
        HOSTMARKET.send_keys(Keys.ENTER)
        # 选择清偿等级
        self.findxpath_click('//*[@name="bSeniority"]')
        LIQUIDATION_LEVEL = self.findxpath('//*[@name="bSeniority"]')
        LIQUIDATION_LEVEL.send_keys(Keys.ARROW_DOWN)
        LIQUIDATION_LEVEL.send_keys(Keys.ARROW_DOWN)
        LIQUIDATION_LEVEL.send_keys(Keys.ENTER)
        # 输入发行日期
        self.findxpath_sendkey('//*[@name="bIssueDate"]', B_ISSUEDATE)
        # 输入起息日
        self.findxpath_sendkey('//*[@name="bStartDate"]', B_STARTDATE)
        # 输入到期日
        self.findxpath_sendkey('//*[@name="bMtrDate"]', B_ENDDATE)
        # 选择计息基准
        self.findxpath_click('//*[@name="bDayCount"]')
        DAYCOUNT = self.findxpath('//*[@name="bDayCount"]')
        DAYCOUNT.send_keys(Keys.ARROW_DOWN)
        DAYCOUNT.send_keys(Keys.ARROW_DOWN)
        DAYCOUNT.send_keys(Keys.ENTER)
        # 选择计息频率
        self.findxpath_click('//*[@name="calcPeriodFreq"]')
        CALC_FREQ = self.findxpath('//*[@name="calcPeriodFreq"]')
        CALC_FREQ.send_keys(Keys.ARROW_DOWN)
        CALC_FREQ.send_keys(Keys.ENTER)
        # 选择付息频率
        self.findxpath_click('//*[@name="paymentFreq"]')
        PAY_FREQ = self.findxpath('//*[@name="paymentFreq"]')
        PAY_FREQ.send_keys(Keys.ARROW_DOWN)
        PAY_FREQ.send_keys(Keys.ENTER)
        # 输入利率
        self.findxpath_sendkey('//*[@name="textFieldCoupon"]', 6)
        # 点击保存
        self.findxpath_click('//div[3]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/a[4]/span/span/span[1]')
        # 点击确定
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        # 点击返回
        self.findxpath_click('//div[3]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/a[3]/span/span/span[1]')
        # 查看未生效列表并搜索对应债券
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/img')
        self.findxpath_sendkey('//*[@name="I_CODE"]', I_CODE)
        self.findxpath_click('//*[@name="STATUS"]')
        STATUS = self.findxpath('//*[@name="STATUS"]')
        STATUS.send_keys(Keys.ARROW_DOWN)
        STATUS.send_keys(Keys.ENTER)
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div/div[4]/div[1]/div/div/a[1]/span/span/span[1]')
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div/div[4]/div[1]/div/div/a[4]/span/span/span[2]')
        # 选中债券
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr/td[1]/div')
        # 点击复核
        self.findxpath_click('//div[3]/div[2]/div[2]//div[1]/div[1]/span/div/div[1]/div/div/a[8]/span/span/span[1]')
        # 点击确定
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        return True