# 添加成员页面
from selenium.webdriver.common.by import By

from base_page import BasePage


class AddMemberPage(BasePage):
    def add_member(self, username, alias, account, phonenum, post):
        # 输入用户名
        self.find(By.ID, "username").send_keys(username)
        # 输入别名
        self.find(By.ID, "memberAdd_english_name").send_keys(alias)
        # 输入账号
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        # 输入手机号
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        # 输入职务
        self.find(By.ID, "memberAdd_title").send_keys(post)
        # 点击保存按钮
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return True

    def get_member(self):
        # 调用继承的显式等待方法，设置超时时间10秒,10秒内可点即不报错
        locator = (By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")
        self.wait_for_click(10, locator)
        # 查找元素
        element_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        names = []
        for ele in element_list:
            names.append(ele.get_attribute("title"))

        return names