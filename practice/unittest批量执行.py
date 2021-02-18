import unittest

# 初步猜测，应为路径中-的原因，不能加载出对应的文件，导致执行没结果
if __name__ == '__main__':
    test_dir = 'D:/PycharmProjects/-/practice'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")
    unittest.TextTestRunner(verbosity=2).run(discover)
