# 理财估值核算系统登录页面自动化测试用例
from time import sleep

from selenium import webdriver


class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.64.131:8080/xIR_J2EE')
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_login1(self, stagemark):
        self.driver.find_element_by_xpath("//*[@id='subBtn']").click()
        message1 = self.driver.find_element_by_xpath('//*[@id="ASPxLabel_Message"]').text
        assert message1 == "请输入用户名"

    def test_login2(self, get_fail_token, stagemark):
        self.driver.find_element_by_xpath("//*[@id='txtAccount_I']").send_keys(get_fail_token[0])
        self.driver.find_element_by_xpath("//*[@id='txtPwd_I']").send_keys(get_fail_token[1])
        self.driver.find_element_by_xpath("//*[@id='subBtn']").click()
        message2 = self.driver.find_element_by_xpath('//*[@id="ASPxLabel_Message"]').get_attribute('textContent')
        assert message2 == "用户名或密码错误"

    def test_login3(self, get_success_token, stagemark):
        self.driver.find_element_by_xpath("//*[@id='txtAccount_I']").send_keys(get_success_token[0])
        self.driver.find_element_by_xpath("//*[@id='txtPwd_I']").send_keys(get_success_token[1])
        self.driver.find_element_by_xpath("//*[@id='subBtn']").click()
        bussiness_date = self.driver.find_element_by_xpath('//*[@id="switchBox"]/h2').text
        assert bussiness_date == "菜单"
