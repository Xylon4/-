"""
函数代码块以 def 关键字开头，后接函数名称和圆括号 ()。
冒号起始
注意缩进
圆括号中定义参数
函数说明——文档字符串
return[表达式]结束函数
选择性地返回一个值给调用方。
不带表达式的return或者不写return函数，相当于返回 none。
pycharm光标所在行使用 ctrl+d 快捷键复制一行
"""

#函数的定义
def func1(a,b,c,d):
    print("参数a",a)
    print("参数b",b)
    print("参数c",c)
    print("参数d",d)
    return(a+b+b+d)

#函数的调用

#位置参数，当未定义参数时，根据定义函数的参数顺序默认传入参数，注意参数不能缺少或者多余
func1(1, 2, 3, 4)    #只传参不输出
print(func1(1, 2, 3, 4))  #传参的同时return输出结果

#默认参数的使用
def func2(a=1,b=2,c=3,d=4):
    print("参数a", a)
    print("参数b", b)
    print("参数c", c)
    print("参数d", d)
    return(a+b*c/d)

print(func2(2,d=4,c=5))  #未传参时，使用默认值，传参后使用新的参数；其中2是位置参数，只能是首位定义参数，c=4和d=5的位置可以交换

#可以用lambda关键字来创建一个小的匿名函数，lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。在不常调用的情况下使用
func3 = lambda x,y: x*y
print(func3(1, 2))

def func4(x,y):
    return(x*y)
print(func4(1,2))    #这个函数定义+调用的效果和上面的lambda作用相同