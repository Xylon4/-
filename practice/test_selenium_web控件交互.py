# 鼠标左键单机 左键双击 右键单机
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_case_click(self):
        element_click = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        element_doubleclick = self.driver.find_element_by_xpath("/html/body/form/input[2]")
        element_rightclick = self.driver.find_element_by_xpath("/html/body/form/input[4]")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_doubleclick)
        action.context_click(element_rightclick)
        sleep(3)
        action.perform()
