# 资产池注册表自动化测试用例
# 功能描述：统计投组成立时间
from time import sleep

from selenium.webdriver.common.keys import Keys

from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class AssetPoolRegistry(BasePageXams):
    # 版本更新校验历史数据自动化测试案例
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

    # 自动化测试工具案例
    def registry_excel(self):
        unit_id = 'gyxjzcpt001'
        unit_id_xpath = '//tbody/tr[3]/td/div/span[@class="x-tree-node-text "]'
        # 获取字典
        self.excel = TestExcel()
        # 点击综合管理
        self.findxpath_click(self.excel.first_menu().get('综合管理'))
        # self.findxpath_click('//*[@id="navId"]/li[10]/a')
        # 点击资产池注册表
        self.findxpath_click(self.excel.second_menu().get('资产池注册表'))
        # self.findxpath_click('//*[@id="floatMenu"]/dl[3]/dd[1]/a')
        sleep(1)
        # 选择投组
        if self.excel.registry_list()[3] == 1:
            self.findxpath_sendkey(self.excel.registry_xpath().get('投组'), unit_id)
            sleep(1)
            self.findxpath_click(unit_id_xpath)
        # 输入产品名称/代码
        if self.excel.registry_list()[4] == 1:
            self.findxpath_sendkey(self.excel.registry_xpath().get('产品名称/代码'),
                                   self.excel.get_cell_value('资产池注册表', 5, 3))
        # 输入开始日期日
        if self.excel.registry_list()[5] == 1:
            if self.excel.get_cell_value('资产池注册表', 6, 3) == '置空':
                start_date = self.findxpath(self.excel.registry_xpath().get('开始日期'))
                start_date.send_keys(Keys.CONTROL, 'a')
                start_date.send_keys(Keys.BACK_SPACE)
            else:
                start_date = self.findxpath(self.excel.registry_xpath().get('开始日期'))
                start_date.send_keys(Keys.CONTROL, 'a')
                start_date.send_keys(Keys.BACK_SPACE)
                start_date.send_keys(self.excel.get_cell_value('资产池注册表', 6, 3))
        # 输入结束日期
        if self.excel.registry_list()[6] == 1:
            if self.excel.get_cell_value('资产池注册表', 7, 3) == '置空':
                start_date = self.findxpath(self.excel.registry_xpath().get('结束日期'))
                start_date.send_keys(Keys.CONTROL, 'a')
                start_date.send_keys(Keys.BACK_SPACE)
            else:
                start_date = self.findxpath(self.excel.registry_xpath().get('结束日期'))
                start_date.send_keys(Keys.CONTROL, 'a')
                start_date.send_keys(Keys.BACK_SPACE)
                start_date.send_keys(self.excel.get_cell_value('资产池注册表', 7, 3))
        # 点击搜索
        if self.excel.registry_list()[7] == 1:
            self.findxpath_click(self.excel.registry_xpath().get('搜索'))
        # 点击落地

        # 点击导出
        if self.excel.registry_list()[0] == 1:
            self.findxpath_click(self.excel.registry_xpath().get('导出'))
        # 点击批量导出

        return True
