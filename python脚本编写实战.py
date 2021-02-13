# 变量和函数
# 1、python 允许在模块里定义 变量和方法的
# 2、函数里是可以调用外部的变量
# 3、函数里不允许改变外部变量
# 4、把外部变量设置为global 全局的，就可以改变它
# 5、通过 id() 方法可以打印对象的内存地址
# 6、方法默认返回值 是None

# from … import 与 import 区别
# 1、 from…import 是复制了一份到本地
# 2、import … 是引用了变量的地址

# pycharm 常用的快捷键
# 常用快捷键
# 格式化 alt + ctrl + L
# 导入 alt + 回车
# 复制当前行 ctrl +d
# 查看源代码 ctrl + 鼠标左键
# 注释，多行注释 ctrl + /
# 查找，替换 ctrl+f ,ctrl+r

class House:
    # 静态属性 -> 类变量，在类之中，方法之外的定义
    door = "red"
    floor = "white"

    # 构造方法，在类实例化的时候自动执行
    def __init__(self, bed):
        self.bed = bed  # 未定义，需要在实例化时初始化bed参数
        self.kitchen = "厨房"  # 已定义，不需要实例化时初始化kitchen参数

    # 动态方法
    def sleep(self):
        # 普通变量->在类之中，方法之中，并且前面没有self. 开头
        bed = "席梦思"
        print(f"在房子里可以躺在{self.bed}睡觉")  # {self.bed}为调用方法变量，若为{bed}为调用普通变量

    def cook(self):
        print(f"在房子的{self.kitchen}里可以做饭")


if __name__ == '__main__':
    # 实例化->变量=类()
    north_house = House(bed="雅兰")
    china_house = House(bed="喜临门")
    # 通过实例对象调用类属性
    north_house.door = "white"
    print(north_house.door)
    print(House.door)

    north_house.sleep()
    china_house.sleep()
    print(north_house.kitchen)
    china_house.cook()
