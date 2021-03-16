from appium.webdriver.common.mobileby import MobileBy

from practice.appium.WeCom.page.basepage import BasePage


class SignPage(BasePage):
    def sign(self):
        self.find_click("//*[@text='外出打卡']")
        # 通过MobileBy.XPATH 的 contains用法来模糊搜索"次外出"关键字
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        self.find_click("//*[contains(@text,'次外出')]")
        # 当断言的结果为界面显示的内容时，可以直接判断元素是否存在来代替assert
        self.find("//*[@text='外出打卡成功']")
        # assert self.driver.find_element_by_xpath("//*[@text='外出打卡成功']").text == "外出打卡成功"