try:
    num1=int(input("请输入一个除数"))
    num2=int(input("请输入一个被除数"))
    print(num1/num2)
except ZeroDivisionError:     #调用try方法，一定要在末尾跟上except
    print("被除数不能为0")
except ValueError:            #根据报错的原因不同，自动寻找对应的报错来执行输出语句
    print("请输入数值型整数")
except:                       #若报错的原因未定义，则找到except:，若无，则直接给出报错信息
    print("发生甚么事了")
finally:                      #不管执行的结果是什么，最终都会执行finally:后的语句
    print("吃不下了，别送了")
