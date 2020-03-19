def merge_sort(items,comp=lambda x,y:x<=y):
    '''归并排序'''
    if len(items)<2:
        return items[:]
    mid=len(items)//2
    left=merge_sort(items[:mid],comp)
    right=merge_sort(items[mid:],comp)
    return merge(left,right,comp)
def merge(items1,items2,comp):
    '''合并'''
    items=[]
    index1,index2=0,0
    while index1<len(items1) and index2<len(items2):
        if comp(items1[index1],items2[index2]):
            items.append(items1[index1])
            index1+=1
        else:
            items.append(items2[index2])
            index2+=1
    items+=items1[index1:]
    items+=items2[index2:]
    return items

def seq_search(items,key):
    '''顺序查找'''
    for index,item in enumerate(items):#enumerate用来提取key和对象
        if item == key:
            return index
    return -1

def bin_search(items,key):
    '''折半查找(必须是顺序结构)'''
    start,end=0,len(items)-1
    while start<=end:
        mid=(start+end)//2
        if key>items[mid]:
            start=mid+1
        elif key<items[mid]:
            end=mid-1
        else:return mid
    return -1