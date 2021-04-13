# 理财估值核算系统产品端自动化测试用例
# 产品新增及复核
from time import sleep

from FSFA.basepage_FSFA import BasePageFsfa


class Product(BasePageFsfa):
    def product1(self):
        i_Code = "FB0401-3"
        end_date = "20220331"
        # 点击账套管理
        self.findxpath_click('//*[@id="navId"]/li[3]/a')
        # 点击产品信息定义
        self.findxpath_click('//*[@id="floatMenu"]/dl[2]/dd/a')
        # 点击新增按钮
        self.findxpath_click('//*[@id="addButton-1093"]')
        # 点击是否平行分层
        self.findxpath_click('//*[@id="combobox-1235-inputEl"]')
        self.findxpath_click('//*[@id="boundlist-1369-listEl"]/ul/li[2]')
        # 输入产品代码
        self.findxpath_sendkey('//*[@id="textfield-1239-inputEl"]', i_Code)
        # 输入产品名称
        self.findxpath_sendkey('//*[@id="textfield-1241-inputEl"]', "封闭净值型产品")
        # 输入产品全称
        self.findxpath_sendkey('//*[@id="textfield-1256-inputEl"]', "封闭净值型理财产品")
        # 点击产品类型选择框
        self.findxpath_click('//*[@id="commonCombox-1242-inputEl"]')
        # 选择产品类型
        self.findxpath_click("/html/body/div[7]/div/ul/li[1]")
        # 输入管理人
        self.findxpath_sendkey('//*[@id="textfield-1250-inputEl"]', "浦银理财子公司")
        # 输入托管人
        self.findxpath_sendkey('//*[@id="textfield-1251-inputEl"]', "上海浦东发展银行")
        self.findxpath_sendkey('//*[@id="datefield-1281-inputEl"]', end_date)
        self.findxpath_click('//*[@id="saveButton-1226-btnInnerEl"]')
        sleep(2)
        # 点击浮窗中的确定
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        # 点击返回按钮
        self.findxpath_click('//*[@id="backButton-1229-btnInnerEl"]')
        # 输入产品代码
        self.findxpath_sendkey('//*[@id="textfield-1080-inputEl"]', i_Code)
        # 点击搜索按钮
        self.findxpath_click('//*[@id="searchButton-1108-btnInnerEl"]')
        sleep(1)
        # 勾选产品
        self.findxpath_click('//*[@class="x-grid-cell-inner x-grid-cell-inner-row-numberer"]')
        # 点击复核按钮
        self.findxpath_click('//*[@id="reviewButton-1098-btnInnerEl"]')
        self.findxpath_click('//*[@id="button-1006-btnIconEl"]')
        self.findxpath_click('//*[@id="button-1005-btnIconEl"]')
        return True
