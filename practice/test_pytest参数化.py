import pytest


class TestData:
    @pytest.mark.parametrize('a,b', [
        (1, 2),
        (2, 3)
    ])
    def test_date(self, a, b):
        print(a + b)
        print(a * b)
        print(a / b)
        print(a - b)
