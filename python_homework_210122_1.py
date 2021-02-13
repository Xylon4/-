"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
"""


class Animal:
    name = "动物类"
    color = "黑白"
    age = 3
    gender = 'male'

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def call(self):
        print("我能发出轻柔的叫声")

    def run(self):
        print("我能在丛林里奔跑")


if __name__ == '__main__':
    panda = Animal("大熊猫", "黑白", 1, 'female')
    print(f"我是一只{panda.age}岁的{panda.color}{panda.name} ")
    panda.call()
    panda.run()
