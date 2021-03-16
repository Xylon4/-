from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to


class TestDemo:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        # 输入值为中文时先定义如下两个参数 #实测没有这两个参数也能正常执行
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)
        print("用例执行开始")

    def teardown(self):
        # self.driver.quit()
        # 参数化执行用例时，为了提高执行效率，执行完一次输入后立刻点击取消，就能再次输入了
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/action_close').click()
        print("用例执行结束")
        # pass

    # 直接在用例中定义参数/yaml文件中读取参数/网上搜索到的参数都支持
    @pytest.mark.parametrize('sendkeys,type,expect_price', [
        ('阿里巴巴', 'BABA', 230),
        ('小米', '01810', 20)
    ])
    def test_search(self, sendkeys, type, expect_price):
        """
        1.打开 雪球 APP
        2.点击搜索输入框
        3.向搜索输入框里输入“阿里巴巴” or “小米”
        4.分别获取股价后进行断言
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(sendkeys)
        self.driver.find_element_by_id("com.xueqiu.android:id/name").click()
        price = float(self.driver.find_element(MobileBy.XPATH,
                                               f'//*[@text="{type}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text)
        # 判断查询到的价格是否在期望价格的10%范围内
        assert_that(price, close_to(expect_price, expect_price * 0.1))
