from appium.webdriver.common.mobileby import MobileBy

from practice.appium.WeCom.page.basepage import BasePage
from practice.appium.WeCom.page.sign_page import SignPage


class WorkPage(BasePage):
    def goto_sign_page(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("打卡").instance(0));').click()
        return SignPage(self.driver)
