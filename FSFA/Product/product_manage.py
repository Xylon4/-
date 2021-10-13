# 理财估值核算系统产品端自动化测试用例
# 账套创建及复核
from time import sleep

from selenium.webdriver import TouchActions
from selenium.webdriver.common.keys import Keys

from FSFA.basepage_FSFA import BasePageFsfa


class ProductManage(BasePageFsfa):
    def productmanage1(self, get_product_manage):
        fee_rate = get_product_manage[0]
        accid01 = get_product_manage[1]
        accname01 = get_product_manage[2]
        accid02 = get_product_manage[3]
        accname02 = get_product_manage[4]
        accid03 = get_product_manage[5]
        accname03 = get_product_manage[6]
        # 点击账套管理
        self.findxpath_click('//*[@id="navId"]/li[3]/a')
        # 点击账套设置
        self.findxpath_click('//*[@id="floatMenu"]/dl[1]/dd[2]/a')
        # 选择第一条待创建数据
        self.findxpath_click('/html/body/div[3]/div[2]/div[2]/div/div/div[3]/div/table/tbody/tr[1]/td[4]/div')
        # 点击新增按钮
        self.findxpath_click(
            '/html/body/div[3]/div[2]/div[2]/div/div/div[1]/span/div/div[1]/div/div/a[2]')
        # 选择理财子公司
        self.findxpath_sendkey('//*[@name="investGrpPkgId"]', "理财子公司")
        sleep(1)
        self.findxpath_click('//*[@class="x-tree-node-text "]')
        # 页面下滑到底部
        action = TouchActions(self.driver)
        basic1 = self.findxpath('//*[@class="x-component x-fieldset-header-text x-component-default"]')
        action.scroll_from_element(basic1, 0, 1000).perform()
        # 点击费用的新增按钮
        self.findxpath_click('/html//div[2]/div[2]/div/div[1]/div/div/a[1]/span/span/span[1]')
        # 输入费率
        self.findxpath_sendkey(
            '//*[@name="amountTextFiled-1578-inputEl"]', fee_rate)
        # 点击保存按钮
        self.findxpath_click('/html/body/div[14]/div[2]/div/div[2]/div/div/a[1]')
        # 点击清算路径
        self.findxpath_click('/html/body/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/a[2]')
        # 点击资金账户中的新增按钮
        self.findxpath_click(
            '/html/body/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div/div/a[1]')
        # 输入资金账号
        self.findxpath_sendkey(
            '//div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[2]//table[2]/tbody/tr/td[2]/input',
            accid01)
        # 输入资金账户名称
        self.findxpath_sendkey('//*[@name="cashAccExtName"]', accname01)
        # 选择开户行
        self.findxpath_sendkey('//*[@name="customerId"]', '310290000013')
        # 下拉选择的第一个选项的div会随机变更，此处的写法不稳妥，故用模拟键盘方向↓键组合回车键完成
        # self.findxpath_click('/html/body/div[16]/div/ul/li')
        bank_name1 = self.findxpath('//*[@name="customerId"]')
        bank_name1.send_keys(Keys.SPACE)
        bank_name1.send_keys(Keys.ARROW_DOWN)
        bank_name1.send_keys(Keys.ENTER)
        # 选择活期利率
        self.findxpath_click('//*[@name="rateDefId"]')
        # 同理，键盘方向↓键组合回车键完成选择
        interest_rate = self.findxpath('//*[@name="rateDefId"]')
        interest_rate.send_keys(Keys.ARROW_DOWN)
        interest_rate.send_keys(Keys.ENTER)
        # 点击保存
        self.findxpath_click(
            '/html/body/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[3]/div/div/a[1]')
        # 点击银行间账户信息中的新增按钮
        self.findxpath_click(
            '//div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]//div[2]/div[2]/div/div/a[1]/span/span/span[1]')
        # 选择托管模式-乙类户
        self.findxpath_click('//*[@value="多级托管"]')
        # 同开户行
        # self.findxpath_click('/html/body/div[30]/div/ul/li[1]')
        managed_mode = self.findxpath('//*[@value="多级托管"]')
        managed_mode.send_keys(Keys.ARROW_DOWN)
        managed_mode.send_keys(Keys.ENTER)
        # 输入证券账号
        self.findxpath_sendkey('//*[@name="exhSecu"]', accid02)
        # 输入账户名称
        self.findxpath_sendkey('//*[@name="secuAccExtName"]', accname02)
        # 输入资金账号
        self.findxpath_sendkey(
            '//div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[4]/div[2]//table[7]/tbody/tr/td[2]/input',
            accid03)
        # 输入资金账户名称
        self.findxpath_sendkey('//*[@name="cashAccDvpName"]', accname03)
        # 选择开户行-中债登
        self.findxpath_sendkey(
            '//div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[4]/div[2]//table[9]/tbody/tr/td[2]/table/tbody/tr/td[1]/input',
            '中债登')
        # 直接输入关键字"中债登"未能触发关键字匹配，模拟人工操作：输入完成后加一个空格触发匹配
        bank_name2 = self.findxpath(
            '//div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[4]/div[2]//table[9]/tbody/tr/td[2]/table/tbody/tr/td[1]/input')
        bank_name2.send_keys(Keys.SPACE)
        bank_name2.send_keys(Keys.ARROW_DOWN)
        bank_name2.send_keys(Keys.ENTER)
        # 点击弹窗中的保存
        self.findxpath_click(
            '/html/body/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[4]/div[3]/div/div/a[1]')
        # 点击保存
        self.findxpath_click('/html/body/div[3]/div[2]/div[2]/div/div[2]/div[2]/div/div/a[1]')
        # 点击浮窗中的确定
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        # 点击复核按钮
        self.findxpath_click('/html/body/div[3]/div[2]/div[2]/div/div[2]/div[2]/div/div/a[4]')
        self.findxpath_click('//*[@id="button-1006-btnIconEl"]')
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        return True
