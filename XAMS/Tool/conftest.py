# 解决命令行执行找不到调用的包
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

Excel_basedata = 'E:\菜单基础数据维护.xlsx'
Excel_custom = 'E:\自动化测试用例模板.xlsx'
universal_sheet = 'Sheet1'
