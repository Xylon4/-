# 基类封装
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # 复用浏览器，需要设置 option.debugger_address
            """
            复用浏览器基础条件：
            1.将chrome.exe所在目录放在环境变量path下；
            2.cmd执行命令 chrome --remote-debugging-port=9222  需保证9222端口没有被占用
            3.在弹出的浏览器中打开需要的页面，此处使用原因是需要扫码登录
            """
            # Options()注意选择对应的浏览器
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        else:
            # 未指定驱动器类型时，默认为chrome，若有指定，则使用指定类型
            self.driver = driver

        if self.base_url != "":
            self.driver.get(self.base_url)

    # 定义关闭浏览器方法
    def quit_driver(self):
        self.driver.quit()

    # 定义查找元素方法
    def find(self, locator, value):
        return self.driver.find_element(locator, value)

    # 定义查找多组元素方法
    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    # 定义显式等待方法
    def wait_for_click(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
