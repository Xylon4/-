import pytest
import yaml

# 读取外部文件并定义,路径中的.代表实际调用方法的文件的上一级目录
# product文件读取
with open("./product.yaml", encoding='gb18030', errors='ignore') as f:
    datas = yaml.safe_load(f)['product']
    product = datas['product']
    product_manage = datas['product_manage']
    cash_flow = datas['cash_flow']


# 定义产品信息定义成立的装饰器方法
@pytest.fixture(params=product)
def get_product(request):
    product = request.param
    print(f"测试数据为：{product}")
    return product


# 定义账套管理新增的装饰器方法
@pytest.fixture(params=product_manage)
def get_product_manage(request):
    product_manage = request.param
    print(f"测试数据为：{product_manage}")
    yield product_manage
