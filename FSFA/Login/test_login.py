# 产品系统登录页面自动化测试用例
from time import sleep

from selenium import webdriver


class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.64.131:8080/xIR_J2EE")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.find_element_by_xpath("//*[@id='txtAccount_I']").send_keys("T999999")
        self.driver.find_element_by_xpath("//*[@id='txtPwd_I']").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@id='subBtn']").click()
        sleep(5)
        bussiness_date = self.driver.find_element_by_xpath('//*[@id="switchBox"]/h2').text
        assert bussiness_date == "菜单"
