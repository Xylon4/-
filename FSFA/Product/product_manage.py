# 理财估值核算系统产品端自动化测试用例
# 账套创建
from selenium.webdriver import TouchActions

from FSFA.basepage_FSFA import BasePageFsfa


class ProductManage(BasePageFsfa):
    def productmanage1(self):
        # 点击账套管理
        self.findxpath_click('//*[@id="navId"]/li[3]/a')
        # 点击账套设置
        self.findxpath_click('//*[@id="floatMenu"]/dl[1]/dd[2]/a')
        # 选择第一条待创建数据
        self.findxpath_click('/html/body/div[3]/div[2]/div[3]/div/div/div[3]/div/table/tbody/tr[1]/td[4]/div')
        # 点击新增按钮
        self.findxpath_click(
            '/html/body/div[3]/div[2]/div[3]/div/div/div[1]/span/div/div[1]/div/div/a[2]/span/span/span[1]')
        # 点击账套选择倒三角
        self.findxpath_click(
            '/html/body/div[3]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[1]//table[1]/tbody/tr/td[2]/table/tbody/tr/td[2]/div')
        # 选择理财子公司
        self.findxpath_click('/html/body/div[26]/div[3]/div/table/tbody/tr[4]/td/div/span')
        # 页面下滑到底部
        action = TouchActions(self.driver)
        basic1 = self.findxpath('//*[@class="x-component x-fieldset-header-text x-component-default"]')
        action.scroll_from_element(basic1, 0, 10000).perform()
        # 点击费用的新增按钮
        self.findxpath_click('/html//div[2]/div[2]/div/div[1]/div/div/a[1]/span/span/span[1]')
        # 输入费率
        self.findxpath_sendkey(
            '/html/body/div[29]/div[2]/div/div[1]//table[11]/tbody/tr/td[2]/table/tbody/tr/td[1]/input', '0.01')
        # 点击保存按钮
        self.findxpath_click('/html/body/div[29]/div[2]/div/div[2]/div/div/a[1]/span/span/span[1]')
        # 点击清算路径
        self.findxpath_click('/html/body/div[3]/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/a[2]/span/span/span[1]')
