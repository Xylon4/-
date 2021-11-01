import pytest
import yaml

# 读取外部文件并定义,路径中的.代表实际调用方法的文件的上一级目录,./.代表实际调用方法的文件的上两级目录
# report文件读取 指定文件内容读取格式为gb18030，并且需要设置文件编码格式为相同编码
with open("././report.yaml", encoding='gb18030', errors='ignore') as f:
    datas = yaml.safe_load(f)['report']
    registry = datas['registry']
    nonstandard = datas['nonstandard']


# 定义资产池注册表的装饰器方法
@pytest.fixture(params=registry)
def get_registry(request):
    registry = request.param
    print(f"测试数据为：{registry}")
    return registry


Excel_basedata = 'E:\菜单基础数据维护.xlsx'
Excel_custom = 'E:\自动化读取用例.xlsx'
# 获取sheet，通过Excel表格名称(rank)获取工作表
sheet1 = '资产池注册表'
sheet2 = '产品信息表'
sheet3 = '资负信息注册(浙商)'
sheet4 = '估值表'
