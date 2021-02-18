#os的用法
import  os
print(os.getcwd() )     #获取当前路径

print(os.path.exists("b"))      #检查目录是否存在
if not os.path.exists("b"):
    os.mkdir("b")       #创建b目录
if os.path.exists("b/test.txt"):
    os.remove("b/test.txt")     #文件存在，先删除；remove命令可以删除文件和文件夹
if not os.path.exists("b/test.txt"):
    x = open("b/test.txt", "w")     #定义创建文件的方法x,并赋予write的权限
    x.write("hello, os using")
    x.close()

#time的用法
import time

print(time.asctime())     #英文格式时间
print(time.time())        #获取时间戳，秒数
print(time.localtime())     #tuple格式时间
print(time.strftime("%Y-%m-%d %H:%M:%S"))      #自定义格式时间

# 获取两天前的时间
now_timestamp=time.time()       #获取当前秒数
two_day_timestamp=time.time()- 60*60*24*2       #计算两天前的秒数
time_tuple=time.localtime(two_day_timestamp)        #两天前的秒数转化为tuple格式时间
print(time.strftime("%Y年%m月%d日 %H:%M:%S", time_tuple))      #tuple格式时间转化为自己想要的格式的时间

#urllib的用法
import urllib.request
response:object=urllib.request.urlopen('http://www.baidu.com')
print(response.status)
print(response.read())
print(response.headers)

#math库的用法 数学计算常用
#math.ceil(x) 返回大于等于参数x的最小整数
#math.floor(x) 返回小于等于参数x的最大整数
#math.sqrt(x) 平方根
import math

print(math.ceil(12.6156))
print(math.floor(-1515.1))
print(math.sqrt(16))
print(math.exp(5))