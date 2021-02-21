import pytest
import yaml

from calc import Calculator


# 创建装饰器方法stageprint，用来标记用例的开始与结束
@pytest.fixture(scope="module")
def stageprint():
    print("开始计算")
    yield
    print("计算结束")


@pytest.fixture(scope='class')
def get_calc():
    print('获取计算器实例')
    calc = Calculator()
    return calc


# 从外部文件calc.yaml中读取数据，并分模块定义
with open("./calc.yaml") as f:
    datas = yaml.safe_load(f)['calc_data']
    add_datas = datas['add_datas']
    sub_datas = datas['sub_datas']
    mul_datas = datas['mul_datas']
    div_datas = datas['div_datas']
    myid = datas['myid']


# 定义加法需要的装饰器方法
@pytest.fixture(params=add_datas, ids=myid)
def get_add_datas(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data


# 定义减法需要的装饰器方法
@pytest.fixture(params=sub_datas, ids=myid)
def get_sub_datas(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data


# 定义乘法需要的装饰器方法
@pytest.fixture(params=mul_datas, ids=myid)
def get_mul_datas(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data


# 定义除法需要的装饰器方法
@pytest.fixture(params=div_datas, ids=myid)
def get_div_datas(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data
