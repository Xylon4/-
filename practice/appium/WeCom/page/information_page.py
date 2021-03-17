from practice.appium.WeCom.page.basepage import BasePage
from practice.appium.WeCom.page.work_page import WorkPage


class InformationPage(BasePage):
    def goto_work_page(self):
        # self.find_click("//*[@text='工作台']")
        # 绝对路径为D:\PycharmProjects\-\practice\appium\WeCom\page\information_page.yaml  因为\a无法解析需要添加\转译
        self.parse_action("D:\PycharmProjects\-\practice/\/appium\WeCom\page\information_page.yaml", "goto_workpage")
        return WorkPage(self.driver)
