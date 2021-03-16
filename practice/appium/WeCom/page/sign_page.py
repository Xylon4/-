from appium.webdriver.common.mobileby import MobileBy

from practice.appium.WeCom.page.basepage import BasePage


class SignPage(BasePage):
    def sign(self):
        self.driver.find_element_by_xpath("//*[@text='外出打卡']").click()
        # 通过MobileBy.XPATH 的 contains用法来模糊搜索"次外出"关键字
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        assert self.driver.find_element_by_xpath("//*[@text='外出打卡成功']").text == "外出打卡成功"