# 封装excel读取、生成字典等公共方法
# 1、读取Excel表数据
# 2、把数据作为参数传给后面的函数
# 3、后面的函数循环读取参数执行操作
import pandas as pd
import xlrd
from openpyxl.utils import get_column_letter
import math
from XAMS.Tool.conftest import Excel_basedata_zs, Excel_custom, universal_sheet, auto_sheet, Excel_xls, Excel_xlsx, \
    Excel_basedata_nj


class TestExcel:
    # 定义获取单列数据,并将数据存入列表[]的方法
    def test_list(self):
        # wb = xlrd.open_workbook_xls()
        # 打开excel文件
        wb = xlrd.open_workbook(Excel_basedata_zs)
        # 获取sheet，通过Excel表格名称()获取工作表
        sheet = wb.sheet_by_name('一级菜单')
        # 创建空list
        dat = []
        for a in range(sheet.nrows):  # 循环读取表格内容（每次读取一行数据）
            cells = sheet.row_values(a)  # 每行数据赋值给cells
            # 根据数据类型选择合适的转换类型num选用（int、float、bool、complex）中文选用(str)
            data = str(cells[0])  # 因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
            dat.append(data)  # 把每次循环读取的数据插入到list
        return dat

    # 获取sheet页第一列数据生成list
    def sheet_list(self, Excel_basedata, sheetname):
        # 打开excel文件
        wb = xlrd.open_workbook(Excel_basedata)
        # 获取sheet，通过Excel表格名称()获取工作表
        sheet = wb.sheet_by_name(sheetname)
        dat = []
        for a in range(sheet.nrows):  # 循环读取表格内容（每次读取一行数据）
            cells = sheet.row_values(a)  # 每行数据赋值给cells
            # 根据数据类型选择合适的转换类型num选用（int、float、bool、complex）中文选用(str)
            data = str(cells[0])  # 将第一列数据存入列表
            dat.append(data)  # 把每次循环读取的数据插入到list
        return dat

    # 定义获取整行数据，并将数据存入字典{}的方法
    def test_dic(self):
        # 打开excel文件
        wb = xlrd.open_workbook(Excel_basedata_zs)
        # 通过名称定位所有sheet
        sheet1 = wb.sheet_by_name('一级菜单')
        sheet2 = wb.sheet_by_name('二级菜单')
        sheet3 = wb.sheet_by_name('资产池注册表')
        sheet4 = wb.sheet_by_name('产品信息表')
        sheet5 = wb.sheet_by_name('资负信息注册(浙商)')
        # 打印sheet的名称，行数，列数，用来校验字典中item数量
        print(sheet2.name, sheet2.nrows, sheet2.ncols)
        # 获取整行或整列的值
        rows2 = sheet2.row_values(8)
        cols = sheet2.col_values(1)
        # print(sheet2.row_values(8))
        # print(sheet2.row_values(9))     # 可知合并单元格不能显示在后续的行或者列中，需要取消合并复制粘贴
        # print(sheet2.row_values(10))
        # print(sheet2.col_values(1))
        # sheet页第三列数据从第二行开始标记是否有值
        print(sheet3.col_types(3, 1))
        print(sheet3.col_values(3, 1))
        # sheet页第三列数据从第二行开始做切片展示(字典列表)，两种方法都可以，第二种写法不包含结尾行
        print(sheet3.col_slice(3, 1))
        print(sheet3.col_slice(3, 1, 9))
        # 获取指定单元格内容
        print(sheet3.cell_value(5, 3))

    # 获取指定单元格内容方法
    def get_cell_value(self, name, rowx, colx):
        wb = xlrd.open_workbook(Excel_basedata_zs)
        sheet1 = wb.sheet_by_name('资产池注册表')
        sheet2 = wb.sheet_by_name('产品信息表')
        sheet3 = wb.sheet_by_name('资负信息注册(浙商)')
        if name == '资产池注册表':
            return sheet1.cell_value(rowx, colx)
        if name == '产品信息表':
            return sheet2.cell_value(rowx, colx)
        if name == '资负信息注册(浙商)':
            return sheet3.cell_value(rowx, colx)

    # 创建"一级菜单"xpath字典
    def first_menu(self, Excel_basedata):
        wb = xlrd.open_workbook(Excel_basedata)
        sheet = wb.sheet_by_name('一级菜单')
        # 创建空字典
        dat = {}
        for i in range(sheet.nrows):  # 循环读取"一级菜单"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分
            col1 = str(cells[0])  # 每行第一列数据赋值给col1
            col2 = str(cells[1])  # 每行第二列数据赋值给col2
            dat.setdefault(col1, col2)  # 用setdefault方法成对插入键值对
        return dat

    # 创建"二级菜单"xpath字典
    def second_menu(self, Excel_basedata):
        wb = xlrd.open_workbook(Excel_basedata)
        sheet = wb.sheet_by_name('二级菜单')
        # 创建空字典
        dat = {}
        for i in range(sheet.nrows):  # 循环读取"二级菜单"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分，中间的空白数据形成'': ''字典，不影响使用
            col0 = str(cells[0])  # 每行第一列数据赋值给col1
            col1 = str(cells[1])  # 每行第二列数据赋值给col1
            col2 = str(cells[2])  # 每行第三列数据赋值给col2
            dat.setdefault(f'{col0}-{col1}', col2)  # 用setdefault方法成对插入键值对
        return dat

    # 创建"二级菜单"映射一级菜单字典
    def secondmatch_menu(self):
        wb = xlrd.open_workbook(Excel_basedata_zs)
        sheet = wb.sheet_by_name('二级菜单')
        # 创建空字典
        dat = {}
        for i in range(sheet.nrows):  # 循环读取"二级菜单"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分，中间的空白数据形成'': ''字典，不影响使用
            col1 = str(cells[1])  # 每行第二列数据赋值给col1
            col2 = str(cells[0])  # 每行第一列数据赋值给col2
            dat.setdefault(col1, col2)  # 用setdefault方法成对插入键值对，setdefault方法只会存一次value，不支持更新
        return dat

    # 创建"资产池注册表"操作点xpath字典
    def registry_xpath(self):
        wb = xlrd.open_workbook(Excel_basedata_zs)
        sheet = wb.sheet_by_name('资产池注册表')
        # 创建空字典
        dat = {}
        for i in range(sheet.nrows):  # 循环读取"资产池注册表"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分
            col1 = str(cells[0])  # 每行第一列数据赋值给col1
            col2 = str(cells[1])  # 每行第二列数据赋值给col2
            dat.setdefault(col1, col2)  # 用setdefault方法成对插入键值对，setdefault方法只会存一次value，不支持更新
        return dat

    # 创建"资产池注册表"操作列表
    def registry_list(self):
        wb = xlrd.open_workbook(Excel_basedata_zs)
        sheet = wb.sheet_by_name('资产池注册表')
        # 获取"执行操作"列的数据列表
        dat = sheet.col_types(3, 1)  # 统计sheet中第四列第二行开始有值的单元格，有值的标记为1，空为0
        # print(dat.count(1))   # 统计"1"在列表中出现的次数
        return dat

    # 创建"产品信息表"操作点xpath字典
    def product_xpath(self):
        wb = xlrd.open_workbook(Excel_basedata_zs)
        sheet = wb.sheet_by_name('产品信息表')
        # 创建空字典
        dat = {}
        for i in range(sheet.nrows):  # 循环读取"产品信息表"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分
            col1 = str(cells[0])  # 每行第一列数据赋值给col1
            col2 = str(cells[1])  # 每行第二列数据赋值给col2
            dat.setdefault(col1, col2)  # 用setdefault方法成对插入键值对，setdefault方法只会存一次value，不支持更新
        return dat

    # 创建"产品信息表"操作列表
    def product_list(self):
        wb = xlrd.open_workbook(Excel_basedata_zs)
        sheet = wb.sheet_by_name('产品信息表')
        # 获取"执行操作"列的数据列表
        dat = sheet.col_types(3, 1)
        return dat

    # 创建"资负信息注册(浙商)"操作点xpath字典
    def registration_xpath(self):
        wb = xlrd.open_workbook(Excel_basedata_zs)
        sheet = wb.sheet_by_name('资负信息注册(浙商)')
        # 创建空字典
        dat = {}
        for i in range(sheet.nrows):  # 循环读取"资负信息注册(浙商)"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分
            col1 = str(cells[0])  # 每行第一列数据赋值给col1
            col2 = str(cells[1])  # 每行第二列数据赋值给col2
            dat.setdefault(col1, col2)  # 用setdefault方法成对插入键值对，setdefault方法只会存一次value，不支持更新
        return dat

    # 创建"估值表"操作点xpath字典
    def valuation_xpath(self):
        wb = xlrd.open_workbook(Excel_basedata_zs)
        sheet = wb.sheet_by_name('估值表')
        # 创建空字典
        dat = {}
        for i in range(sheet.nrows):  # 循环读取"估值表"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分
            col1 = str(cells[0])  # 每行第一列数据赋值给col1
            col2 = str(cells[1])  # 每行第二列数据赋值给col2
            dat.setdefault(col1, col2)  # 用setdefault方法成对插入键值对，setdefault方法只会存一次value，不支持更新
        return dat

    # 创建"表1-1产品募集余额统计表"操作点xpath字典
    def product_remain_xpath(self):
        wb = xlrd.open_workbook(Excel_basedata_zs)
        sheet = wb.sheet_by_name('表1-1产品募集余额统计表')
        # 创建空字典
        dat = {}
        for i in range(sheet.nrows):  # 循环读取"表1-1产品募集余额统计表"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分
            col1 = str(cells[0])  # 每行第一列数据赋值给col1
            col2 = str(cells[1])  # 每行第二列数据赋值给col2
            dat.setdefault(col1, col2)  # 用setdefault方法成对插入键值对，setdefault方法只会存一次value，不支持更新
        return dat

    # 创建sheet页对应操作点-xpath字典
    def sheet_xpath_dic(self, Excel_basedata, sheet_name):
        wb = xlrd.open_workbook(Excel_basedata)
        sheet = wb.sheet_by_name(sheet_name)
        # 创建空字典
        dat = {}
        for i in range(sheet.nrows):  # 循环读取"sheet_name"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分
            col1 = str(cells[0])  # 每行第一列数据赋值给col1
            col2 = str(cells[1])  # 每行第二列数据赋值给col2
            dat.setdefault(col1, col2)  # 用setdefault方法成对插入键值对，setdefault方法只会存一次value，不支持更新
        return dat

    # 创建sheet页对应操作点-备注字典
    def sheet_remark_dic(self, Excel_basedata, sheet_name):
        wb = xlrd.open_workbook(Excel_basedata)
        sheet = wb.sheet_by_name(sheet_name)
        # 创建空字典
        dat = {}
        for i in range(sheet.nrows):  # 循环读取"sheet_name"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分
            col1 = str(cells[0])  # 每行第一列数据赋值给col1
            col2 = str(cells[4])  # 每行第五列数据赋值给col2
            dat.setdefault(col1, col2)  # 用setdefault方法成对插入键值对，setdefault方法只会存一次value，不支持更新
        return dat

    # 创建"用例编号"枚举项列表
    def code_list(self):
        # 读取excel,指定sheet页
        df = pd.DataFrame(pd.read_excel(Excel_custom, sheet_name=universal_sheet))
        # 获取"用例编号"枚举项
        code = list(set(df['用例编号']))
        code.sort()  # 将列表中的数据进行升序排列
        return code

    # 创建"用例编号"和"操作元素"映射列表
    def group_ele_list(self):
        wb = xlrd.open_workbook(Excel_custom)
        sheet = wb.sheet_by_name('Sheet1')
        # 创建空列表
        group_list = []
        for i in range(sheet.nrows):  # 循环读取"sheet1"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分
            data = [str(cells[1]), str(cells[5])]  # 取第二列和第六列数据生成列表
            group_list.append(data)  # 将列表数据循环插入group_list
        return group_list

    # 创建"用例编号"和"值"映射列表
    def group_value_list(self):
        wb = xlrd.open_workbook(Excel_custom)
        sheet = wb.sheet_by_name('Sheet1')
        # 创建空列表
        group_list = []
        for i in range(sheet.nrows):  # 循环读取"sheet1"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分
            data = [str(cells[1]), str(cells[8])]  # 取第二列和第九列数据生成列表
            group_list.append(data)  # 将列表数据循环插入group_list
        return group_list

    # 创建"用例编号"和"操作步骤"映射列表
    def group_step_list(self):
        wb = xlrd.open_workbook(Excel_custom)
        sheet = wb.sheet_by_name('Sheet1')
        # 创建空列表
        group_list = []
        for i in range(sheet.nrows):  # 循环读取"sheet1"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分
            data = [str(cells[1]), str(cells[7])]  # 取第二列和第八列数据生成列表
            group_list.append(data)  # 将列表数据循环插入group_list
        return group_list

    # 创建"用例编号"对应"操作元素"的映射字典
    def group_ele_dic(self):
        dat = {}  # 创建空字典
        a = self.group_ele_list()
        c = self.code_list()
        l = len(c)  # 读取数组长度
        for b in a:
            n = 0
            while n < l:
                if c[n] not in dat:
                    dat.setdefault(c[n], [])  # 将枚举项先插入字典生成key，value列表为空
                if c[n] == b[0]:
                    dat[c[n]].append(b[1])  # 将枚举项的映射值填入value列表
                n = n + 1
        return dat

    # 创建"用例编号"对应"值"的映射字典
    def group_value_dic(self):
        dat = {}  # 创建空字典
        a = self.group_value_list()
        c = self.code_list()
        l = len(c)  # 读取数组长度
        for b in a:
            n = 0
            while n < l:
                if c[n] not in dat:
                    dat.setdefault(c[n], [])  # 将枚举项先插入字典生成key，value列表为空
                if c[n] == b[0]:
                    dat[c[n]].append(b[1])  # 将枚举项的映射值填入value列表
                n = n + 1
        return dat

    # 创建"用例编号"对应"操作步骤"的映射字典
    def group_step_dic(self):
        dat = {}  # 创建空字典
        a = self.group_step_list()
        c = self.code_list()
        l = len(c)  # 读取数组长度
        for b in a:
            n = 0
            while n < l:
                if c[n] not in dat:
                    dat.setdefault(c[n], [])  # 将枚举项先插入字典生成key，value列表为空
                if c[n] == b[0]:
                    dat[c[n]].append(b[1])  # 将枚举项的映射值填入value列表
                n = n + 1
        return dat

    # 通过"用例编号"获取一二级菜单xpath
    def match_menu(self, code):
        a = self.group_ele_dic()
        b = self.first_menu(Excel_basedata_zs)
        c = self.second_menu(Excel_basedata_zs)
        first_menu = a.get(code)[0]
        second_menu = a.get(code)[1]
        first_menu_xpath = b.get(first_menu)
        second_menu_xpath = c.get(f'{first_menu}-{second_menu}')
        return [first_menu_xpath, second_menu_xpath]

    # 通过"用例编号"获取操作元素和值的列表(模拟操作)
    def match_step(self, code):
        a = self.group_ele_dic()
        b = self.group_value_dic()
        c = len(a.get(code))  # "操作元素"最少是四个
        n = 3
        data = []
        while n < c:
            data.append([a.get(code)[n], b.get(code)[n]])
            n = n + 1
        return data

    # 通过"用例编号"获取操作元素和值的列表(流程自动化)
    def match_step2(self, code):
        a = self.group_ele_dic()
        b = self.group_value_dic()
        c = len(a.get(code))  # "操作元素"从第二行开始
        n = 1
        data = []
        while n < c:
            data.append([a.get(code)[n], b.get(code)[n]])
            n = n + 1
        return data

    # 通过"用例编号"创建操作元素和值的字典(流程自动化)
    def match_step_dic(self, code):
        a = self.match_step2(code)
        l = len(a)
        n = 0
        dat = {}
        while n < l:
            dat.setdefault(a[n][0], a[n][1])
            n = n + 1
        return dat

    # 创建"用例编号"对应"用例目的"的映射字典
    def group_goal_dic(self):
        wb = xlrd.open_workbook(Excel_custom)
        sheet = wb.sheet_by_name(universal_sheet)
        # 创建空字典
        dat = {}
        for i in range(sheet.nrows):  # 循环读取"sheet1"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分
            col1 = str(cells[1])  # 每行第二列数据赋值给col1
            col2 = str(cells[3])  # 每行第四列数据赋值给col2
            dat.setdefault(col1, col2)  # 用setdefault方法成对插入键值对，setdefault方法只会存一次value，不支持更新
        return dat

    # 筛选列表中的校验点
    def checkpoint_list(self, Excel_basedata, sheetname):
        a = self.sheet_list(Excel_basedata, sheetname)
        l = len(a)
        n = 0
        x = []
        while n < l:
            b = a[n].__contains__('-')
            if b:
                x.append(a[n])
            n = n + 1
        return x

    # 筛选列表中的校验点2.0
    def checkpoint_list2(self, Excel_basedata, sheetname):
        a = self.sheet_list(Excel_basedata, sheetname)
        l = len(a)
        n = 0
        x = []
        while n < l:
            b = a[n].__contains__('=')
            if b:
                x.append(a[n])
            n = n + 1
        return x

    # 筛选字典中的校验点
    def checkpoint_dic(self, Excel_basedata, sheetname):
        a = self.sheet_list(Excel_basedata, sheetname)
        b = self.sheet_xpath_dic(Excel_basedata, sheetname)
        l = len(a)
        n = 0
        x = {}
        while n < l:
            c = a[n].__contains__('-')
            if c:
                x.setdefault(a[n], b.get(a[n]))
            n = n + 1
        return x

    # 筛选字典中的校验点2.0
    def checkpoint_dic2(self, Excel_basedata, sheetname):
        a = self.sheet_list(Excel_basedata, sheetname)
        b = self.sheet_xpath_dic(Excel_basedata, sheetname)
        l = len(a)
        n = 0
        x = {}
        while n < l:
            c = a[n].__contains__('=')
            if c:
                x.setdefault(a[n], b.get(a[n]))
            n = n + 1
        return x

    # 筛选列表中的拼接点
    def splicing_list(self, Excel_basedata, sheetname):
        a = self.sheet_list(Excel_basedata, sheetname)
        l = len(a)
        n = 0
        x = []
        while n < l:
            b = a[n].__contains__('+')
            if b:
                x.append(a[n].split('+')[0])
            n = n + 1
        return x

    # 通过拼接点列表生成字典-第一列
    def splicing_dic(self, Excel_basedata, sheetname, low, page, h):  # 当页行数，当前页数，单页最大行数
        a = self.splicing_list(Excel_basedata, sheetname)
        b = len(a)
        c = low
        d = page - 1
        m = 0
        x = {}
        while m < b:
            n = 0  # 子循环的初始参数定义需要写在循环内，一次循环结束后重置成初始值，不然一次子循环后即满足条件结束整个循环
            while n < c:
                x.setdefault(f'{a[m]}-{d * h + n + 1}', (n + 1, m + 1))
                n = n + 1
            m = m + 1
        return x

    # 通过拼接点列表生成字典-第二列
    def splicing_dic2(self, Excel_basedata, sheetname, low):
        a = self.splicing_list(Excel_basedata, sheetname)
        b = len(a)
        c = low
        m = 0
        x = {}
        while m < b:
            n = 0  # 子循环的初始参数定义需要写在循环内，一次循环结束后重置成初始值，不然一次子循环后即满足条件结束整个循环
            while n < c:
                x.setdefault(f'{a[m]}-{n + 1}', (n + 1, m + 2))
                n = n + 1
            m = m + 1
        return x

    # 通过备注筛选出支持的可操作点列表
    def operable_list(self, Excel_basedata, sheetname):
        a = self.sheet_remark_dic(Excel_basedata, sheetname)
        b = self.sheet_list(Excel_basedata, sheetname)
        l = len(b)
        n = 0
        x = []
        while n < l:
            c = a.get(b[n])
            if c not in ['暂不支持', '不需要填写', '备注']:
                x.append(b[n])
            n = n + 1
        return x

    # 通过备注和元素关键字精准筛选出枚举项列表 eg:['业务种类_银行间现券买入', '业务种类_银行间现券卖出']
    def enumeration_list(self, Excel_basedata, sheetname, element):
        a = self.sheet_remark_dic(Excel_basedata, sheetname)
        b = self.sheet_list(Excel_basedata, sheetname)
        l = len(b)
        n = 0
        x = []
        e = element.__contains__('_')
        if e:
            element = element.split('_')[1]  # 如果是弹窗中的字段，用_分隔，取后半段
        while n < l:
            c = a.get(b[n])
            if c in ['不需要填写']:
                d = b[n].__contains__(f'{element}_')
                if d:
                    x.append(b[n])
            n = n + 1
        return x

    # 通过备注和元素关键字精准筛选出枚举项列表2.0 eg:['银行间现券买入', '银行间现券卖出']
    def enumeration_list2(self, Excel_basedata, sheetname, element):
        a = self.sheet_remark_dic(Excel_basedata, sheetname)
        b = self.sheet_list(Excel_basedata, sheetname)
        l = len(b)
        n = 0
        x = []
        e = element.__contains__('_')
        if e:
            element = element.split('_')[1]  # 如果是弹窗中的字段，用_分隔，取后半段
        while n < l:
            c = a.get(b[n])
            if c in ['不需要填写']:
                d = b[n].__contains__(f'{element}_')
                if d:
                    f = b[n].split('_')[1]
                    x.append(f)
            n = n + 1
        return x

    # 测试入口
    def test_value(self):
        a = self.splicing_dic(Excel_basedata_zs, '损益结转分录查询', 20, 6, 20)
        # print(a)
        b = self.splicing_dic(Excel_basedata_zs, '损益结转分录查询', 4, 5, 20)
        # print(b)
        c = self.enumeration_list2(Excel_basedata_zs, '产品报备管理', '高级查询_产品投资性质')
        # print(c)
        d = self.splicing_dic2(Excel_basedata_zs, '损益结转分录查询', 20)
        # print(d)
        e = self.match_step_dic('temp70')
        print(e)
