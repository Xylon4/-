from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # 被继承的基类中一定要有初始化driver，不然驱动无法复用和传递，每一个链式调用都会报错
    # 这两种方法都可以，不加：WebDriver也能正常执行
    # def __init__(self, driver):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 定义查找元素的方法
    def find(self, locator):
        # return查找内容，方便其他方法调用该元素
        return self.driver.find_element_by_xpath(locator)

    # 定义查找元素并点击的方法
    def find_click(self, locator):
        # 当引用其他方法时，需要注意上一个方法是否有返回值（未定义默认为None），若没有，则不能继续操作
        self.find(locator).click()
        # self.driver.find_element_by_xpath(locator).click()

    # 定义从上往下滑动页面后找到想要的元素并点击的方法
    def swip_find(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));').click()
