# 正常文件读取操作
# f = open('data.py')
# print(f.readable())  # 判断文件是否可读
# print(f.readline())  # 逐行依次读取
# print(f.readline())
# print(f.readline())
# print(f.read())  # 读取全部内容，大数据会影响性能
# print(f.readlines())  # 读取剩余内容，并显示在一行，若无内容显示为空，并用【】
# f.close()

# 最优文件读取
# with 语句块，可以将文件打开后，操作完毕，自动关闭这个文件
# 图片读取需要使用rb权限 读取二进制的格式
# 正常的文本，可以使用rt，也就是默认读取格式
with open('data.py', 'rt')  as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break
