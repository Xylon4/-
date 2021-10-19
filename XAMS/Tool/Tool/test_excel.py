# 1、读取Excel表数据
# 2、把数据作为参数传给后面的函数
# 3、后面的函数循环读取参数执行操作
import xlrd


class TestExcel():
    # 定义获取单列数据,并将数据存入列表[]
    def test_list(self):
        # wb = xlrd.open_workbook_xls()
        # 打开excel文件
        wb = xlrd.open_workbook(r'C:\Users\1\Desktop\自动化读取报表.xlsx')
        # 获取sheet，通过Excel表格名称(rank)获取工作表
        sheet = wb.sheet_by_name('一级菜单')
        # 创建空list
        dat = []
        for a in range(sheet.nrows):  # 循环读取表格内容（每次读取一行数据）
            cells = sheet.row_values(a)  # 每行数据赋值给cells
            # 根据数据类型选择合适的转换类型num选用（int、float、bool、complex）中文选用(str)
            data = str(cells[0])  # 因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
            dat.append(data)  # 把每次循环读取的数据插入到list
        return dat

    # 取值入口
    def test_value(self):
        a = self.test_list()  # 调用test_list方法获取整列数据
        print(a)  # 返回整个函数的值
        for b in a:  # 循环读取a变量list
            print(b)

    # 定义获取整行数据，并将数据存入元组()
    def test_tuple(self):
        # 打开excel文件
        wb = xlrd.open_workbook(r'C:\Users\1\Desktop\自动化读取报表.xlsx')
        # 获取sheet页信息
        # print(wb.sheets())
        # print(wb.sheet_names())
        # 打印sheet的名称，行数，列数
        sheet1 = wb.sheet_by_name('一级菜单')
        sheet2 = wb.sheet_by_name('二级菜单')
        sheet3 = wb.sheet_by_name('资产池注册表')
        sheet4 = wb.sheet_by_name('产品信息表')
        sheet5 = wb.sheet_by_name('资负信息注册(浙商)')
        # print(sheet1.name, sheet1.nrows, sheet1.ncols)
        # print(sheet2.name, sheet2.nrows, sheet2.ncols)
        # 获取整行或整列的值
        rows2 = sheet2.row_values(8)
        cols = sheet2.col_values(1)
        print(sheet2.row_values(8))
        print(sheet2.row_values(9))
        print(sheet2.row_values(10))
        print(sheet2.col_values(1))
