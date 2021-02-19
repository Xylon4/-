import pytest
import allure


# 对测试类标注feature
@allure.feature("登录")
class TestLogin():
    # 对方法进行标注story
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录：测试用例，登录成功")
        pass

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("登陆失败")
    def test_login_success_a(self):
        print("这是登录：测试用例，登陆失败")
        pass

    # allure.serverity添加执行级别，未添加的默认为normal
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("用户名缺失")
    def test_login_success_b(self):
        print("用户名缺失")
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("密码缺失")
    def test_login_failure(self):
        # 对步骤进行标注step
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录之后登录失败"):
            assert '1' == 1
            print("登陆失败")

        pass

    @allure.story("登录失败")
    def test_login_failure_a(self):
        print("这是登录：测试用例，登录失败")
        pass

    # allure.link添加链接
    @allure.link("http://www.baidu.com", name="这是一个链接")
    def test_with_link(self):
        print("这是一条加了链接的测试用例")
        pass

    # allure.testcase添加用例
    TEST_CASE_LINK = 'https://github.com/Xylon4/-/tree/master/practice'

    @allure.testcase(TEST_CASE_LINK, '这是一个测试用例')
    def test_with_testcase_link(self):
        print("这是一条测试用例的链接，链接到测试用例地址")
        pass

    # allure.issue添加bug链接
    # --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
    # 需要在pytest执行用例的时候加上这一行数据，{}会自动填上allure/issue里输入的编号
    @allure.issue('1', '这是一个issue')
    def test_with_issue_link(self):
        pass

    # allure.attach添加附件，附件内容可以是text，html,图片等
    def test_attach_text(self):
        allure.attach("这是一个文本", attachment_type=allure.attachment_type.TEXT)

    def test_accach_html(self):
        allure.attach("<body>这是一段htmlbody块</body>", "html测试块",attachment_type=allure.attachment_type.HTML)

    def test_accach_photo(self):
        allure.attach.file("F:\文档\真实伤害亚索壁纸.jpg",name="这是一张图片",attachment_type=allure.attachment_type.JPG)
