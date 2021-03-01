from practice.selenium.page.main import Main


class TestRegister:
    def setup(self):
        # self.main = Main()之后即可使用Main()下的方法
        self.main = Main()
        self.main.setup()

    def teardown(self):
        # 两种调用方法，效果相同
        # self.main = Main()之后即可使用Main()下的方法，并且Main继承了BasePage，所以通过Main调用._driver
        # self.main._driver.quit()
        # 使用Main()下面的teardown方法
        self.main.teardown()

    def test_register(self):
        # 连环调用：Main()→goto_register→Register()→register→Ture，断言=True，通过案例，和直接写assert True 效果相同
        assert self.main.goto_register().register()
        # assert True
