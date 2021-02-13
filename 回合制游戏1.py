"""
一个回合制游戏，每个角色都有hp和power,hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200.
定义一个fight方法：
my_hp=hp-enemy_power
enemy_final_hp=enemy_hp-my_power
两个hp进行对比，血量剩余多的人获胜
1.使用面向对象的实现一个回合制格斗游戏
2.使用面向对象的继承改造游戏
"""
from log_decorater import log_decorator

class Game:
    def __init__(self, my_hp, my_power, enemy_hp, enemy_power):
        # 初始化属性
        self.my_hp = my_hp
        self.my_power = my_power
        self.enemy_hp = enemy_hp
        self.enemy_power = enemy_power
        # 定义私有变量
        self.__secret = "secret"

    # 对打方法
    @log_decorator      #方法开始前，添加装饰器
    def fight(self):
        while True:
            # 我的剩余血量
            self.my_hp = self.my_hp - self.enemy_power
            # 敌人的剩余血量
            self.enemy_hp -= self.my_power  # -=和上面的效果相同
            print(f"我的血量：{self.my_hp} VS 敌人的血量：{self.enemy_hp}")
            # 胜负判断
            if self.my_hp <= 0:
                print("我输了")
                break
            if self.enemy_hp <= 0:
                print("我赢了")
                break

    # 定义休息方法
    def rest(self, rest_num):  # 循环外定义，所以调用时只执行一次
        self.rest_num = rest_num
        # self.__private_method()     #类中的公共方法可以调用私有方法
        print(f"老匹夫，敢不敢一杯酒后再战{self.rest_num}百回合")

    # 定义私有方法
    def __private_method(self):  # 双下划线开头命名，代表私有方法
        print(f"{self.__secret}")  # 私有方法中读取私有变量
        print("这是一个私有的方法")


if __name__ == '__main__':
    game = Game(1000, 200, 1000, 199)
    game.fight()
    game.rest("三")
    # 私有变量不能被对象调用
    # print(game.__secret())
    # #私有方法也不能被对象调用
    # print(game.__private_method(self))
