from time import sleep
import os

class Clock(object):
    '''数字时钟'''
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second

    os.system('cls')
    def run(self):
        self.second+=1
        if self.second==60:
            self.minute+=1
            self.second=0
            if self.second==60:
                self.hour+=1
                self.second=0
                if self.hour==24:
                    self.hour=0
    def show(self):
        return '%02d:%02d:%02d' %(self.hour,self.minute,self.second)


def main():
    clock1=Clock(00,00,00)
    while True:
        print(clock1.show())
        os.system('cls')
        sleep(1)
        clock1.run()

if __name__=='__main__':
    main()