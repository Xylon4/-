# print("hello pycharm")


# #打印a
# a=1
# print(a)
#
# A1=2
# print(A1)

# A2="123456789"
# print(A2)
# print(A2[0:6:2])
# print(A2[0:6])
# print(A2[0:5:2])
# print(A2[0:7:2])
# print(A2[6])
# print(A2[7])


# A3=r"12351\n"
# print(A3)
#
# A4="12156" "ASDAD"
# print(A4)
#
# A5="5615"
# A6="1161"
# print(A5+A6)

# a=1
# if a >0:
#     print("a=0")
# elif a <0:
#     print("我很帅")
# elif a==0:
#     print("我很高")

# result=0
# for i in range(2,101,2):
#     result =result+i
#     print(result)

# flag=1
# while(flag):print('欢迎来到召唤师峡谷')
# print("python测试")

# import requests
#
# print(requests.post("http://www.baidu.com"))

import yaml

print(yaml.load("""
a:1
""", Loader=yaml.FullLoader))
