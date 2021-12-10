# 产品信息表自动化测试用例
# 功能描述：统计投组产品核心和管理要素
from time import sleep
from selenium.webdriver.common.keys import Keys

from XAMS.basepage_XAMS import BasePageXams
from XAMS.Report.conftest import sheet2, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel


class Product(BasePageXams):
    def product(self):
        unit_id = 'gyxjzcpt001'
        check1 = 'C11111'
        check2 = '公募'
        check3 = '单独管理'
        check4 = '开放式净值型'
        check5 = '权益类'
        check6 = '表外'
        check7 = '否'
        check8 = '否'
        check9 = '2020-08-01'
        check10 = '2020-08-14'
        check11 = '有'
        check12 = '无'
        check13 = '否'
        check14 = 'C11111'
        check15 = '2020-08-14'
        check16 = '2020-12-28'
        check17 = '人民币'
        check18 = '人民币'
        check19 = '人民币'
        check20 = '个人'
        check21 = '主动管理业务'
        check22 = '独立运作'
        check23 = '否'
        check24 = '否'
        check25 = '商业银行发行'
        # 点击综合管理
        self.findxpath_click('//*[@id="navId"]/li[10]/a')
        # 点击产品信息表
        self.findxpath_click('//*[@id="floatMenu"]/dl[3]/dd[2]/a')
        # 输入产品名称（适用于非母子非分层产品）
        self.findxpath_sendkey('//tbody/tr/td[2]/input[@name="condition"]', unit_id)
        # 置空开始日期
        start_date = self.findxpath('//table[4]//tbody/tr/td[1]/input[@class="x-form-field x-form-text"]')
        start_date.send_keys(Keys.CONTROL, 'a')
        start_date.send_keys(Keys.BACK_SPACE)
        # 点击查询
        self.findxpath_click('//div[1]/a/span/span/span[@class="x-btn-icon-el x-toolbar-more-icon "]')
        self.findxpath_click('//div/a/span[@class="x-menu-item-text"]')
        # 校验信息
        # 发行结构代码
        issuer = self.findxpath('//div[2]/div[2]//tbody/tr/td[1]/div[@style="text-align:center;"]')
        # 募集方式
        raising = self.findxpath('//tbody/tr/td[7]/div[@style="text-align:center;"]')
        # 管理方式
        management = self.findxpath('//tbody/tr/td[8]/div[@style="text-align:center;"]')
        # 运行方式
        operation = self.findxpath('//tbody/tr/td[9]/div[@style="text-align:center;"]')
        # 产品类型
        product_type = self.findxpath('//tbody/tr/td[10]/div[@style="text-align:center;"]')
        # 业务模式
        business = self.findxpath('//tbody/tr/td[11]/div[@style="text-align:center;"]')
        # 收益保障标识
        revenue = self.findxpath('//tbody/tr/td[12]/div[@style="text-align:center;"]')
        # 本金保障标识
        principal = self.findxpath('//tbody/tr/td[13]/div[@style="text-align:center;"]')
        # 募集起始日期
        raising_start = self.findxpath('//tbody/tr/td[16]/div[@style="text-align:center;"]')
        # 募集结束日期
        raising_end = self.findxpath('//tbody/tr/td[17]/div[@style="text-align:center;"]')
        # 提前终止权标识
        early = self.findxpath('//tbody/tr/td[18]/div[@style="text-align:center;"]')
        # 客户赎回权标识
        redemption = self.findxpath('//tbody/tr/td[19]/div[@style="text-align:center;"]')
        # 产品增信标识
        credit = self.findxpath('//tbody/tr/td[20]/div[@style="text-align:center;"]')
        # 境内托管机构代码
        custodian = self.findxpath('//tbody/tr/td[21]/div[@style="text-align:center;"]')
        # 产品起始日期
        product_start = self.findxpath('//tbody/tr/td[24]/div[@style="text-align:center;"]')
        # 产品预计终止日期
        product_end = self.findxpath('//tbody/tr/td[25]/div[@style="text-align:center;"]')
        # 募集资金币种
        raising_currency = self.findxpath('//tbody/tr/td[27]/div[@style="text-align:center;"]')
        # 兑付本金币种
        cashing_principal_currency = self.findxpath('//tbody/tr/td[28]/div[@style="text-align:center;"]')
        # 兑付收益币种
        cashing_income_currency = self.findxpath('//tbody/tr/td[29]/div[@style="text-align:center;"]')
        # 客户类型
        customer_type = self.findxpath('//tbody/tr/td[30]/div[@style="text-align:center;"]')
        # 受托职责
        duties = self.findxpath('//tbody/tr/td[33]/div[@style="text-align:center;"]')
        # 合作模式
        cooperation = self.findxpath('//tbody/tr/td[34]/div[@style="text-align:center;"]')
        # 产品分级标识
        classification = self.findxpath('//tbody/tr/td[35]/div[@style="text-align:center;"]')
        # 收益权转让产品标识
        usufruct = self.findxpath('//tbody/tr/td[36]/div[@style="text-align:center;"]')
        # 理财产品发起机构标识
        identification = self.findxpath('//tbody/tr/td[37]/div[@style="text-align:center;"]')
        ele1 = issuer.get_attribute('textContent')
        ele2 = raising.get_attribute('textContent')
        ele3 = management.get_attribute('textContent')
        ele4 = operation.get_attribute('textContent')
        ele5 = product_type.get_attribute('textContent')
        ele6 = business.get_attribute('textContent')
        ele7 = revenue.get_attribute('textContent')
        ele8 = principal.get_attribute('textContent')
        ele9 = raising_start.get_attribute('textContent')
        ele10 = raising_end.get_attribute('textContent')
        ele11 = early.get_attribute('textContent')
        ele12 = redemption.get_attribute('textContent')
        ele13 = credit.get_attribute('textContent')
        ele14 = custodian.get_attribute('textContent')
        ele15 = product_start.get_attribute('textContent')
        ele16 = product_end.get_attribute('textContent')
        ele17 = raising_currency.get_attribute('textContent')
        ele18 = cashing_principal_currency.get_attribute('textContent')
        ele19 = cashing_income_currency.get_attribute('textContent')
        ele20 = customer_type.get_attribute('textContent')
        ele21 = duties.get_attribute('textContent')
        ele22 = cooperation.get_attribute('textContent')
        ele23 = classification.get_attribute('textContent')
        ele24 = usufruct.get_attribute('textContent')
        ele25 = identification.get_attribute('textContent')
        while ele1 == check1 and ele2 == check2 and ele3 == check3 and ele4 == check4 and ele5 == check5 and ele6 == check6 and ele7 == check7 and ele8 == check8 and ele9 == check9 and ele10 == check10 and ele11 == check11 and ele12 == check12 and ele13 == check13 and ele14 == check14 and ele15 == check15 and ele16 == check16 and ele17 == check17 and ele18 == check18 and ele19 == check19 and ele20 == check20 and ele21 == check21 and ele22 == check22 and ele23 == check23 and ele24 == check24 and ele25 == check25:
            return True

    # 模拟操作自动化案例
    def product_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu().get(menu[0]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu().get(f'{menu[0]}-{menu[1]}'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 2
        while n < l:
            targetsheet = self.base.sheet_xpath_dic(Excel_basedata_zs, sheet2)
            findelement = self.findxpath(targetsheet.get(menu[n]))
            if menu[n] == '导出':
                findelement.click()
            elif menu[n] == '批量导出':
                findelement.click()
            elif menu[n] == '投组':
                if value[n] == '置空':
                    unit = self.findxpath(targetsheet.get(menu[n]))
                    unit.send_keys(Keys.CONTROL, 'a')
                    unit.send_keys(Keys.BACK_SPACE)
                else:
                    unit = self.findxpath(targetsheet.get(menu[n]))
                    unit.send_keys(Keys.CONTROL, 'a')
                    unit.send_keys(Keys.BACK_SPACE)
                    self.findxpath_sendkey(targetsheet.get(menu[n]), value[n])
                    sleep(1)
                    self.findxpath_click(targetsheet.get('投组下拉选择'))
            elif menu[n] == '产品名称或代码':
                if value[n] == '置空':
                    code = self.findxpath(targetsheet.get(menu[n]))
                    code.send_keys(Keys.CONTROL, 'a')
                    code.send_keys(Keys.BACK_SPACE)
                else:
                    code = self.findxpath(targetsheet.get(menu[n]))
                    code.send_keys(Keys.CONTROL, 'a')
                    code.send_keys(Keys.BACK_SPACE)
                    self.findxpath_sendkey(targetsheet.get(menu[n]), value[n])
            elif menu[n] == '搜索':
                self.findxpath_click(targetsheet.get('折叠按钮'))
                findelement.click()
            elif menu[n] == '起息日起':
                if value[n] == '置空':
                    start_date = self.findxpath(targetsheet.get(menu[n]))
                    start_date.send_keys(Keys.CONTROL, 'a')
                    start_date.send_keys(Keys.BACK_SPACE)
                else:
                    start_date = self.findxpath(targetsheet.get(menu[n]))
                    start_date.send_keys(Keys.CONTROL, 'a')
                    start_date.send_keys(Keys.BACK_SPACE)
                    self.findxpath_sendkey(targetsheet.get(menu[n]), value[n])
            elif menu[n] == '起息日止':
                self.findxpath_click(targetsheet.get('折叠按钮'))
                if value[n] == '置空':
                    start_date = self.findxpath(targetsheet.get(menu[n]))
                    start_date.send_keys(Keys.CONTROL, 'a')
                    start_date.send_keys(Keys.BACK_SPACE)
                else:
                    start_date = self.findxpath(targetsheet.get(menu[n]))
                    start_date.send_keys(Keys.CONTROL, 'a')
                    start_date.send_keys(Keys.BACK_SPACE)
                    self.findxpath_sendkey(targetsheet.get(menu[n]), value[n])
            elif menu[n] == '产品分类(收益特性)':
                findelement.click()
                if value[n] == '保证收益型':
                    self.findxpath_click(targetsheet.get(value[n]))
                elif value[n] == '保本浮动收益型':
                    self.findxpath_click(targetsheet.get(value[n]))
                elif value[n] == '非保本浮动收益型':
                    self.findxpath_click(targetsheet.get(value[n]))
                else:
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
                findelement.click()
            else:
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            n = n + 1
        return True
