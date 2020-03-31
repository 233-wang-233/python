def main():
    items=list(map(int,input().split()))#一种数据输入方法
    size=len(items)
    overall,partial={},{}
    for i in range(size-2,-1,-1):
        partial[i]=max(items[i],partial[i+1]+items[i])
        overall[i]=max(partial[i],overall[i+1])
    print(overall[0])
if __name__ == '__main__':
    main()

items1=list(map(lambda  x:x**2,filter(lambda  x:x%2,range(1,10))))
items2=[x**2 for x in range(1,10) if x%2]