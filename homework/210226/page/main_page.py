# 企业微信的主页，定义一个点击“添加成员”按钮的方法，用以测试用例中调用
# 观察页面，有两种方式，首页下面的添加成员和通讯录下的添加成员，这两个入口都会跳转到AddMemberPage
from selenium.webdriver.common.by import By
from add_member_page import AddMemberPage
from base_page import BasePage


class MainPage1(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # 第一种方法是通过首页点击
    def goto_add_member1(self):
        # 点击首页的添加成员按钮
        # 保证能获取到元素的情况下做点击操作
        locator = (By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)")
        self.wait_for_click(10, locator)
        # XPATH使用绝对路径更精确，但复杂页面花费时间长，CSS_SELECTOR效率更高
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        # 封装原则 reture到下层页面
        return AddMemberPage(self.driver)


class MainPage2(BasePage):
    # 第二种方法是通过通讯录页点击
    # 一个类下面两次对一个变量赋值，它会取最新的，所以需要两个类，把base_url分开定义
    base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def goto_add_member2(self):
        # 两个方法之间需要刷新浏览器地址，显式等待能保证后执行的方法能正常的获取元素
        locator = (By.XPATH, '//*[@id="main"]//div[3]/div[1]/a[1]')
        self.wait_for_click(10, locator)
        # 这个元素用CSS_SELECTOR定位出多条，所以使用XPATH
        self.find(By.XPATH, '//*[@id="main"]//div[3]/div[1]/a[1]').click()
        return AddMemberPage(self.driver)
