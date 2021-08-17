from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePageFsfa:
    def __init__(self, driver: WebDriver = None):
        if driver == None:
            self.start()

        else:
            # 未指定驱动器类型时，默认为chrome，若有指定，则使用指定类型
            self.driver = driver

    def start(self):
        # opt参数用来解决页面下滑动作
        opt = Options()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=opt)
        self.driver.get("http://192.168.64.131:8080/xIR_J2EE")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//*[@id='txtAccount_I']").send_keys("T999999")
        self.driver.find_element_by_xpath("//*[@id='txtPwd_I']").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@id='subBtn']").click()

    def end(self):
        self.driver.quit()

    def findxpath(self, path1):
        return self.driver.find_element_by_xpath(path1)

    def findxpath_click(self, path2):
        self.findxpath(path2).click()

    def findxpath_sendkey(self, path3, key3):
        self.findxpath(path3).send_keys(key3)

    def find(self, locator1, value1):
        return self.driver.find_element(By.XPATH, f'//*[@{locator1}="{value1}"]')

    def find_click(self, locator2, value2):
        self.find(locator2, value2).click()

    def find_sendkey(self, locator3, value3, key3):
        self.find(locator3, value3).send_keys(key3)

    # 定义显式等待方法
    def wait_for_click(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))