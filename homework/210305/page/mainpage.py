from appium import webdriver
from maillist import MailList


class MainPage:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        cap = {}
        cap['platformName'] = 'Android'
        cap['platformVersion'] = '6.0'
        cap['deviceName'] = 'emulator-5554'
        cap['appPackage'] = 'com.tencent.wework'
        cap['appActivity'] = '.launch.WwMainActivity'
        cap['noReset'] = 'true'
        cap['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)
        self.driver.implicitly_wait(20)

    def end(self):
        self.driver.quit()

    def goto_maillist(self):
        return MailList(self.driver)
