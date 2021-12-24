import pytest


# 定义装饰器方法stagemark，用来标记用例的开始与结束
@pytest.fixture(scope="module")
def stagemark():
    print("自动化案例执行开始")
    yield
    print("自动化案例执行结束")


# 解决命令行执行找不到调用的包
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# 浙商环境
zs_address1 = 'http://191.168.0.206:8001/xIR_J2EE/login.action'

# 南京环境
nj_address1 = 'http://172.19.6.44:8001/xIR_J2EE/login.action'

# 案例运行环境
default_address = nj_address1

# 报表列表
report_list = ['投组管理-投组单元资产明细表(穿透)',
               '投组管理-资产结构分析表',
               '投组管理-现金流明细表(新)',
               '投组管理-现金流缺口表(新)',
               '投组管理-投组单元估值明细表',
               '投组管理-投组单元资产明细表',
               '投组管理-损益分析表',
               '估值管理-估值表',
               '综合管理-产品信息表',
               '综合管理-资负信息注册(浙商)',
               '综合管理-产品终止信息表',
               '综合管理-产品存续期登记',
               '综合管理-资产要素登记',
               '综合管理-交易登记',
               '综合管理-表1-1产品募集余额统计表',
               '综合管理-表1-2产品募集兑付统计表',
               '综合管理-表1-3产品只数情况统计表',
               '综合管理-表1-5产品提前延期兑付统计表',
               '综合管理-表1-6产品到期未兑付统计表',
               '综合管理-表2-1产品资产负债统计表',
               '综合管理-表2-2贷款分行业及企业规模统计表',
               '综合管理-表2-3贷款分地区统计表',
               '综合管理-表2-4资产收益权投向分类统计表',
               '综合管理-表2-5企业债券分行业及企业规模统计表',
               '综合管理-表3-1存续产品分合同期限募集余额统计表',
               '综合管理-表3-2新发产品分合同期限募集金额统计表',
               '综合管理-表3-3资管产品资产负债剩余期限统计表',
               '综合管理-产品情况月度统计表-资产'
               ]

# 资产列表
asset_list = ['资产管理-债券类资产(新)'
              ]

# 交易列表
trade_list = ['交易管理-交易所债券审批',
              '交易管理-现券审批',
              '交易管理-银行间债券行权审批',
              '交易管理-同业存单审批'
              '交易管理-质押式回购审批'
              ]
# 产品列表
