"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
"""
from python_homework_210122_1 import Animal


class Cat(Animal):
    hair = "短毛"

    def __init__(self):
        super().__init__("猫", "蓝", 2, 'female')

    def catching_mice(self):
        print(f"我是一只{self.name}，我会抓老鼠")

    def call(self):
        print("喵喵叫")


bulecat = Cat()
print(f"我是一只{bulecat.age}岁的{bulecat.hair}{bulecat.color}{bulecat.name}")
bulecat.catching_mice()
bulecat.call()
bulecat.run()
