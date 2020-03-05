#面向对象进阶
'''
通过属性命名以_打头表明该属性受保护，不建议外界直接访问
getter（访问器）
setter（修改器）
@property包装器包装getter和setter
'''
class person(object):
    def __init__(self,name,age):
        self._name=name
        self._age=age

    #访问器 -getter方法
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return  self._age

    #修改器 -setter方法
    @age.setter
    def age(self,age):
        self._age=age

    def play(self):
        if self._age<=16:
            print('%s正在玩飞行棋。'%self._name)
        else:
            print('%s正在玩斗地主。' % self._name)

def main():
    Person=person('王小刀',12)
    Person.play()
    Person.age=22
    Person.play()
if __name__=='__main__':
    main()
