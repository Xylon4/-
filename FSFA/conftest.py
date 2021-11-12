import pytest


# 定义装饰器方法stagemark，用来标记用例的开始与结束
# @pytest.fixture(scope="module")
# def stagemark():
#     print("自动化案例执行开始")
#     yield
#     print("自动化案例执行结束")


# 解决命令行执行找不到调用的包
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
