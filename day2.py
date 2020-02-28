'''
寻找水仙花数,水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，
例如：$1^3 + 5^3+ 3^3=153$。

version:0.1
autor:233-wang-233
'''
for num in range(100, 1000):
    low=num%10
    mid=num//10%10
    high=num//100
    if low**3+mid**3+high**3==num:
        print("%d是水仙花。"%num)

'''
正整数反转

version:0.1
autor:233-wang-233
'''
# num=int(input())
# reversed_num=0
# while num>0:
#     reversed_num=reversed_num*10+num%10
#     num//=10
# print(reversed_num)

'''
百钱百鸡问题

version:0.1
autor:233-wang-233
'''
for x in range(0,20):
    for y in range(0,33):
        if x*5+y*3+(100-x-y)*0.3==100:
            print('公鸡%d只;'%x,'母鸡%d只;'%y,'小鸡%d只;'%(100-y-x))

'''
CRAPS赌博游戏，假定玩家有1000元赌注，
游戏结束的条件是玩家输光所有的赌注

version:0.1
autor:233-wang-233
'''
from random import randint
money =1000
while money>0:
    print("你的总资产为：",money)
    needs_go_on=False
    while True:
        debt=int(input("请下注:"))
        if 0<debt<=money:
            break
    first = randint(1, 6)+randint(1,6)#randint随机生成数字
    print("玩家摇出的色子数目为：",first)
    if first==7 or first==11:
        print("YOU WIN!")
        money+=debt
    elif first==2 or first==3 or first==12:
        print("YOU LOST!")
        money-=debt
    else:
        needs_go_on=True
    while needs_go_on:
        needs_go_on=False
        current=randint(1, 6)+randint(1,6)
        print("玩家摇出的色子数目为：",current)
        if current==7:
            print("YOU WIN!")
            money+=debt
        elif current==first:
            print("YOU WIN!")
            money+=debt
        else:
            needs_go_on=True
print('你破产了！')



