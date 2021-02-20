"""
pytest.fixture装饰器选择性添加用法
"""

import pytest


# 定义装饰器方法login
@pytest.fixture()
def login():
    print("装饰器添加成功")
    print("获取token")
    username = "tom"
    password = "tomcat"
    token = "token03748"
    # yield 关键字可以激活fixture的teardown功能
    # yield 关键字后添加变量，和函数的返回功能return相同
    yield [username, password]  # 一举两得
    # yield后面添加输出，是在案例执行完后直接输出的方法
    print(username, password, token)
    print("注销操作")


# 需要添加装饰器的方法中传入装饰器即可
def test_case1(login):
    # 案例中调用含有yield关键字的装饰器方法，且yield后添加了变量的情况下，将会返回变量，未添加变量时返回none，这点和函数相同
    print(f"用户信息为：{login}")
    print("测试用例1")


def test_case2():
    print("测试用例2")


def test_case3(login):
    print("测试用例3")


# 直接添加装饰器的方法，在参数中传入字符串login,其中login需要提前定义为一个装饰器方法，普通的方法不能使用
@pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")


"""
yield 生成器
"""

# def provider():
#     # 循环读取数据
#     for i in range(10):
#         yield i
#
#
# # 普通函数调用
# p = provider()
# print(next(p))
