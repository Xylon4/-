from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, contains_string, equal_to, close_to


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

        ele_toast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        # hamcrest下的assert_that断言方法  contains_string、equal_to、close_to包含方法
        # 判断ele_toast.text中是否包含字符串"menu"
        assert_that(ele_toast.text, contains_string("menu"))
        # 判断9是否等于9
        assert_that(9, equal_to(9), '这是一个提示')
        # 判断9.9是否在10的上下浮动0.2的范围内
        assert_that(9.9, close_to(10, 0.2))
        # 可添加多个断言，需要全部结果为True，最终才会PASSED
