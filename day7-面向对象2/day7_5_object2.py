'''
通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，
当我们调用这个经过子类重写的方法时，
不同的子类对象会表现出不同的行为，这个就是多态
'''
from abc import ABCMeta,abstractmethod

class Pet(object,metaclass=ABCMeta):
    '''宠物'''
    def __init__(self,nickname):
        self._nickname=nickname

    @abstractmethod
    def make_voice(self):
        '''发出声音'''
        pass

class Dog(Pet):
    '''狗'''
    def make_voice(self):
        print('%s:汪汪汪..'%self._nickname)

class Cat(Pet):
    '''mao'''
    def make_voice(self):
        print('%s:喵喵喵..'%self._nickname)
def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()