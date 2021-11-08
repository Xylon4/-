# 用None来描述动态默认值的参数
import time
from datetime import datetime


def log(message, when=None):
    when = datetime.now() if when is None else when
    print('{}:{}'.format(when, message))

log('Hi,there!')
time.sleep(0.1)
log('Hi,again!')