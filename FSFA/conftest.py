import pytest
import yaml


# 定义装饰器方法stagemark，用来标记用例的开始与结束
@pytest.fixture(scope="module")
def stagemark():
    print("自动化案例执行开始")
    yield
    print("自动化案例执行结束")


# 读取外部文件并定义,路径中的.代表根目录"FSFA"
with open("./login.yaml") as f:
    datas = yaml.safe_load(f)['login_data']
    ip = datas['ipaddr']
    fail_token = datas['fail_token']
    success_token = datas['success_token']


# 定义IP的装饰器方法
@pytest.fixture(params=ip)
def get_ip(request):
    ip = request.param
    print(f"测试数据为：{ip}")
    yield ip


# 定义错误用户密码的装饰器方法
@pytest.fixture(params=fail_token)
def get_fail_token(request):
    fail_token = request.param
    print(f"测试数据为：{fail_token}")
    yield fail_token


# 定义正确用户密码的装饰器方法
@pytest.fixture(params=success_token)
def get_success_token(request):
    success_token = request.param
    print(f"测试数据为：{success_token}")
    yield success_token


# 解决命令行执行找不到调用的包
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
