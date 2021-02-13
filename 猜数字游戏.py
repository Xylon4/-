import random
computer_numer=random.randint(1,100)
while True:
    person_number=int(input("请输入一个数字"))
    if person_number>100:
        print("当前输入的值过大,请重新输入")
    elif person_number<1:
        print("当前输入的值过小，请重新输入")
    elif person_number>computer_numer:
        print("小一点")
    elif person_number<computer_numer:
        print("大一点")
    elif person_number==computer_numer:
        print("猜对啦")
        break