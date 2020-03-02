"""
输入M和N计算C(M,N)

Version: 0.1
Author: 233-wang-233
"""
# m=int(input())
# n=int(input())
# fm=1
# #求m的阶乘
# for i in range(1,m+1):
#     fm*=i
# fn=1
# for i in range(1,n+1):
#     fn*=i
# fm_n=1
# for i in range(1,m-n+1):
#     fm_n*=i
# C=int(fm/(fn*fm_n))
# print(C)
'''
要写出高质量的代码首先要解决的就是重复代码的问题。对于上面的代码来说，
我们可以将计算阶乘的功能封装到一个称之为“函数”的功能模块中，
在需要计算阶乘的地方，我们只需要“调用”这个“函数”就可以了。
'''
'''
对以上代码重构
'''
# def factorial(num):#range不包括end
#     fn=1
#     for i in range(1, num+1):
#         fn *= i
#     return fn
# m=int(input())
# n=int(input())
# C=int(factorial(m)/(factorial(m)*factorial(m)))
# print(C)

# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
'''
用模块管理函数
'''
from model1 import foo
foo()
from model2 import foo
foo()

import model3