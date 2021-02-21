import pytest


class TestCalc:

    # 测试加法案例
    # 设置加法案例执行顺序为1
    @pytest.mark.run(order=1)
    def test_add(self, stageprint, get_calc, get_add_datas):
        result = get_calc.add(get_add_datas[0], get_add_datas[1])
        # 判断result的数据类型，如果是浮点数，result强制保留小数点后两位
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_add_datas[2]

    # 测试除法案例
    # 设置除法案例执行顺序为4
    @pytest.mark.run(order=4)
    def test_div(self, stageprint, get_calc, get_div_datas):
        result = get_calc.div(get_div_datas[0], get_div_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_div_datas[2]

    # 测试减法案例
    # 设置减法案例执行顺序为2
    @pytest.mark.run(order=2)
    def test_sub(self, stageprint, get_calc, get_sub_datas):
        result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_sub_datas[2]

    # 测试乘法案例
    # 设置乘法案例执行顺序为3
    @pytest.mark.run(order=3)
    def test_mul(self, stageprint, get_calc, get_mul_datas):
        result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_mul_datas[2]
