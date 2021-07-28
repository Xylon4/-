import pytest
import yaml

# 读取外部文件并定义,路径中的.代表实际调用方法的文件的上一级目录
# login文件读取
with open("./login.yaml") as f:
    datas = yaml.safe_load(f)['login_data']
    ipaddr = datas['ipaddr']
    fail_token = datas['fail_token']
    success_token = datas['success_token']


# 定义IP的装饰器方法
@pytest.fixture(params=ipaddr)
def get_ip(request):
    ip = request.param
    print(f"测试数据为：{ip}")
    yield ip


@pytest.fixture(scope="module")
def ip_manager():
    test = 'http://192.168.64.131:8080/xIR_J2EE'
    dev = 'http://192.168.0.5:8080/xIR_J2EE'
    local = 'http://127.0.0.1:8080/xIR_J2EE'
    return test


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
