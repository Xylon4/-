import pytest
import os, sys

path = os.path.abspath(__file__)
for i in range(2):
    path = os.path.dirname(path)
    sys.path.append(path)
from product import Product


# import sys
#
# from tools.getrootdir import get_root_dir
#
# sys.path.append(get_root_dir())
#
#
# # 将这两句添加到入口文件的起始位置，这样之后的导入和其他文件的导入就不会报找不到的问题了


class TestProduct:
    def teardown(self):
        self.product.end()

    def test_product(self, stagemark):
        self.product = Product()
        assert self.product.product1()

# if __name__ == '__main__':
#     pytest.main()
