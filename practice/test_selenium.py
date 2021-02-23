import selenium
from selenium import webdriver
from time import sleep


class TestSelenium():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 隐式等待implicitly_wait,设置最大等待时间，若时间段内查找到对应元素，则立刻执行下一步
        self.driver.implicitly_wait(15)

    def teardown(self):
        self.driver.quit()

    def test_selenium(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("新闻").click()
        self.driver.find_element_by_css_selector(".home-banner-cell").click()
        # self.driver.find_element_by_xpath("//div[@id='pane-news']/div/ul/li[2]/strong/a/b").click()
