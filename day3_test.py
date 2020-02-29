'''
生成斐波那契数列的前20个数

version:0.1
autor:233-wang-233
'''
# import array as np
# a=0
# b=1
# for i in range(1,20):
#     a,b=b,a+b#############右边的 a, a+b 会返回一个tuple 然后这个左边的a, b 会分别赋值为这个tuple里的第一个和第二个
#     print(a)
'''
找出10000以内的完美数

version:0.1
autor:233-wang-233
'''
import math

# for i in range(2,10000):
#     num = 0
#     for j in range(1,i-1):
#         m=i%j
#         if m==0:
#             num+=j
#     if num==i:
#         print(i)


# import math
#
# for num in range(1, 10000):
#     result = 0
#     for factor in range(1, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             result += factor
#             if factor > 1 and num // factor != factor:
#                 result += num // factor
#     if result == num:
#         print(num)

'''
输出100以内的素数

version:0.1
autor:233-wang-233
'''
print(1)
for i in range(2,100):
    is_prime=True
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i)
