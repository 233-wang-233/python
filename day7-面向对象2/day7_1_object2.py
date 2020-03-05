'''
__slots__魔法
python作为一个动态语言，允许我们给程序运行时给对象绑定新的属性或方法
可以通过在类中定义__slots__变量来进行限定，其只对当前类的对象生效。对子类并不起作用
'''
class Person(object):

    #限定Person对象只能绑定_name,_age,和_gender属性
    __slots__ = ('_name','_age','_gender')

    def __init__(self,name,age):
        self._name=name
        self._age=age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age=age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

def main():
    person=Person('王小刀',22)
    person.play()
    person._gender='男'
    #print(person._gender)
if __name__=='__main__':
    main()
