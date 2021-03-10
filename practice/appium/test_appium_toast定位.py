from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast:
    def setup(self):
        desire = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.touchboarder.android.api.demos',
            'appActivity': 'com.example.android.apis.view.PopupMenu1'
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Make a Popup!']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search']").click()
        # .page_source可以打印页面信息，用来查看toast基础信息
        # print(self.driver.page_source)
        print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        # contains(@text,'Clicked popup') 通过文本中包含Clicked popup的方式定位到toast
        # print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'Clicked popup')]").text)
