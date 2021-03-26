# 蜗牛抽奖活动碎片计算
# def func1(a=120,b=150,c=180,d=200):
#     return (2*a+2*b+2*c+d)
# print(func1())
# print(3*func1()+750+900+900+250)
# print(500+1000+1500+3000)

# 蜗牛祭坛活动碎片计算
def func1(a=150, b=160, c=180, d=210, e=250):
    x = 2 * a + b + c + d + e
    print(f"单轮获取碎片为{x}")
    return (x)


y = 5 * func1() + 400 * 4 + 1200
print(f"三轮加速+宝箱能获得的碎片数量{y}")
z = 500 + 1000 + 1500 + 3000 + 5000
print(f"满奖励需要的碎片数为{z}")
w = 240 * 3
m = w / 24
print(f"三轮加速需要的时间为{w}小时，合{m}天")
n = 47 * 2 + 48 * 2 + 5 + 31 * 24
if n > w and n < z:
    print("这次可以拿四挡奖励")
elif n > z:
    print("这次可以拿满奖励")
else:
    print("这次不行，再攒一会")

# c = "asdhgijom4iovnobhudiasb"
# print(set(c))
# print(type(c))


# import sys
# print(sys.path)

# class Exception:
#     def __init__(self,value1,value2):
#         self.value1=value1
#         self.value2=value2
#
#
# my=Exception(1,2)
# print(my.value1)
# import yaml
#
# with open("./calc.yaml") as f:
#     datas = yaml.safe_load(f)['add']
#     add_datas = datas['datas']
#     print(add_datas)
#     myid = datas['myid']
#     print(myid)
