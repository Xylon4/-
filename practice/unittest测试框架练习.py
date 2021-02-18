import unittest


# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# 定义被测试方法 search_fun
class Search:
    def search_fun(self):
        print("search")
        return True


class TestSearch1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("测试开始，我会出现在每个CLASS的开头")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print("测试结束，我会出现在每个CLASS的末尾")

    def setUp(self) -> None:
        print("案例执行开始，我会出现在每个案例的开头")
        self.search = Search()

    def tearDown(self) -> None:
        print("案例执行结束，我会出现在每个案例的末尾")

    def test_search1(self):
        print("案例1在此")
        assert True == self.search.search_fun()

    def test_search2(self):
        print("案例2在此")
        assert True == self.search.search_fun()

    def test_search3(self):
        print("案例3在此")
        assert True == self.search.search_fun()

    def test_notequal(self):
        print("断言不相等")
        # self.assertNotEqual(1, 1, "判断1！=2")
        self.assertTrue(1 == 1, "verif")


class TestSearch2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("测试开始，我会出现在每个CLASS的开头")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print("测试结束，我会出现在每个CLASS的末尾")

    def setUp(self) -> None:
        print("案例执行开始，我会出现在每个案例的开头")
        self.search = Search()

    def tearDown(self) -> None:
        print("案例执行结束，我会出现在每个案例的末尾")

    def test_search21(self):
        print("案例21在此")
        assert True == self.search.search_fun()

    def test_search22(self):
        print("案例22在此")
        assert True == self.search.search_fun()

    def test_search23(self):
        print("案例23在此")
        assert True == self.search.search_fun()

    def test_notequal(self):
        print("断言相等")
        # self.assertNotEqual(1, 1, "判断1==1")
        self.assertTrue(1 == 1, "verif")


# 使用main调用所有测试模块，unittest.main()为执行unittest的固定写法

if __name__ == '__main__':
    # unittest.main()

    # 创建一个测试套件，testsuite
    suite1 = unittest.TestSuite()
    # 套件中添加需要执行的案例,可以添加多个
    suite1.addTest(TestSearch1("test_search1"))
    suite1.addTest(TestSearch1("test_search3"))
    unittest.TextTestRunner().run(suite1)

    # 套件中添加需要执行的测试类
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch2)
    suite = unittest.TestSuite([suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)

    # 两个不同类型的套件能兼容执行
