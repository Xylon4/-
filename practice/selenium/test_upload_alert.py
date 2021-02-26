from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains


class TestUpload:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # .send_keys文件上传
    @pytest.mark.skip
    def test_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id("uploadImg").send_keys("E:\ 2.jpg")
        sleep(3)

    # 弹框
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        sleep(2)
        print("点击 alert 确认")
        # .switch_to.alert切换到弹窗 .accept()执行点击确认操作
        self.driver.switch_to.alert.accept()
        # 切换回原始界面
        self.driver.switch_to.default_content()
        # 点击"点击运行"按钮
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)
