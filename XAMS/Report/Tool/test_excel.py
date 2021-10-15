# 1、读取Excel表数据
# 2、把数据作为参数传给后面的函数
# 3、后面的函数循环读取参数执行操作
import xlrd

from XAMS.basepage_XAMS import BasePageFsfa


class TestExcel(BasePageFsfa):
    def test_excel(self):
        # wb = xlrd.open_workbook_xls()
        # 打开Excel文件
        wb = xlrd.open_workbook('C:\Users/\/1\Desktop\自动化读取报表.xlsx')
        # 获取sheet，通过Excel表哥名称(rank)获取工作表
        sheet = wb.sheet_by_name('一级菜单')
        # 创建空list
        dat = []
        for a in range(sheet.nrows):  # 循环读取表格内容（每次读取一行数据）
            cells = sheet.row_values(a)  # 每行数据赋值给cells
            data = int(cells[0])  # 因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
            dat.append(data)  # 把每次循环读取的数据插入到list
        return dat
    a = test_excel()  # 返回整个函数的值
    print(a)


    # def test(a):  # a变量传入
    #     for b in a:  # 循环读取a变量list
    #         print(b)
    #
    # test(a)