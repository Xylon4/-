from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ceshiren.com/')
        self.driver.maximize_window()
        # implicitly_wait 隐式等待三秒，适用于全局
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        # 元素中ID和NAME虽然是唯一的，但是不排除每一次刷新页面后，或者点击某些元素后，发生变更的情况，所以要根据情况选择每次操作都不变的元素来定位
        self.driver.find_element(By.XPATH, '//*[@id="ember41"]').click()

        # WebDriverWait 显式等待,先定义一个方法wait,并且方法会返回一个判断，WebDriverWait定义等待10秒，直到wait方法通过时，才执行下一步操作，不然就报错
        def wait(x):
            # 返回判断，寻找大于等于一的路径数据（至少一个搜索项）
            return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1

        WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
