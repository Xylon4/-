# 公用conftest.py 文件，名字不能修改，相同的包（package）下所有调用fixture方法的文件都能生效
# 一级目录和二级目录同时拥有conftest.py文件时，离得近的生效，同时文件内又定义了一遍相同名字的装饰器方法，则文件内的生效
import pytest
from calc import Calculator


# fixture作用域定义scope
@pytest.fixture(scope="class")
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库连接")


@pytest.fixture(scope='class')
def get_calc():
    print('获取计算器实例')
    calc = Calculator()
    return calc
