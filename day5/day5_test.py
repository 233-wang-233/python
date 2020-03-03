'''
在屏幕上显示跑马灯文字
'''
# import os
# import time
# def main():
#     content='北京欢迎您！'
#     while True:
#         #清理屏幕输出
#         os.system('clear')
#         print(content)
#         time.sleep(0.2)
#         content=content[1:]+content[0]#前进一格
# if __name__=='__main__':
#     main()
'''
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
'''
import random
def generate_code(code_len=4):
    '''
    生成指定长度验证码
    :param code_len:
    :return:
    '''
    all_chars='0123456789abcdefghijklmnopqrstuvwxyz'
    last_pos=len(all_chars)-1
    code=''
    for _ in range(code_len):
        index=random.randint(0,last_pos)
        code+=all_chars[index]
    return code
print(generate_code((4)))

'''
设计一个函数返回给定文件名的额后缀名
'''
def get_suffix(filename,has_dot=False):
    '''
    获取文件后缀名
    :param filename:
    :param has_dot:
    :return:
    '''
    pos=filename.rfind('.')
    if 0<pos<len(filename)-1:
        index=pos if has_dot else pos+1
        return filename[index:]
    else:
        return  ''
'''
设计一个函数返回传入的列表中最大和第二大的元素的值
'''
def max2(x):
    m1,m2=(x[0],x[1]) if x[0]>x[1] else (x[1],x[0])
    for index in range(2,len(x)):
        if x[index]>m1:
            m2=m1
            m1=x[index]
        elif x[index]>m2:
            m2=x[index]
    return m1,m2

'''
计算指定的年月日是这一年的第几天
'''
def is_leap_year(year):
    '''
    判断这一年是否为闰年
    :param year: 年份
    :return: 闰年返回True
    '''
    return year%4==0 and year%100!=0 or year%400==0

def which_day(year,month,date):
    '''
    计算传入的日期是这一年的第几天
    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    '''
    days_of_month=[
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]#返回布尔值
    total=0
    for index in range(month-1):
        total++days_of_month[index]
    return  total+date
# print([is_leap_year(1998)])
def main():
    print(which_day(1998,11,23))
if __name__=='__main__':
    main()

'''
打印杨辉三角
'''
def main():
    num=int(input('number of rows: '))
    yh=[[]]*num
    for row in range(len(yh)):
        yh[row]=[None]*(row+1)
        for col in range(len(yh[row])):
            if col ==0 or col==row:
                yh[row][col]=1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

if __name__ == '__main__':
    main()

