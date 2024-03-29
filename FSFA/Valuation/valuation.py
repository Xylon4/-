# 理财估值核算系统估值端自动化测试用例
# 估值批处理
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from FSFA.basepage_FSFA import BasePageFsfa


class Valuation(BasePageFsfa):
    # 估值批处理执行
    def valuation1(self, get_batch):
        I_CODE = get_batch[0]
        CALC_DATE = get_batch[1]
        # 点击批处理
        self.findxpath_click('//*[@id="navId"]/li[8]/a')
        # 点击估值批处理
        self.findxpath_click('//*[@id="floatMenu"]/dl[1]/dd[2]/a')
        # 定位账套
        self.findxpath_sendkey('//*[@name="accSecuId"]', I_CODE)
        sleep(1)
        self.findxpath_click('//div[3]/div/table/tbody/tr[2]/td/div/span')
        self.findxpath_click('//div[3]/div[2]/div[2]/div[2]//div/div[2]/div[2]/span/div/div[2]/div/div/a')
        sleep(2)
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
        # valuation = (By.XPATH, '/html/body/div[9]/div/div')
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(valuation))
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(valuation))
        # WebDriverWait(self.driver, 10).until(expected_conditions.NoSuchElementException(valuation))
        sleep(10)
        # 点击估值日切
        # 实际执行中，visibility_of_element_located这个方法也并不能展现元素的可点击状态，因为代码不完善，元素状态不随着肉眼可见的状态变更；
        # 显式等待能保证元素可被点击，之后的强制等待一秒保证顺畅处理，实际等待时间为N+1秒
        # 将visibility_of_element_located修改为element_to_be_clickable方法，沿用+1S逻辑，目前运行稳定
        self.findxpath_click('/html/body/div[3]/div[2]/div[3]/div[1]/div/div/a/span/span/span[1]')

        # sleep(120)
        # 等待估值批处理结束-显式等待
        def wait(x):
            batch_status = self.findxpath('/html/body/div[3]/div[2]//div[1]/div/div/label[1]').get_attribute(
                'textContent')
            return batch_status == "批次状态：执行完毕"

        WebDriverWait(self.driver, 300).until(wait)
        return True

    # 估值表检查
    def valuation2(self, get_batch):
        I_CODE = get_batch[0]
        amount_check = get_batch[2]
        cp_check = get_batch[3]
        asset_check = get_batch[4]
        cash_check = get_batch[5]
        nav_check = get_batch[6]
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
        amount = self.findxpath('//tbody/tr[5]/td[3]/div[@class="x-grid-cell-inner " and @style="text-align:right;"]')
        cp = self.findxpath('//tbody/tr[6]/td[5]/div[@class="x-grid-cell-inner " and @style="text-align:right;"]')
        asset = self.findxpath('//tbody/tr[19]/td[5]/div[@class="x-grid-cell-inner " and @style="text-align:right;"]')
        cash = self.findxpath('//tbody/tr[42]/td[5]/div[@class="x-grid-cell-inner " and @style="text-align:right;"]')
        nav = self.findxpath('//tbody/tr[54]/td[5]/div[@class="x-grid-cell-inner " and @style="text-align:right;"]')
        ele1 = amount.get_attribute('textContent')
        ele2 = cp.get_attribute('textContent')
        ele3 = asset.get_attribute('textContent')
        ele4 = cash.get_attribute('textContent')
        ele5 = nav.get_attribute('textContent')
        while ele1 == amount_check and ele2 == cp_check and ele3 == asset_check and ele4 == cash_check and ele5 == nav_check:
            return True

    # 估值回历史
    def valuation3(self, get_batch):
        I_CODE = get_batch[0]
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
        # 点击估值回历史
        self.findxpath_click('//div[3]/div[2]/div[2]/div[1]/div/div/a[2]/span/span/span[1]')
        # 在新页签中点击估值回历史
        sleep(2)
        self.findxpath_click('//div[3]/div[2]/div[3]/div[1]/div/div/a/span/span/span[2]')

        # 等待估值批处理结束-显式等待
        def wait(x):
            batch_status = self.findxpath('/html/body/div[3]/div[2]/div[3]/div[1]/div/div/label[1]').get_attribute(
                'textContent')
            return batch_status == "批次状态：执行完毕"

        WebDriverWait(self.driver, 100).until(wait)
        return True
