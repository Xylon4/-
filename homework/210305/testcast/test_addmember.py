from mainpage import MainPage


class TestAddmember:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.end()

    def test_addmemeber(self):
        self.main.goto_maillist().goto_addmember().addmember()
