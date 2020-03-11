#进程就是操作系统中执行的一个程序
#进程可以通过fork或spawn的方式来创建新的进程来执行其他的任务
'''
randint(1,3)随机整数
randrange(1,3)随机生成0-2的数字
'''
print('非多线程'.center(40,'*'))
from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()#时间戳：是一种浮点数格式，从1970年到现在的秒数
    #print(start)
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()

print('多线程'.center(42,'*'))
from multiprocessing import Process
from os import getpid
from random import randint
from  time import time,sleep
def down_to_time(filename):
    print('驱动下载进程，进程号[%d].'%getpid())
    print('开始下载%s....'%filename)
    time_to_download=randint(5,10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒'%(filename,time_to_download))
def main():
    start=time()
    p1=Process(target=down_to_time,args=('python',))#创建进程对象
    #target参数我们传入一个函数来表示进程启动后要执行的代码，
    # 后面的args是一个元组，它代表了传递给函数的参数
    p1.start()#启动进程
    p2=Process(target=down_to_time,args=('java',))
    p2.start()
    p1.join()#停止进程
    p2.join()
    end=time()
    print('总共耗费了%.2f秒.' % (end - start))
if __name__ == '__main__':
    main()
