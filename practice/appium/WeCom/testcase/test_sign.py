from practice.appium.WeCom.page.app import App
from practice.appium.WeCom.page.basepage import BasePage


class TestSign():
    def setup(self):
        # 案例中起始步骤需要传入封装的第一个页面（return初始页面）
        self.app = App()

    def teardown(self):
        self.app.goto_main().quit()

    def test_sign(self):
        self.app.goto_main().goto_work_page().goto_sign_page().sign()

    def test_firstsign(self):
        self.app.goto_main().goto_work_page().goto_sign_page().first_sign()
