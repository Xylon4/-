# 因为目录下有很多main_page,且其他几个是常用项，导致选中MainPage一直无法关联出我需要的import选项
# 右键选中page文件夹，点击Mark Directory as,再选择Sources Root;能刷新备选项，重新定位到离本文件最近的main_page

from main_page import *


class TestCase:
    def setup(self):
        print("欢迎来到召唤师峡谷")

    def teardown(self):
        # self.mainpage1.quit_driver()
        print("我好了，你呢")

    def test_addmember1(self):
        self.mainpage1 = MainPage1()
        username = "赵信"
        alias = "zhaoxin"
        account = "zhaoxin"
        phonenum = "13031141132"
        post = "工程师"
        page = self.mainpage1.goto_add_member1()
        page.add_member(username, alias, account, phonenum, post)
        names = page.get_member()
        assert username in names

    def test_addmember2(self):
        self.mainpage2 = MainPage2()
        username = "嘉文四世"
        alias = "jiawensishi"
        account = "jiawensishi"
        phonenum = "13022212332"
        post = "开发经理"
        page = self.mainpage2.goto_add_member2()
        page.add_member(username, alias, account, phonenum, post)
        names = page.get_member()
        assert username in names
