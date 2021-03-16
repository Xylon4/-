from appium import webdriver

from practice.appium.WeCom.page.information_page import InformationPage


class App:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        # 两种capability设置方法均可，要注意字符和bool值不同的书写格式，引号，大小写经常需要查半天
        cap = {}
        cap['platformName'] = 'Android'
        cap['platformVersion'] = '6.0'
        cap['deviceName'] = 'emulator-5554'
        cap['appPackage'] = 'com.tencent.wework'
        cap['appActivity'] = '.launch.WwMainActivity'
        cap['noReset'] = 'true'
        cap['settings[waitForIdleTimeout]'] = 0
        # cap = {
        #     'platformName': 'Android',
        #     'platformVersion': '6.0',
        #     'deviceName': 'emulator-5554',
        #     'appPackage': 'com.tencent.wework',
        #     'appActivity': '.launch.WwMainActivity',
        #     # 不清空缓存启动app
        #     'noReset': True,
        #     # 设置等待页面空间状态的时间为0s
        #     'settings[waitForIdleTimeout]': 0
        # }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)
        self.driver.implicitly_wait(20)

    def goto_main(self):
        return InformationPage(self.driver)
