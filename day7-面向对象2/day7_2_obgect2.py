'''
静态方法和类方法
之前的定义方法为对象方法
例如：我们定义一个“三角形”类，通过传入三条边长来构造三角形，
并提供计算周长和面积的方法，但是传入的三条边长未必能构造出三角形对象，
因此我们可以先写一个方法来验证三条边长是否可以构成三角形，
这个方法很显然就不是对象方法，因为在调用这个方法时三角形对象尚未创
建出来（因为都不知道三条边能不能构成三角形），
所以这个方法是属于三角形类而并不属于三角形对象的。
'''
from math import sqrt

class Triangle(object):
    def __init__(self,a,b,c):
        self._a=a
        self._b=b
        self._c=c

    @staticmethod
    def is_valid(a,b,c):
        return a+b>c and a+c>b and b+c>a

    def perimeter(self):
        return self._a+self._b+self._c

    def area(self):
        half=self.perimeter()/2
        return sqrt(half*(half-self._c)*(half-self._b)*(half-self._a))

def main():
    a,b,c=2,3,4
    #静态方法和类方法都是通过类发消息来调用
    if Triangle.is_valid(a,b,c):
        t=Triangle(a,b,c)
        print(t.area())
        print(t.perimeter())#计算周长
    else:
        print('无法构成三角形')

if __name__=='__main__':
    main()