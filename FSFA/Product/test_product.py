# 理财估值核算系统产品端自动化测试用例
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestProduct:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.64.131:8080/xIR_J2EE")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//*[@id='txtAccount_I']").send_keys("T999999")
        self.driver.find_element_by_xpath("//*[@id='txtPwd_I']").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@id='subBtn']").click()

    def teardown(self):
        self.driver.quit()

    def test_product1(self):
        # 点击账套管理
        self.driver.find_element_by_xpath('//*[@id="navId"]/li[3]/a').click()
        # 点击产品信息定义
        self.driver.find_element_by_xpath('//*[@id="floatMenu"]/dl[2]/dd/a').click()
        # 点击新增按钮
        self.driver.find_element_by_xpath('//*[@id="addButton-1093"]').click()
        # 点击是否平行分层
        self.driver.find_element_by_xpath('//*[@id="combobox-1235-inputEl"]').click()
        self.driver.find_element_by_xpath('//*[@id="boundlist-1369-listEl"]/ul/li[2]').click()
        # 输入产品代码
        self.driver.find_element_by_xpath('//*[@id="textfield-1239-inputEl"]').send_keys("FB0331")
        # 输入产品名称
        self.driver.find_element_by_xpath('//*[@id="textfield-1241-inputEl"]').send_keys("封闭净值型产品")
        # 输入产品全称
        self.driver.find_element_by_xpath('//*[@id="textfield-1256-inputEl"]').send_keys("封闭净值型理财产品")
        # 点击产品类型选择框
        self.driver.find_element_by_xpath('//*[@id="commonCombox-1242-inputEl"]').click()
        # 选择产品类型
        self.driver.find_element_by_xpath("//*[@class='x-boundlist x-boundlist-floating x-layer x-boundlist-default x-border-box x-boundlist-above']//li[1]").click()
        # self.driver.find_element_by_xpath('//*[@id="boundlist-1794-listEl"]/ul/li[1]').click()
        # 输入管理人
        self.driver.find_element_by_xpath('//*[@id="textfield-1670-inputEl"]').send_keys("浦银理财子公司")
        # 输入托管人
        self.driver.find_element_by_xpath('//*[@id="textfield-1671-inputEl"]').send_keys("上海浦东发展银行")
        mtr_date = self.driver.find_element_by_xpath('//*[@id="datefield-1697-inputEl"]').text + 5
        self.driver.find_element_by_xpath('//*[@id="datefield-1701-inputEl"]').send_keys(mtr_date)
        self.driver.find_element_by_xpath('//*[@id="saveButton-1646-btnInnerEl"]').click()
        sleep(2)
        # 点击浮窗中的确定
        self.driver.find_element_by_xpath('//*[@id="button-1005-btnIconEl"]').click()
        # 点击返回按钮
        self.driver.find_element_by_xpath('//*[@id="backButton-1229-btnInnerEl"]').click()
        # product_type = self.driver.find_element_by_xpath('//*[@id="checkcombo-1487-labelEl"]')
        # action = TouchActions(self.driver)
        # action.scroll_from_element(product_type, 0, 10000).perform()
        self.driver.find_element_by_xpath('//*[@text="FB0331"]').click()
        self.driver.find_element_by_xpath('//*[@id="reviewButton-1098-btnInnerEl"]').click()
        self.driver.find_element_by_xpath('//*[@id="button-1006-btnIconEl"]').click()
        self.driver.find_element_by_xpath('//*[@id="button-1005-btnIconEl"]').click()
