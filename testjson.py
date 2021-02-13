import json

#json 由字典和列表组成
data={
    "name":"jerry",
    "age":26,
    "gender":"female"
}

print(type(data))
data1 =json.dumps(data)      #通过dumps,将字典转化成字符型
print(data1)
print(type(data1))

data2 =json.loads(data1)     #通过loads，将字符型转化成字典
print(type(data2))
print(data2)