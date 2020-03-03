#实现一个生成斐波拉切数列的生成器
def fib(n):
    a=0
    b=1
    for _ in range(n):
        a,b=b,a+b
        yield a   #通过yield关键字将一个普通函数改造成生成器函数
def main():
    for val in fib(20):
        print(val)

if __name__ =='__main__':
    main()