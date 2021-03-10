# 常见的ID和xpath定位，安卓实用工具 uiautomatorviewer 方便快捷定位元素
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        # 输入值为中文时先定义如下两个参数 #实测没有这两个参数也能正常执行
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # 若没有quit()方法，容易引起案例执行之间资源未释放导致报错：Original error: Could not proxy command to remote server. Original error: Error: socket hang up
        self.driver.quit()
        # pass

    # @pytest.mark.skip
    def test_search(self):
        print("搜索测试用例")
        """
        1.打开 雪球 APP
        2.点击搜索输入框
        3.向搜索输入框里输入“阿里巴巴”
        4.在搜索结果里面选择“阿里巴巴”，然后进行点击
        5.获取阿里巴巴的估价，并判断 这只股价>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/stock_current_price").text)
        current_name = self.driver.find_element_by_id("com.xueqiu.android:id/stock_current_price")
        # 元素层面可以使用.get_attribute("属性")来获取属性值，和uiautomatorviewer中看到的相同
        print(current_name.get_attribute("text"))
        # print(current_price)
        assert current_price > 200

    # @pytest.mark.skip
    def test_attr(self):
        """
        打开雪球应用首页
        定位首页的搜索框
        判断搜索框是否可用，并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和她得宽高
        向搜索框输入：alibaba
        判断【阿里巴巴】是否可见
        如果可见，打印“搜索成功”，如果不可见，打印“搜索失败”
        """
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enable = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enable == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # 获取元素是否可见的两种写法
            # if alibaba_element.is_displayed() == "true":
            if alibaba_element.get_attribute("displayed") == "true":
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        action = TouchAction(self.driver)
        # get_window_rect获取坐标值
        window_rect = self.driver.get_window_rect()
        # 定义窗口宽和高的变量
        width = window_rect['width']
        height = window_rect['height']
        # 定义窗口中间点的宽度
        # 通过相对位置来定位，方便不同的设备之间的案例通用
        x1 = int(width / 2)
        # 定义上下滑动的起始点和终止点高度
        # 手机显示往下浏览时手势是上滑，所以y_end要高于y_start
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        # .press点击初始点  .move_to移动到目标点
        # action操作顺序为 点击 等待 移动
        # 手势操作的方法相同，.press后.move_to多个点，并在每步操作之间添加等待即可
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

    def test_get_current(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        # 高级定位技巧：通过不同层级的数据定位
        # /.. 当前定位text=09988的位置开始，选择它的父节点   连跳三层父节点后//* 向下选择所有元素 最后通过resource-id精确匹配
        current_price = self.driver.find_element_by_xpath(
            "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"当前09988 对应的股价价格是：{current_price}")
        # 界面上观察到的结果是大于200的，所以断言结果为True
        assert float(current_price) > 200

    # uiautomator定位
    def test_myinfo(self):
        # 单属性查找
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("热门")').click()
        # 多属性查找
        # new UiSelector()后面可以跟多个关键字.resourceId() .text() .class()等
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        sleep(1)
        # 跨节点查找
        # 通过父节点来查找子节点，常规查找后跟 .childSelector(关键字())
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/root").childSelector(text("沪深"))').click()
        sleep(1)
        # 后退一步
        self.driver.back()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("雪球")').click()
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("推荐")').click()
        # 滚动查找：首页没有的情况下，先滚动页面，再往下查找
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("阿里巴巴(BABA)").instance(0));').click()
        sleep(5)

    # 显式等待
    def test_wait(self):
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="行情"]').click()
        # 定义显式等待指定元素 locator返回的是定位方法和对应的值
        # locator需要定义一个元祖，而不是某一个元素，所以要用 By.ID的方法，外面还要加()
        # 错误方式： (self.driver.find_element_by_id("com.xueqiu.android:id/tv_two"))
        locator = (By.ID, "com.xueqiu.android:id/tv_two")
        # locator = (self.driver.find_element_by_id("com.xueqiu.android:id/tv_two"))
        # 定义显式等待方法,10秒内指定元素能被点击则通过
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_two").click()
        self.driver.find_element_by_xpath("//*[@text='关注榜']").click()
        rankprice = self.driver.find_element_by_xpath(
            '//*[@resource-id="com.xueqiu.android:id/item_rank" and @text="NO.8"]/../..//*[@resource-id="com.xueqiu.android:id/item_name"]').text
        assert rankprice == "特斯拉"
