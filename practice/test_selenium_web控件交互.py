# 鼠标左键单机 左键双击 右键单机
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        # 定义并传入option，未识别的命令会报如下错误，所以需要先定义
        # unknown command: Cannot call non W3C standard command while in W3C mode
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # @pytest.mark.skip标记需要跳过的案例
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        element_doubleclick = self.driver.find_element_by_xpath("/html/body/form/input[2]")
        element_rightclick = self.driver.find_element_by_xpath("/html/body/form/input[4]")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_doubleclick)
        action.context_click(element_rightclick)
        sleep(3)
        action.perform()

    # 鼠标移动交互
    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    # 拖拽交互
    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        # 三种写法取其一即可
        # action.drag_and_drop(drag_element, drop_element).perform()
        action.click_and_hold(drag_element).release(drop_element).perform()
        # action.click_and_hold(drag_element).move_to_element(drop_element).perform()
        sleep(3)

    # 点击输入框，输入内容，空格，删除，全选，复制，粘贴交互
    @pytest.mark.skip
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele1 = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele2 = self.driver.find_element_by_xpath("/html/body/label[2]/table/tbody/tr/td[2]/input")
        ele1.click()
        action = ActionChains(self.driver)
        # 加上.pause(1) 停顿一秒
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE)
        action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
        action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)
        # 注意.perform()一定是所有action之后执行的
        action.key_down(Keys.CONTROL, ele2).send_keys('v').key_up(Keys.CONTROL).perform()
        sleep(3)

    # 页面滚动交互
    @pytest.mark.skip
    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com/")
        # 定义搜索框
        ele3 = self.driver.find_element_by_id("kw")
        # 定义百度一下按钮
        ele4 = self.driver.find_element_by_id("su")
        # .send_keys("输入搜索内容")
        ele3.send_keys("selenium测试")
        action = TouchActions(self.driver)
        # .tap单击操作
        action.tap(ele4)
        # .scroll_from_element,从ele3元素开始，X轴偏移0，Y轴偏移10000，视觉效果就是滑到页面底端，实际可以定位到页面的任意位置
        action.scroll_from_element(ele3, 0, 10000).perform()

    # 表单的操作，输入用户密码，勾选记住密码，点击登录
    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("xylona")
        self.driver.find_element_by_id("user_password").send_keys("qilong555")
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[3]/div/label').click()
        # 表单的勾选框控件不一定支持点击，这时候可以退而求其次点击对应的文本来实现同样的效果
        # self.driver.find_element_by_id("user_remember_me").click()
        # 当引用的内容中包含了单双引号/大中小括号等成对出现的符号时，需要使用不同的符号来避免异常
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
        sleep(3)
