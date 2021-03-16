from practice.appium.WeCom.page.basepage import BasePage
from practice.appium.WeCom.page.work_page import WorkPage


class InformationPage(BasePage):
    def goto_work_page(self):
        self.find_click("//*[@text='工作台']")
        return WorkPage(self.driver)
