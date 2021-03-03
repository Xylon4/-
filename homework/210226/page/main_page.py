# 企业微信的主页，定义一个点击“添加成员”按钮的方法，用以测试用例中调用
# 观察页面，有两种方式，首页下面的添加成员和通讯录下的添加成员，这两个入口都会跳转到AddMemberPage
from selenium.webdriver.common.by import By

from base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        # 点击首页的添加成员按钮
        # XPATH使用绝对路径更精确，但复杂页面花费时间长，CSS_SELEECTOR效率更高
        self.find(By.CSS_SELECTOR,
                  "#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt.js_service_list > a:nth-child(1)").click()
        # 封装原则 reture到下层页面
        return AddMemberPage(self.driver)
