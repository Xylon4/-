# 每次启动模拟器和appium后，在terminal执行连接命令
# adb connect 127.0.0.1:7555
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['abd'] = 'com.android.settings.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.quit()