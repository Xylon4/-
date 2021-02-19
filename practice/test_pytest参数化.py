import pytest
import yaml


class TestData:
    @pytest.mark.parametrize('a,b', [
        (1, 2),
        (2, 3)
    ])
    def test_date1(self, a, b):
        print(a + b)
        print(a * b)
        print(a / b)
        print(a - b)

    @pytest.mark.parametrize('a,b', [
        (1, 2),
        (2, 2),
        (3, 2)
    ])
    def test_answer(self, a, b):
        if a == b:
            print("这俩玩意相等")
        if a > b:
            print(f"{a}大于{b}")
        else:
            print(f"{a}小于{b}")

    # 外部文件数据驱动
    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./data.yaml")))
    def test_data2(self, a, b):
        print(a + b)
