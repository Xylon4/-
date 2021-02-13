# 创造一个人类
# 通过class关键字，定义一个类
class person:
    name = "humen"
    age = 0
    gender = 'male'
    weight = 0
    hight = 12

    # 构造方法，在类实例化的时候被调用
    def __init__(self, name, age, gender, weight, hight):  # 通过init初始化参数，引用时通过输入个性化变量来实现，不能缺少变量
        # self.变量名的方式，访问的问题，叫做实例变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.hight = hight

    # def set_param(self,name,age,gender,weight,hight):     #定义设置参数方法，仅能一共一次调用输入，一次结果输出
    #     self.name = name
    #     self.age = age
    #     self.gender = gender
    #     self.weight = weight
    #     self.hight = hight

    def set_age(self, age):  # 定义设置单一属性方法，比较土
        self.age = age

    @classmethod
    def eat(self):  # 定义方法，使用方法时会执行对应的语句
        print(f"{self.name} eating")
        print("我吃饱了")

    def play(self):
        print(f"{self.name} playing")
        print("我好开心啊")

    def swim(self):
        print(f"{self.name} swiming")
        print(f"我已经{self.age}岁了，可以下水游泳了")


zs = person("张飞", 60, "男", 175, 180)  # 类的实例化，使用class，括号中可以添加初始化参数，对应init方法
# zs.set_age(18)
# print(f"zs的年龄是{zs.age}岁")
# zs.set_param("张三",20,"male",120,175)
zs.eat()  # 实例名.方法 来使用
zs.play()
zs.swim()
print(f"张飞在{zs.age}多岁的年纪还能大口吃肉，大口饮酒,真了不起")
print(f"{zs.name}身高{zs.hight}，体重{zs.weight}，是个顶天立地的{zs.gender}子汉")

# 类变量和实例变量的区别
# 类变量是需要类来访问的，实例变量需要实例来访问
print(person.name)  # 输出类的默认值,所以是类变量
person.name = 'lisi'
print(person.name)  # 支持修改
# 类不能直接调用方法，而实例可以；或者在方法前添加 装饰器@classmethod来使用（添加一个生效一个）
person.eat()
# person.play()      #未添加装饰器@classmethod 不能使用

ls = person("李四", 12, "female", 90, 160)
print(ls.name)
print(f"{ls.name}")
