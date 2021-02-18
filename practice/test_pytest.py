import pytest


def func(x):
    return x + 1


# pytest参数化
@pytest.mark.parametrize('a,b', [
    (1, 2),
    (10, 20),
    ('a', 'a1'),
    (3, 4),
    (5, 6)
])
def test_answer(a, b):
    assert func(a) == b


# 选择性增加登录信息功能 fixture装饰器
@pytest.fixture()
def login():
    print("登录操作")
    username = "xylona"
    return username


class TestDemo:
    def test_a(self, login):
        print(f"{login}\'s demo1")

    def test_b(self, login):
        print("demo2")

    # 错误命名示范，不执行c
    def c(self):
        print("demo3")


# 加了如下入口语句后，才能用python来执行，不然只能用pytest，同时指定class和-v展示详细信息
if __name__ == '__main__':
    pytest.main(['test_pytest.py::TestDemo', '-v'])
