import xlrd, time
from tkinter import *
from googletrans import Translator
import tkinter.messagebox
import tkinter.filedialog
from openpyxl.utils import get_column_letter


class Comp:
    def __init__(self, master):
        self.master = master

    # 初始化界面显示标签
    def label(self, properties, padx=3, pady=2, ipadx=5, ipady=1):  # padx组件之间左右横向外部间隔，ipadx组件左右横向内部间隔
        for name, x, y in properties:
            self.la = Label(self.master, text=name)
            self.la.grid(row=x, column=y, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)

    # 初始化界面显示按钮
    def button(self, properties, padx=1, pady=2, ipadx=2, ipady=1):
        for text, x, y, command in properties:
            self.bu = Button(self.master, text=text, command=command)
            self.bu.grid(row=x, column=y, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)


class Tr:
    def __init__(self):
        self.main = Tk()  # 创建窗口
        self.mainwindow = Comp(self.main)  # 传入标签和按钮定义信息
        self.main.geometry('454x400')  # 窗口大小
        self.main.title(u"Excel对比工具-xYlonA")  # 窗口标题
        self.main.resizable(width=False, height=False)  # 固定窗口大小不可调整

    # 对比excel内容部分
    def Compared(self, filename1, filename2, savefile):
        Logtime = time.strftime('%Y-%m-%d %H%M%S', time.localtime(time.time()))  # 记录时间
        with open(r"%s/%s.txt" % (savefile, Logtime), "w") as f:
            print("当前对比Excel：\n%s\n%s" % (filename1, filename2), file=f)
            print("\n对比结果如下：", file=f)

        book1 = xlrd.open_workbook(filename1, formatting_info=True)  # formatting_info=True参数不支持xlsx格式，需要另存为xls
        sheet1 = book1.sheet_by_index(0)

        book2 = xlrd.open_workbook(filename2, formatting_info=True)
        sheet2 = book2.sheet_by_index(0)

        rows = sheet1.nrows  # 最大行数
        cols = sheet1.ncols  # 最大列数

        # 判断两个excel行数和列数是否相等
        if sheet1.nrows != sheet2.nrows or sheet1.ncols != sheet2.ncols:
            with open(r"%s/%s.txt" % (savefile, Logtime), "a+") as f:
                print("两个excel获取到的最大行或列不相同,\n%s行数为：%s,列数为：%s\n%s行数为：%s,列数为：%s\n" % (
                    filename1, sheet1.nrows, sheet1.ncols, filename2, sheet2.nrows, sheet2.ncols), file=f)

        # 循环对比
        for row in range(0, rows):
            for col in range(0, cols):
                # 对比值
                e1 = sheet1.cell_value(row, col)
                e2 = sheet2.cell_value(row, col)
                column = get_column_letter(col + 1)
                if e1 != e2:
                    e1 = str(e1)
                    if (e1.split(".")[0]).isdigit() or e1.isdigit() or (e1.split('-')[-1]).split(".")[
                        -1].isdigit():
                        e1 = float(e1)
                        e2 = float(e2)
                        if e1 == e2:
                            with open(r"%s/%s.txt" % (savefile, Logtime), "a+") as f:
                                print(f"单元格(%s-%s),格式不同,分别为 {e1} {e2}" % (row + 1, column), file=f)
                        else:
                            with open(r"%s/%s.txt" % (savefile, Logtime), "a+") as f:
                                print(f"单元格(%s-%s),值不同,分别为 {e1} {e2}" % (row + 1, column), file=f)
                    else:
                        with open(r"%s/%s.txt" % (savefile, Logtime), "a+") as f:
                            print(f"单元格(%s-%s),值不同,分别为 {e1} {e2}" % (row + 1, column), file=f)

        with open(r"%s/%s.txt" % (savefile, Logtime), "a+") as f:
            print(f"\n***对比完成***\n{Logtime}", file=f)

    # 界面部分
    def interface(self):
        # 文本
        self.mainwindow.label([
            ("Excel路径一：", 0, 0),
            ("Excel路径二：", 1, 0),
            ("结果存放路径：", 2, 0)
        ], ipady=10, ipadx=8)

        path = StringVar()
        path1 = StringVar()
        savepath = StringVar()

        def selectPath():
            # 文件选择框
            path_ = tkinter.filedialog.askopenfilename(filetypes=[("", ".xls")])
            # path = StringVar() 配合使用，更新显示地址
            path.set(path_)
            # 选择文档的路径
            self.t = path_

        def selectPath1():
            # 文件选择框
            path1_ = tkinter.filedialog.askopenfilename(filetypes=[("", ".xls")])
            # path = StringVar() 配合使用，更新显示地址
            path1.set(path1_)
            # 选择文档的路径
            self.t1 = path1_

        def savePath():
            # 文件选择框
            savepath_ = tkinter.filedialog.askdirectory(initialdir='E:\Excel对比工具')
            # path = StringVar() 配合使用，更新显示地址
            savepath.set(savepath_)
            # 选择文档的路径
            self.t2 = savepath_

        def start():
            try:
                self.Compared(self.t, self.t1, self.t2)
                tkinter.messagebox.showinfo('提示', '对比成功！')
            except:
                tkinter.messagebox.showinfo('提示', '对比出错，请先正确选择路径或文件内容！')

        # 显示选择文件地址
        Label(self.main, width=35, height=3, wraplength=230, textvariable=path).grid(row=0, column=1, padx=8)
        Label(self.main, width=35, height=3, wraplength=230, textvariable=path1).grid(row=1, column=1, padx=8)
        Label(self.main, width=35, height=3, wraplength=230, textvariable=savepath).grid(row=2, column=1, padx=8)

        # 按钮
        self.mainwindow.button([
            ("选择", 0, 2, selectPath),
            ("选择", 1, 2, selectPath1),
            ("选择", 2, 2, savePath),
            ("开始对比", 3, 1, start)
        ], ipadx=8, ipady=1)

        self.main.mainloop()  # 接收操作系统发来的事件，然后把事件分发给各个控件和窗体


if __name__ == "__main__":
    t = Tr()
    t.interface()
