import pytest


# pytest.assume列出所有报错的断言信息
def test_a():
    # assert 1==2
    # assert False ==True
    # assert 100 == 200
    pytest.assume(1 == 1)
    pytest.assume(False == True)
    pytest.assume(100 == 200)
