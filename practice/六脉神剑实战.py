'''
六脉神剑实战
a=易方达蓝筹精选混合 005827
b=兴全合宜混合(LOF)A 163417
c=景顺长城新兴成长混合 260108
d=汇添富创新药主题混合 006113
e=嘉实新能源新材料股票A 003984
f=汇添富价值精选混合A 519069
g=中欧盛世成长混合C 004233
'''

def func2021(s=35000, a=10500, b=5250, c=7000, d=5250, e=5250, f=1750, g=0):
    print('"易方达蓝筹精选混合 005827" %d %.2f%%' % (a, a / s * 100))  # 格式化输出方法
    print('"兴全合宜混合(LOF)A 163417" %d %.2f%%' % (b, b / s * 100))
    print('"景顺长城新兴成长混合 260108" %d %.2f%%' % (c, c / s * 100))
    print('"汇添富创新药主题混合 006113" %d %.2f%%' % (d, d / s * 100))
    print('"嘉实新能源新材料股票A 003984" %d %.2f%%' % (e, e / s * 100))
    print('"汇添富价值精选混合A 519069" %d %.2f%%' % (f, f / s * 100))
    print('"中欧盛世成长混合C 004233" %d %.2f%%' % (g, g / s * 100))
    return ((a + b + c + d + e + f + g) / s)


print('投资比例 {:.2%}'.format(func2021(a=5000, b=5000, g=5750)))  # str.format输出方法
print(f"投资比例 {func2021()}")  # 最常用字面量插值
print("投资比例", func2021())
