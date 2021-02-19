import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_demo(self, env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的IP是:", env["test"])
        # 当下面语句使用if时，无论上个if是否已经满足条件，还会再判断一次，并输出结果；若使用elif，则不会判断
        if "dev" in env:
            print("这是开发环境")
            print("开发环境的IP是:", env["dev"])
        else:
            print("未找到任何环境")

# 模糊匹配未实现
