import pytest
import yaml

# 读取外部文件并定义,路径中的.代表实际调用方法的文件的上一级目录,./.代表实际调用方法的文件的上两级目录
# report文件读取 指定文件内容读取格式为gb18030，并且需要设置文件编码格式为相同编码
# with open("././report.yaml", encoding='gb18030', errors='ignore') as f:
#     datas = yaml.safe_load(f)['report']
#     registry = datas['registry']
#     nonstandard = datas['nonstandard']


# 定义资产池注册表的装饰器方法
# @pytest.fixture(params=registry)
# def get_registry(request):
#     registry = request.param
#     print(f"测试数据为：{registry}")
#     return registry


Excel_basedata_zs = 'E:\PycharmProjects\菜单基础数据维护_浙商.xlsx'
Excel_basedata_nj = 'E:\PycharmProjects\菜单基础数据维护_南京.xlsx'
Excel_basedata_tj = 'E:\PycharmProjects\菜单基础数据维护_天津.xlsx'
Excel_custom = 'E:\PycharmProjects\自动化测试用例模板.xlsx'
# 获取sheet，通过Excel表格名称()获取工作表
sheet1 = '资产池注册表'
sheet2 = '产品信息表'
sheet3 = '资负信息注册(浙商)'
sheet4 = '估值表'
sheet5 = '表1-1产品募集余额统计表'
sheet6 = '表1-2产品募集兑付统计表'
sheet7 = '表1-3产品只数情况统计表'
sheet8 = '表1-5产品提前延期兑付统计表'
sheet9 = '表1-6产品到期未兑付统计表'
sheet10 = '表2-1产品资产负债统计表'
sheet11 = '表2-2贷款分行业及企业规模统计表'
sheet12 = '表2-3贷款分地区统计表'
sheet13 = '表2-4资产收益权投向分类统计表'
sheet14 = '表2-5企业债券分行业及企业规模统计表'
sheet15 = '表3-1存续产品分合同期限募集余额统计表'
sheet16 = '表3-2新发产品分合同期限募集金额统计表'
sheet17 = '表3-3资管产品资产负债剩余期限统计表'
sheet18 = '产品终止信息表'
sheet19 = '交易登记'
sheet20 = '资产要素登记'
sheet21 = '产品存续期登记'
sheet22 = '投组单元资产明细表(穿透)'
sheet23 = '投组单元资产明细表'
sheet24 = '现金流缺口表(新)'
sheet25 = '现金流明细表(新)'
sheet26 = '损益分析表'
sheet27 = '资产结构分析表'
sheet28 = '投组单元估值明细表'
sheet29 = '债券类资产(新)'
sheet30 = '产品情况月度统计表-资产'
sheet31 = '交易所债券审批'
sheet32 = '现券审批'
sheet33 = '银行间债券行权审批'
sheet34 = '同业存单审批'
sheet35 = '质押式回购审批'
sheet36 = '货币基金申购赎回审批'
sheet37 = '表内外投资业务基础资产情况表'
sheet38 = '表内外投资业务期限结构及成本收益表'
sheet39 = '表七同业交易对手情况表'
sheet40 = '活期账户提前收息'
sheet41 = '待审批任务'
sheet42 = '待复核交易指令列表'
sheet43 = '货币基金'
sheet44 = '日间分录查询'
sheet45 = '周期分录查询'
sheet46 = '损益结转分录查询'
sheet47 = '利润表(平台)'
