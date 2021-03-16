from appium.webdriver.common.mobileby import MobileBy

from practice.appium.WeCom.page.basepage import BasePage
from practice.appium.WeCom.page.sign_page import SignPage


class WorkPage(BasePage):
    def goto_sign_page(self):
        self.swip_find("打卡")
        return SignPage(self.driver)
