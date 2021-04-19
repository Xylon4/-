# 理财估值核算系统产品端自动化测试用例
# 估值批处理
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from FSFA.basepage_FSFA import BasePageFsfa


class Valuation(BasePageFsfa):
    # 估值批处理执行
    def valuation1(self):
        I_CODE = "FB0419"
        CALC_DATE = "2020-03-04"
        # 点击批处理
        self.findxpath_click('//*[@id="navId"]/li[8]/a')
        # 点击估值批处理
        self.findxpath_click('//*[@id="floatMenu"]/dl[1]/dd[2]/a')
        # 定位账套
        self.findxpath_sendkey('//*[@name="accSecuId"]', I_CODE)
        sleep(1)
        self.findxpath_click('//div[3]/div/table/tbody/tr[2]/td/div/span')
        self.findxpath_click('//div[3]/div[2]/div[2]/div[2]//div/div[2]/div[2]/span/div/div[2]/div/div/a')
        sleep(1)
        self.findxpath_click('//div[3]/div[2]/div[2]/div[2]//div[2]/div[4]/div/table/tbody/tr/td[2]/div')
        # 点击估值日切
        self.findxpath_click('//div[3]/div[2]/div[2]/div[1]/div/div/a[1]')
        sleep(1)
        # 输入目标估值日期
        date = self.findxpath('//div[3]/div[2]/div[3]/div[1]//tbody/tr/td[2]/table/tbody/tr/td[1]/input')
        date.send_keys(Keys.CONTROL, "a")
        date.send_keys(Keys.DELETE)
        # self.findxpath('//div[3]/div[2]/div[3]/div[1]//tbody/tr/td[2]/table/tbody/tr/td[1]/input').clear()
        self.findxpath_sendkey('//div[3]/div[2]/div[3]/div[1]//tbody/tr/td[2]/table/tbody/tr/td[1]/input', CALC_DATE)
        valuation = (By.XPATH, '/html/body/div[3]/div[2]/div[3]/div[1]/div/div/a')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(valuation))
        sleep(1)
        # 点击估值日切
        # 实际执行中，visibility_of_element_located这个方法也并不能展现元素的可点击状态，实际生效的还是强制等待这一秒，待优化
        self.findxpath_click('/html/body/div[3]/div[2]/div[3]/div[1]/div/div/a')

        # sleep(120)
        # 等待估值批处理结束-显式等待
        def wait(x):
            batch_status = self.findxpath('/html/body/div[3]/div[2]//div[1]/div/div/label[1]').get_attribute(
                'textContent')
            return batch_status == "批次状态：执行完毕"

        WebDriverWait(self.driver, 300).until(wait)
        return True

    # 估值表检查
    def valuation2(self):
        I_CODE = "FB0419"
        # 点击估值管理
        self.findxpath_click('//*[@id="navId"]/li[7]/a')
        # 点击估值表查询
        self.findxpath_click('//*[@id="floatMenu"]/dl[1]/dd/a')
        # 查询当日估值表
        self.findxpath_sendkey('//*[@name="wmsunitname$array"]', I_CODE)
        sleep(1)
        self.findxpath_click('/html/body/div[last()]/div[3]/div/table/tbody/tr[2]/td/div/span')
        self.findxpath_click('/html/body/div[3]/div[2]//div/div/div[1]/div/div/a[3]')
        sleep(5)
        # 判断值是否正确
        amount = self.findxpath('//div[3]/div[2]//div/div/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[5]/td[3]/div')
        cp = self.findxpath('//div[3]/div[2]//div/div/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[5]/td[5]/div')
        asset = self.findxpath('//div[3]/div[2]//div/div/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[19]/td[5]/div')
        cash = self.findxpath('//div[3]/div[2]//div/div/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[42]/td[5]/div')
        nav = self.findxpath('//div[3]/div[2]//div/div/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[53]/td[5]/div')
        ele1 = amount.get_attribute('textContent')
        ele2 = cp.get_attribute('textContent')
        ele3 = asset.get_attribute('textContent')
        ele4 = cash.get_attribute('textContent')
        ele5 = nav.get_attribute('textContent')
        while ele1 == "1,000,000.00" and ele2 == "99,930,843.84" and ele3 == "99,930,843.84" and ele4 == "87,786.30" and ele5 == "1.000181":
            return True
