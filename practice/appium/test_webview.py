# 测试混合应用中的web页面
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebview:
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'appPackage': 'com.xueqiu.android',
            'appActivity': 'com.xueqiu.android.common.MainActivity',
            'noReset': True,
            'deviceName': 'emulator-5554',
            'chromedriverExecutable': 'C:\Program Files\Appium/\/resources/\/app/\/node_modules/\/appium/\/node_modules/\/appium-chromedriver\chromedriver\win\chromedriver_52.0.2743'
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass
        # self.driver.quit()

    def test_webview(self):
        self.driver.find_element_by_xpath("//*[@text='交易']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@content-desc='A股开户']").click()
        # 进入webview页面，需要切换窗口
        switch_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(switch_window)

        # 设置显式等待，等待页面加载完再操作
        phone_num = (By.XPATH, "//*[@resource-id='phone-number']")
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(phone_num))
        self.driver.find_element_by_xpath("//*[@resource-id='phone-number']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='phone-number']").send_keys("13012345678")
        self.driver.find_element_by_xpath("//*[@content-desc='获取验证码']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='code']").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@content-desc='立即开户']").click()
        sleep(5)
