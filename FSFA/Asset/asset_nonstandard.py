# 理财估值核算系统资产端自动化测试用例
# 利率型项目资产新增及复核
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from FSFA.basepage_FSFA import BasePageFsfa
from selenium.webdriver.common.keys import Keys


class AssetNonstandard(BasePageFsfa):
    def assetnonstandard1(self, get_nonstandard):
        I_CODE = get_nonstandard[0]
        I_NAME = get_nonstandard[1]
        P_CLASS = get_nonstandard[2]
        MTR_DATE = get_nonstandard[3]
        LBS_RATE = get_nonstandard[4]
        CP = get_nonstandard[5]
        # 点击资产管理
        self.findxpath_click('//*[@id="navId"]/li[4]/a')
        # 点击利率型项目资产
        self.findxpath_click('//*[@id="floatMenu"]/dl[1]/dd[2]/a')
        sleep(1)
        # 点击新增
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div/div[1]/span/div/div[1]/div/div/a[2]/span/span/span[1]')
        # 输入资产代码
        self.findxpath_sendkey('//*[@name="assetLBSInfoSub.i_code"]', I_CODE)
        # 输入资产名称
        self.findxpath_sendkey('//*[@name="assetLBSInfoSub.i_name"]', I_NAME)
        # 选择资产三类
        self.findxpath_sendkey('//fieldset[1]//div[1]/span/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td[1]/input', P_CLASS)
        sleep(1)
        self.findxpath_click('//div[2]/div/table/tbody/tr[3]/td/div/span')
        sleep(1)
        # 选择核算大类
        # 该输入框有aria-invalid="false" 属性，会导致display= none，引起元素不可选中，提示报错：ElementNotVisibleException
        # self.findxpath_click('//*[@name="assetLBSInfoSub.pClassAct"]')
        self.findxpath_click('//fieldset[1]//div[1]/span/div/table[21]/tbody/tr/td[2]/table/tbody/tr/td[2]/div')
        # sleep(1)
        # 点击核算大类弹窗显示有延迟，添加显式等待
        # locator = (By.XPATH, '/html/body/div/div/ul/li[8]')
        # WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
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
        searchlib = self.findxpath('//div[3]/div[2]/div[2]/div/div[1]/div[1]//div[2]//table[2]//tr/td[2]//tr/td[1]/input')
        searchlib.send_keys(Keys.ARROW_DOWN)
        searchlib.send_keys(Keys.ENTER)
        # 输入代码后有一个下拉选择的列表，当列表遮挡下一步的按钮时，操作将会被拦截并提示错误：ElementClickInterceptedException
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div[1]/div[1]//div[3]/div/div/a[1]/span/span/span[1]')
        sleep(1)
        # 选中对应资产
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/table/tbody/tr/td[1]/div/div')
        # self.findxpath_click('//div[3]/div[2]/div[2]/div/div[1]/div[2]//div[1]/div[2]/div/table/tbody/tr/td[2]/div')
        # 点击复核按钮
        self.findxpath_click('//div[3]/div[2]/div[2]/div/div[1]/div[1]//div[1]/div/div/a[7]/span/span/span[1]')
        # 点击确定
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        return True