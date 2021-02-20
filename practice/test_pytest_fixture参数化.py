import pytest

# 装饰器的同时还可以实现参数化，return和yield都能实现参数化返回值
@pytest.fixture(params=[1, 2, 3])
def login1(request):
    data = request.param
    print("获取测试数据")
    return data

def test_case1(login1):
    print(login1)
    print("测试用例1")
