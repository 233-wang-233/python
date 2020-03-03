"""

Version: 0.1
Author: 233-wang-233
"""
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
#在\后面还可以跟一个八进制或者十六进制数来表示字符
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)
'''
我们可以使用+运算符来实现字符串的拼接，可以使用*运算符来重复一个字符串的内容，
可以使用in和not in来判断一个字符串是否包含另外一个字符串（成员运算），
我们也可以用[]和[:]运算符从字符串取出某个字符或某些字符（切片运算），
'''
s1='hello '*3
print(s1)
s2='world'
s1+=s2
# print(s1)
# print('ll'in s1)#True
# print('good'in s1)#False
# str2='abc123456'
# print(str2[2])
# print(str2[2:5])
# print(str2[2::2]) # c246
# print(str2[::2]) # ac246
# print(str2[::-1]) # 654321cba
# print(str2[-3:-1]) # 45

str1 = 'hello, world!'
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())

#用字符串提供的方法来完成字符串的格式
a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))
a, b = 5, 10
print(f'{a}*{b}={a*b}')

'''列表'''
print('*'*100)
list1=[1,3,5,7,100]
print(list1)
list2=['hello']*3
print(list2)
#计算列表的长度
print(len(list1))
#下标索引
print(list1[0])
print(list1[4])
print(list1[-1])
list1[2]=300
print(list1)
#通过循环遍历列表元素
for index in range(len(list1)):
    print(list1[index])
#通过for循环遍历列表元素
for elem in list1:
    print(elem)
#通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index,elem in enumerate(list1):
    print(index,elem)
word='如何从列表中移除元素'
print(word.center(60,'*'))
list1=[1,3,5,7,100]
#添加元素
list1.append(200)
list1.insert(1,400)
list1+=[1000,2000]
print(list1)
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1)
#从指定位置删除元素
list1.pop(0)
list1.pop(len(list1)-1)
print(list1)
list1.clear()


word='列表切片'
print(word.center(60,'*'))
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2) # apple strawberry waxberry
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4) # ['pitaya', 'pear']
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']


word='列表排序'
print(word.center(60,'*'))
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2=list1.sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3=sorted(list1,reversed=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4=sorted(list1,key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)

import sys
word='生成式和生成器'
print(word.center(60,'*'))
f=[x for x in range(1,10)]
print(f)
f=[x+y for x in 'ABCDE' for y in '1234567']
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f=[x**2 for x in range(1,1000)]
print(sys.getsizeof(f))# 查看对象占用内存的字节数

f=(x**2 for x in range(1,1000))#相比生成式生成器不占用存储数据的空间
print(sys.getsizeof(f))# 查看对象占用内存的字节数

