# import pytest
#
# # fixture作用域定义scope
# @pytest.fixture(scope="class")
# def connectDB():
#     print("连接数据库操作")
#     yield
#     print("断开数据库连接")


class TestDemo:

    # fixture作用域需要在所有的方法传入才能生效，未传入会跳过，不传入的话需要使用autouse=True
    def test_a(self, connectDB):
        print("测试用例a")

    def test_b(self, connectDB):
        print("测试用例b")
