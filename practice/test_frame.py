# 切换及定位窗口操作
import pytest
from selenium import webdriver
from time import sleep


class TestSwitch:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_switch(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        # 点击立即注册后出现两个页面，定义变量来获取窗口属性,此时的属性是一个列表，列表内有两个值
        windows = self.driver.window_handles
        # 切换窗口.switch_to.window()
        self.driver.switch_to.window(windows[1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("123456")
        sleep(3)
        # 切换回原目录
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("login_username")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("login_password")
        sleep(2)
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # .switch_to.frame("需要切换的frameID")切换到新的frame下
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        # 返回原frame，两种写法
        self.driver.switch_to.parent_frame()
        # self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
