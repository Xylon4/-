from practice.selenium.page_object_2.page.main_page import MainPage


class TestContact:
    def setup(self):
        self.mainpage = MainPage()

    def teardown(self):
        self.mainpage.quit_driver()

    def test_addmember(self):
        username = "abcd_0001"
        account = "abcd_0001"
        phonenum = "13012345678"
        page = self.mainpage.goto_add_member()
        page.add_member(username, account, phonenum)
        names = page.get_member()
        print(names)
        assert username in names
