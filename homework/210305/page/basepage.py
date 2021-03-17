from time import sleep
from typing import Dict, List

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 被继承的基类中一定要有初始化driver，不然驱动无法复用和传递，每一个链式调用都会报错
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 定义查找元素的方法
    def find(self, locator):
        # return查找内容，方便其他方法调用该元素
        return self.driver.find_element_by_xpath(locator)

    # 定义查找元素并点击的方法
    def find_click(self, locator):
        self.find(locator).click()

    # 定义输入内容方法
    def imput_messages(self, locator, text):
        self.find(locator).send_keys(text)

    # 定义从上往下滑动页面后找到想要的元素并点击的方法
    def swip_find(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));').click()

    # 定义解析关键字方法
    # def parse_action(self, steps: List[Dict]):
    def parse_action(self, path, fun_name):
        with open(path, "r", encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[fun_name]
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["locator"])
            elif step["action"] == "find":
                self.find(step["locator"])
            # 使用保存并继续添加功能时，页面有0.5秒左右的卡顿，想加一个显式等待，但是没有成功（提示超时），先用强制等待完成功能
            elif step["action"] == "imput_messages":
                # element_state = (MobileBy.XPATH, 'step["locator"]')
                # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element_state))
                sleep(1)
                self.imput_messages(step["locator"], step["text"])
