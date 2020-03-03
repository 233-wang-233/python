from random import randrange,randint,sample

def display(balls):
    '''
    输出列表中的双色球号码
    :param balls:
    :return:
    '''
    for index,ball in enumerate(balls):#enumerate为索引
        if index == len(balls)-1:
            print('|',end='')
        print('%02d'%ball,end='')
    print()

def random_select():
    '''
    随机选择一组号码
    :return:
    '''
    red_balls=[x for x in range(1,34)]
    select_balls=[]
    select_balls=sample(red_balls,6) #从数组中随机选取6个数字
    select_balls.sort()
    select_balls.append(randint(1,16))
    return  select_balls
def main():
    n=int(input('随机几注: '))
    for _ in range(n):
        display((random_select()))

if __name__=='__main__':
    main()
