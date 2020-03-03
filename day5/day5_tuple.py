#定义元组
t=('233-wang-233',38,True,'河南周口')
print(t)
#获得元组中的值
print(t[0])
print(t[3])
#遍历元组中的值
for member in t:
    print(member)
# 重新给元组赋值
# t[0] = '王大锤'  # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t=('王大锤',20,True,'云南昆明')
print(t)
#将元组转化为列表
person=list(t)
print(person)
#列表是可以修改它的元素的
person[0]='李小龙'
person[1]=25
print(person)
#将其转化为元组
fruits_list=['apple','banana','orange']
fruits_tuple=tuple(fruits_list)
print(fruits_tuple)