import pytest


# 创建装饰器方法stagemark，用来标记用例的开始与结束
@pytest.fixture(scope="module")
def stagemark():
    print("自动化案例执行开始")
    yield
    print("自动化案例执行结束")
