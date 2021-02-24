import selenium
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


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
        # 点击新闻后会形成页面跳转，后续的操作在新页面上完成，现在的知识还不足以写出来，先搁置
        self.driver.find_element_by_link_text("新闻").click()
        # 通过XPATH定位法定位到的元素，因为两个a元素是并行的，并且a下面都有b,所以用//a/b[1]定位不到想要的元素
        self.driver.find_element(By.XPATH, '// *[ @ id = "pane-news"] // a[1] / b').click()
        # 通过console拷贝出来的全路径，当你自己通过语句查不到想到的元素时，可以用这个方法，且定位的最精准，但就不是那么高阶了
        # self.driver.find_element(By.XPATH, '//*[@id="pane-news"]/div/ul/li[2]/strong/a[1]/b').click()

