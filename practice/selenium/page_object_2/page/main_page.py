# 企业微信的主页面
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from practice.selenium.page_object_2.page.add_member_page import AddMemberPage
from practice.selenium.page_object_2.page.base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        '''
        添加成员
        :return:
        '''
        # click add member
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        # return AddMemberPage()
        return AddMemberPage(self.driver)
