# 理财估值核算系统资产端自动化测试用例
# 利率型项目资产新增及复核
from time import sleep

from selenium.webdriver import ActionChains

from FSFA.basepage_FSFA import BasePageFsfa
from selenium.webdriver.common.keys import Keys


class AssetNonstandard(BasePageFsfa):
    def assetnonstandard1(self):
        I_CODE = 'LBS20210601'
        I_NAME = '利率型资产20210601'
        P_CLASS = '北金所债权融资计划'
        MTR_DATE = '2021-03-03'
        LBS_RATE = '6'
        CP = '100000000'
        # 点击资产管理
        self.findxpath_click('//*[@id="navId"]/li[4]/a')
        # 点击利率型项目资产
        self.findxpath_click('//*[@id="floatMenu"]/dl[1]/dd[2]/a')
        # 点击新增
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div/div[1]/span/div/div[1]/div/div/a[2]/span/span/span[1]')
        # 输入资产代码
        self.findxpath_sendkey('//*[@name="assetLBSInfoSub.i_code"]', I_CODE)
        # 输入资产名称
        self.findxpath_sendkey('//*[@name="assetLBSInfoSub.i_name"]', I_NAME)
        # 选择核算大类
        self.findxpath_click('//*[@name="assetLBSInfoSub.pClassAct"]')
        # 需要补一个显式等待
        self.findxpath_click('/html/body/div/div/ul/li[8]')
        # PCALSS_ACT = self.findxpath('//*[@name="assetLBSInfoSub.pClassAct"]')
        # 因为北金所债权融资计划在选项的最后，想通过方向键上来选中，但是并未生效，所有的上键均未生效
        # PCALSS_ACT.send_keys(Keys.ARROW_UP)
        # 多次重复操作时，有概率导致动作未生效，需要按八次下，实际只按了六次，故舍弃键盘动作
        # PCALSS_ACT.send_keys(Keys.ARROW_DOWN)
        # PCALSS_ACT.send_keys(Keys.ARROW_DOWN)
        # PCALSS_ACT.send_keys(Keys.ARROW_DOWN)
        # PCALSS_ACT.send_keys(Keys.ARROW_DOWN)
        # PCALSS_ACT.send_keys(Keys.ARROW_DOWN)
        # PCALSS_ACT.send_keys(Keys.ARROW_DOWN)
        # PCALSS_ACT.send_keys(Keys.ARROW_DOWN)
        # PCALSS_ACT.send_keys(Keys.ARROW_DOWN)
        # PCALSS_ACT.send_keys(Keys.ENTER)
        # sleep(1)
        # 选择资产三类
        self.findxpath_sendkey('//fieldset[1]//div[1]/span/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td[1]/input', P_CLASS)
        sleep(1)
        self.findxpath_click('//div[2]/div/table/tbody/tr[3]/td/div/span')
        sleep(1)
        # 输入到期日
        self.findxpath_sendkey('//*[@name="fixedInstrumentSub.mtr_date"]', MTR_DATE)
        # 点击利率调整
        self.findxpath_click('//fieldset[2]/div/span/div/div[2]/span/div/table[4]/tbody/tr/td[2]/div/div/div/a/span/span/span[1]')
        # 输入利率:双击输入框→输入利率
        rate = self.findxpath('//div[3]/span/div/div/div[2]/div/table/tbody/tr/td[3]/div')
        action = ActionChains(self.driver)
        action.double_click(rate)
        action.perform()
        self.findxpath_sendkey('//*[@name="volume"]', LBS_RATE)
        self.findxpath_click('//div[3]/span/div/div/div[1]/div[2]/span/div/a[1]/span/span/span[2]')
        self.findxpath_click('/html/body/div[last()-1]/div[1]/div/div/div/div[2]/img')
        # 输入初始本金
        self.findxpath_sendkey('//*[@name="fixedInstrumentSub.amount"]', CP)
        # 点击保存
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div[2]/div[2]/div/div/a[1]/span/span/span[1]')
        # 点击确定
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        # 点击返回
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div[2]/div[2]/div/div/a[3]/span/span/span[1]')
        # 切换未生效列表
        self.findxpath_click('//*[@name="isEffctive"]')
        ISEFFCTIVE = self.findxpath('//*[@name="isEffctive"]')
        ISEFFCTIVE.send_keys(Keys.ARROW_DOWN)
        ISEFFCTIVE.send_keys(Keys.ENTER)
        # 查询对应代码
        self.findxpath_sendkey('//div[3]/div[2]/div[2]/div/div[1]/div[1]//div[2]//table[2]//tr/td[2]//tr/td[1]/input', I_CODE)
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div[1]/div[1]//div[3]/div/div/a[1]/span/span/span[1]')
        # 选中对应资产
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/table/tbody/tr/td[1]/div/div')
        # self.findxpath_click('//div[3]/div[2]/div[2]/div/div[1]/div[2]//div[1]/div[2]/div/table/tbody/tr/td[2]/div')
        # 点击复核按钮
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div[1]/div[1]//div[1]/div/div/a[7]/span/span/span[1]')
        # 点击确定
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        return True