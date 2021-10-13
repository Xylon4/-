# 资产池注册表自动化测试用例
# 功能描述：统计投组成立时间
from time import sleep

from selenium.webdriver.common.keys import Keys

from XAMS.basepage_XAMS import BasePageFsfa


class AssetPoolRegistry(BasePageFsfa):
    def registry(self):
        self.findxpath_sendkey('//*[@id="navId"]/li[10]/a')