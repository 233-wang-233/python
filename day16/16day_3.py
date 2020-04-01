def fib(num):
    '''生成器'''
    a,b=0,1
    for _ in range(num):
        a,b=b,a+b
        yield a#yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。
class Fib(object):
    '''迭代器'''
    def __init__(self,num):
        self.num=num
        self.a,self.b=0,1
        self.idx=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.idx<self.num:
            self.a,self.b=self.b,self.a+self.b
            self.idx+=1
            return self.a
        raise  StopIteration