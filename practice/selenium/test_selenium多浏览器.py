import os
from time import sleep
import pytest
from selenium import webdriver


class TestDemo:
    def setup(self):
        brower = os.getenv("browser")
        if brower == 'firefox':
            self.driver = webdriver.Firefox()
        elif brower == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="s-top-left"]/a[6]').click()
        sleep(3)


if __name__ == '__main__':
    pytest.main()
