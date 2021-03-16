class BasePage:
    # 被继承的基类中一定要有初始化driver，不然驱动无法复用和传递，每一个链式调用都会报错
    def __init__(self, driver):
        self.driver = driver
