import pytest
import yaml

# 读取外部文件并定义,路径中的.代表实际调用方法的文件的上一级目录
# product文件读取 指定文件内容读取格式为gb18030，并且需要设置文件编码格式为相同编码
with open("./asset.yaml", encoding='gb18030', errors='ignore') as f:
    datas = yaml.safe_load(f)['asset']
    bond = datas['bond']
    nonstandard = datas['nonstandard']


# 定义债券新增的装饰器方法
@pytest.fixture(params=bond)
def get_bond(request):
    bond = request.param
    print(f"测试数据为：{bond}")
    return bond


# 定义利率型项目新增的装饰器方法
@pytest.fixture(params=nonstandard)
def get_nonstandard(request):
    nonstandard = request.param
    print(f"测试数据为：{nonstandard}")
    return nonstandard
