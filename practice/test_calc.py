import pytest
import yaml

with open("./calc.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)


@pytest.fixture(params=add_datas, ids=myid)
def get_datas(request):
    print("开始计算")
    data = request.param
    print(f"测试数据为：{data}")
    yield data
    print("结束计算")


# 注意：测试类里一定不要加__init__()方法
class TestCalc:
    # def setup_class(self):
    #     print("开始计算")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("计算结束")
    """
    优化点：
    1.把setup和teardown换成了fixture方法get_calc
    2.把get_calc方法放到conftest中
    3.把参数化换为了fixture参数化方法
    4.测试用例中的数据需要通过 get_dates 获取
    get_datas 返回了一个列表[0.1,0.2,0.3],分别代表了a,b,except
    """

    # @pytest.mark.parametrize(
    #     "a,b,expect",
    #     add_datas, ids=myid
    # )
    # @pytest.mark.add
    def test_add(self, get_calc, get_datas):
        # 实例化计算器类
        # calc = Calculator()
        # 定义一个变量接收add方法的返回值
        # 调用相加方法
        result = get_calc.add(get_datas[0], get_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相加结果之后写断言
        assert result == get_datas[2]
