def bubble_sort(origin_items,comp=lambda x,y:x>y):
    '''搅拌排序,先把所有的大的放前面，再把所有的小的放后面'''
    items=origin_items[:]
    for i in range(len(items)-1):
        swapped = False
        for j in range(i,len(items)-i-1):
            if comp(items[j],items[j+1]):
                items[j],items[j+1]=items[j+1],items[j]
                swapped=True

        if swapped:
            swapped=False
            for j in range(len(items)-2-i,i,-1):
                if comp(items[j-1],items[j]):
                    items[j],items[j-1]=items[j-1],items[j]
                    swapped=True
        if not swapped:
            break
    return items
def main():
    items=[1,5,2,3,7,9,10]
    items1=[10,8,20,40,100,2,9,10]
    print(bubble_sort(items))
    print(bubble_sort(items1))
if __name__ == '__main__':
    main()