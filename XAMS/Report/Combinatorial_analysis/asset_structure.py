# 资产结构分析表自动化测试用例
# 功能描述：统计投组资产结构分布
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from XAMS.Report.conftest import sheet27, Excel_basedata_zs
from XAMS.Tool.test_excel import TestExcel
from XAMS.basepage_XAMS import BasePageXams


class AssetStructure(BasePageXams):
    # 模拟操作自动化案例
    def asset_structure_excel(self, menu, value):
        print(menu)
        print(value)
        self.base = TestExcel()
        # 点击一级菜单
        self.findxpath_click(self.base.first_menu(Excel_basedata_zs).get(menu[1]))
        # 点击二级菜单
        self.findxpath_click(self.base.second_menu(Excel_basedata_zs).get(f'{menu[1]}-{menu[2]}'))
        # 根据自定义顺序执行操作
        l = len(menu)
        n = 3
        while n < l:
            targetsheet = self.base.sheet_xpath_dic(Excel_basedata_zs, sheet27)
            findelement = self.findxpath(targetsheet.get(menu[n]))
            wait = (By.XPATH, targetsheet.get('加载等待'))
            if menu[n] == '导出':
                findelement.click()
            elif menu[n] == 'Excel(当前页)':
                findelement.click()
            elif menu[n] == 'Excel(所有数据)':
                findelement.click()
            elif menu[n] == '全部展开':
                if findelement.get_attribute('textContent') == menu[n]:
                    findelement.click()
                    self.wait_for_miss(120, wait)
                else:
                    print(f'请检查当前按钮显示是否为"{menu[n]}"，若显示一致，请联系测试开发')
                    return False
            elif menu[n] == '一键收起':
                if findelement.get_attribute('textContent') == menu[n]:
                    findelement.click()
                    self.wait_for_miss(120, wait)
                else:
                    print(f'请检查当前按钮显示是否为"{menu[n]}"，若显示一致，请联系测试开发')
                    return False
            elif menu[n] == '是否穿透':
                if value[n] not in ['是', '否']:
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(value[n])
            elif menu[n] == '所属投组':
                if value[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(value[n])
                    sleep(1)
                    self.findxpath_click(targetsheet.get('投组下拉选择'))
            elif menu[n] == '开始日期':
                if value[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(value[n])
            elif menu[n] == '结束日期':
                if value[n] == '置空':
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                else:
                    findelement.send_keys(Keys.CONTROL, 'a')
                    findelement.send_keys(Keys.BACK_SPACE)
                    findelement.send_keys(value[n])
            elif menu[n] == '数据来源':
                findelement.click()
                if value[n] == '估值核算':
                    self.findxpath_click(targetsheet.get(value[n]))
                elif value[n] == '理财资管':
                    self.findxpath_click(targetsheet.get(value[n]))
                else:
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
            elif menu[n] == '搜索':
                findelement.click()
                # 搜索结束判断依据缺失，产品要改
            elif menu[n] == '图形展示':
                findelement.click()
                show = value[n].split(',')  # str类型转换为list，用,分隔
                if show[1] == '查询':
                    searchdate = self.findxpath(targetsheet.get('查询日期'))
                    searchdate.send_keys(Keys.CONTROL, 'a')
                    searchdate.send_keys(Keys.BACK_SPACE)
                    searchdate.send_keys(show[0])
                    self.findxpath_click(targetsheet.get(show[1]))
                    sleep(1)
                elif show[1] == '返回':
                    searchdate = self.findxpath(targetsheet.get('查询日期'))
                    searchdate.send_keys(Keys.CONTROL, 'a')
                    searchdate.send_keys(Keys.BACK_SPACE)
                    searchdate.send_keys(show[0])
                    self.findxpath_click(targetsheet.get(show[1]))
                else:
                    print(f'值"{value[n]}"输入错误，请检查')
                    return False
            else:
                print(f'操作元素"{menu[n]}"输入错误，请检查')
                return False
            n = n + 1
        return True
