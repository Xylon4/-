from time import sleep

import pytest
from selenium import webdriver


class TestJs:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        # 通过执行JS的方式定义element=百度一下按钮
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        sleep(1)
        # 执行JS代码中的下滑命令document.documentElement.scrollTop=10000
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(2)
        # 点击下一页
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(2)
        # document.title JSON.stringify(performance.timing) 均为JS代码，html前台可以执行
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        # 通过执行JS来做两步操作：1.获取出发日期的输入框 2.去除输入框的readonly属性，使它能够被修改
        time_element = "document.getElementById('train_date').removeAttribute('readonly')"
        sleep(3)
        self.driver.execute_script(time_element)
        sleep(3)
        self.driver.execute_script("document.getElementById('train_date').value='2021-03-01'")
        sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
