# appium的session功能，录制模拟操作后导出代码，修正后可以作为用例执行
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# "noReset": True 是否重置测试环境，默认为false
# "dontStopAppOnReset": True保留之前的app状态，如果案例执行到某一步结束，同时影响了下一步操作时，需要用命令跳转比如driver.back()返回
# "skipDeviceInitialization": True 跳过安装，权限设置等操作，提高执行效率
desire_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "noReset": True,
    "dontStopAppOnReset": True,
    "skipDeviceInitialization": True
}

# 4723是appium的端口号
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
driver.implicitly_wait(10)

el1 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[2]")
el1.click()
el2 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[3]/android.widget.ImageView")
el2.click()
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[3]/android.widget.ImageView")
el3.click()
el4 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[4]/android.widget.ImageView")
el4.click()
el5 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[4]/android.widget.ImageView")
el5.click()
el6 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[1]/android.widget.ImageView")
el6.click()
el7 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el7.click()
el8 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el8.send_keys("华为")
el8.click()
el9 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
el9.click()
el10 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView")
el10.click()
TouchAction(driver).press(x=385, y=798).move_to(x=385, y=323).release().perform()
