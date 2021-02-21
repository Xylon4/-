from time import sleep

import pytest


def test_rerun1():
    sleep(0.5)
    assert 1==2

def test_rerun2():
    sleep(0.5)
    assert 2==2

#命令行方式pytest test_rerun.py --reruns 3 --reruns-delay 1
#装饰器方式@pytest.mark.flaky(reruns=5,reruns_delay=1)
#都可以实现重跑，区别在于命令行会将所有报错的都重跑，装饰器使用后才重跑
@pytest.mark.flaky(reruns=5,reruns_delay=1)
def test_rerun3():
    sleep(0.5)
    assert 3==2


