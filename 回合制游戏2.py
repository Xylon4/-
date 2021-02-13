from 回合制游戏1 import Game  # 因为我的文件命名为中文，所以无法使用快捷键clt+enter导入


class Houyi(Game):
    '''
    后裔，后裔继承了Game的hp和power属性，并添加了护甲属性。
    重新定义另外一个defense属性:
    final_hp = hp + defense - enemy_power
    enemy_final_hp = enemy_hp - power
    两个hp进行对比，血量先为零的人输掉比赛
    '''

    def __init__(self):  # 重写后，部分属性未重定义，则需要继承父类属性
        self.defense = 100
        # spuer().方法用来继承父类属性
        super().__init__(1000, 200, 2000, 199)

    def fight(self):
        # 改造一下 my_hp的计算方法
        while True:
            # 我的剩余血量
            self.my_hp = self.my_hp + self.defense - self.enemy_power  # 添加护甲属性
            # 敌人的剩余血量
            self.enemy_hp -= self.my_power  # -=和上面的效果相同
            print(f"我的血量：{self.my_hp} VS 敌人的血量：{self.enemy_hp}")
            super().rest("五")  # 通过调用父类中的公共方法，间接使用父类中的私有方法和私有变量
            # 胜负判断
            if self.my_hp <= 0:
                print("惜败")
                break
            if self.enemy_hp <= 0:
                print("险胜，承让了")
                break


if __name__ == '__main__':
    houyi = Houyi()
    houyi.fight()
    # houyi.rest("六")     #通过调用父类中的公共方法，间接使用父类中的私有方法和私有变量
