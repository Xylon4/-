import pytest

# order和数字写法都可以，且数字可以不连续，未指定时最后执行

def test_a():
    print("测试用例A")

@pytest.mark.run(order=6)
def test_b():
    print("测试用例B")

# 数字的写法
@pytest.mark.third
def test_c():
    print("测试用例C")

@pytest.mark.run(order=1)
def test_d():
    print("测试用例D")
