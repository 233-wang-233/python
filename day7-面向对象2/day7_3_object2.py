'''
python可以在类中定义类方法，类方法第一个参数约定为cls
其代表当前类相关的信息的对象
通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象
'''
from time import time,localtime,sleep

class Clock(object):
    '''数字时钟'''

    def __init__(self,hour=0,min=0,second=0):
        self._hour=hour
        self._min=min
        self._second=second

    @classmethod
    def now(cls):
        ctime=localtime(time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)

    def run(self):
        '''走字'''
        self._second+=1
        if self._second==60:
            self._second=0
            self._min+=1
            if self._min==60:
                self._min=0
                self._hour+=1
                if self._hour==24:
                    self._hour=0

    def show(self):
        '''显示'''
        return '%02d:%02d:%02d'%(self._hour,self._min,self._second)

def main():
    #通过类方法创建对象并获得系统时间
    clock=Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()
if __name__ == '__main__':
    main()