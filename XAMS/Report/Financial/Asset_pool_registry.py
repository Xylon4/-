# 资产池注册表自动化测试用例
# 功能描述：统计投组成立时间
from time import sleep

from selenium.webdriver.common.keys import Keys

from XAMS.basepage_XAMS import BasePageFsfa


class AssetPoolRegistry(BasePageFsfa):
    def registry(self, get_registry):
        unit_id = get_registry[0]
        check_date = get_registry[1]
        # 点击综合管理
        self.findxpath_click('//*[@id="navId"]/li[10]/a')
        # 点击资产池注册表
        self.findxpath_click('//*[@id="floatMenu"]/dl[3]/dd[1]/a')
        sleep(1)
        # 输入产品名称（适用于非母子非分层产品）
        self.findxpath_sendkey('//tbody/tr/td[2]/input[@class="x-form-field x-form-text"]', unit_id)
        # 置空开始日期
        start_date = self.findxpath('//table[4]//tbody/tr/td[1]/input[contains(@class,"x-form-field x-form-text")]')
        start_date.send_keys(Keys.CONTROL, 'a')
        start_date.send_keys(Keys.BACK_SPACE)
        # 点击搜索
        self.findxpath_click('//div[2]/div/div/a[contains(@ID,"button")]')
        # 校验日期
        beg_date = self.findxpath('//div[3]/div[2]/div[2]//tbody/tr/td[2]/div[@style="text-align:center;"]')
        ele1 = beg_date.get_attribute('textContent')
        while ele1 == check_date:
            return True
