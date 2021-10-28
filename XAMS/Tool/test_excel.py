# 封装excel读取、生成字典等公共方法
# 1、读取Excel表数据
# 2、把数据作为参数传给后面的函数
# 3、后面的函数循环读取参数执行操作
import pandas as pd
import xlrd

from XAMS.Tool.conftest import Excel_basedata, Excel_custom


class TestExcel:
    # 定义初始化参数方法
    # def __init__(self, Excel_basedata):
    #     self.Excel_basedata = Excel_basedata

    # 定义获取单列数据,并将数据存入列表[]的方法
    def test_list(self):
        # wb = xlrd.open_workbook_xls()
        # 打开excel文件
        wb = xlrd.open_workbook(Excel_basedata)
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

    # 定义获取整行数据，并将数据存入字典{}的方法
    def test_dic(self):
        # 打开excel文件
        wb = xlrd.open_workbook(Excel_basedata)
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
        wb = xlrd.open_workbook(Excel_basedata)
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
    def first_menu(self):
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
    def second_menu(self):
        wb = xlrd.open_workbook(Excel_basedata)
        sheet = wb.sheet_by_name('二级菜单')
        # 创建空字典
        dat = {}
        for i in range(sheet.nrows):  # 循环读取"二级菜单"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分，中间的空白数据形成'': ''字典，不影响使用
            col1 = str(cells[1])  # 每行第二列数据赋值给col1
            col2 = str(cells[2])  # 每行第三列数据赋值给col2
            dat.setdefault(col1, col2)  # 用setdefault方法成对插入键值对
        return dat

    # 创建"二级菜单"映射一级菜单字典
    def secondmatch_menu(self):
        wb = xlrd.open_workbook(Excel_basedata)
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
        wb = xlrd.open_workbook(Excel_basedata)
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
        wb = xlrd.open_workbook(Excel_basedata)
        sheet = wb.sheet_by_name('资产池注册表')
        # 获取"执行操作"列的数据列表
        dat = sheet.col_types(3, 1)  # 统计sheet中第四列第二行开始有值的单元格，有值的标记为1，空为0
        # print(dat.count(1))   # 统计"1"在列表中出现的次数
        return dat

    # 创建"产品信息表"操作点xpath字典
    def product_xpath(self):
        wb = xlrd.open_workbook(Excel_basedata)
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
        wb = xlrd.open_workbook(Excel_basedata)
        sheet = wb.sheet_by_name('产品信息表')
        # 获取"执行操作"列的数据列表
        dat = sheet.col_types(3, 1)
        return dat

    # 创建"资负信息注册(浙商)"操作点xpath字典
    def registration_xpath(self):
        wb = xlrd.open_workbook(Excel_basedata)
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
        wb = xlrd.open_workbook(Excel_basedata)
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

    # 创建"用例编号"枚举项列表
    def code_list(self):
        # 读取excel
        df = pd.DataFrame(pd.read_excel(Excel_custom))
        # 获取"用例编号"枚举项
        code = list(set(df['用例编号']))
        code.sort()  # 将列表中的数据进行升序排列
        return code

    # 创建"用例编号"和"操作元素"映射列表
    def group_list(self):
        wb = xlrd.open_workbook(Excel_custom)
        sheet = wb.sheet_by_name('Sheet1')
        # 创建空列表
        group_list = []
        for i in range(sheet.nrows):  # 循环读取"sheet1"的数据（每次读取一行数据）
            cells = sheet.row_values(i)  # 每行数据赋值给cells
            # 根据每列的数据类型进行拆分
            data = [str(cells[1]), str(cells[4])]  # 取第二列和第五列数据生成列表
            group_list.append(data)  # 讲列表数据循环插入group_list
        return group_list

    # 创建"用例编号"对应"操作元素"的映射字典
    def group_dic(self):
        # 创建空字典
        dat = {}
        # 创建空列表
        data = []
        a = self.group_list()
        c = self.code_list()
        l = len(c)
        for b in a:
            n = 0
            while n <= l - 1:
                if c[n] == b[0]:
                    data.append(b[1])  # 将根据枚举项的映射值填入列表
                    dat.setdefault(c[n], data)  # 将枚举项:映射值列表作为key:value插入字典
                    n = n + 1
        return dat

    # 创建"操作元素"
    # 测试入口
    def test_value(self):
        # a = self.group_dic()  # 调用test_list方法获取整列数据
        # print(a)  # 返回整个函数的值
        # for b in a:  # 循环读取a变量list
        #     print(b)
        c = self.group_list()
        # print(c)
        # print(len(c))
        # print(c[1])
        # print(c.count(1))
        for d in c:
            # print(d)
            if d[0] == 'temp01':
                print(d[1])
        # print(a.get('temp01'))  # 通过key获取value
