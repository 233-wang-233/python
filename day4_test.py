"""
判断一个数是不是素数

Version: 0.1
Author: 233-wang-233
"""
def is_prime(num):
    for factor in range(2,num):
        if num%factor==0:
            return False
    return  True if num!=1 else False
"""
实现计算求最大公约数和最小公倍数的函数

Version: 0.1
Author: 233-wang-233
"""
def gcd(x,y):
    '''求最大公约数'''
    (x,y)=(y,x)if x>y else(x,y)
    for factor in range(x,0,-1):
        if x%factor==0 and y%factor==0:
            return factor
def lcm(x,y):
    return x*y//gcd(x,y)
#可以使用global关键字来指示foo函数中的变量a来自于全局作用域