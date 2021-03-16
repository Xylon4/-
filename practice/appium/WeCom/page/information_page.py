from practice.appium.WeCom.page.basepage import BasePage
from practice.appium.WeCom.page.work_page import WorkPage


class InformationPage(BasePage):
    def goto_work_page(self):
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()
        return WorkPage(self.driver)
