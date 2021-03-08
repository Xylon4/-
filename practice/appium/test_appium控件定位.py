# 常见的ID和xpath定位，安卓实用工具uiautomatorviewer 方便快捷定位元素
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


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
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    @pytest.mark.skip
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
        # print(current_price)
        assert current_price > 200

    @pytest.mark.skip
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
