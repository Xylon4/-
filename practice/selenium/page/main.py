from selenium.webdriver.common.by import By

from practice.selenium.page.base_page import BasePage
from practice.selenium.page.login import Login
from practice.selenium.page.register import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    # setup和teardown可以定义在Main()中，也可以定义在BasePage()，或者执行的案例中自己写
    def setup(self):
        self._driver.maximize_window()
        self._driver.implicitly_wait(5)

    def teardown(self):
        self._driver.quit()

    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Login(self._driver)
