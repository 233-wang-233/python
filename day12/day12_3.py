def bubble_sort(origin): #本算法缺点：无法解决有重复数字问题
    '''高质量冒泡排序(搅拌排序)'''
    items=origin[:]
    length=len(items)
    # print(items)
    # print(range(length))
    for i in range(length):
        items1=items[i:length-i]
        max1=items1.index(max(items1))#每过一轮排序排除首尾两项
        # print(max1+i)
        tep=items[max1+i]
        items[max1+i]=items[i]
        items[i]=tep
        # print(items)
        items1 = items[i:length - i]
        min1 = items1.index(min(items1))
        # print(min1+i)
        tep = items[min1+i]
        items[min1+i] = items[length-i-1]
        items[length-i-1] = tep
        if len(items1)==1:
             break
    return items
def main():
    items=[1,5,2,3,7,9,10]
    items1=[10,8,20,40,100,2,9]
    print(bubble_sort(items))
    print(bubble_sort(items1))
if __name__ == '__main__':
    main()