#1、堆排序过程
#2、得到堆顶元素，为最大元素
#3、去掉对顶，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序
#4、堆顶元素为最大元素
#5、重复步骤3，直到堆变空
import random

def sift(li,low,high):
    """
    :param li:
    :param low: 堆节点的位置（最顶端的数，在堆中，每建一次堆，出来一个剩下数中最大的数）
    :param high:堆最右一个节点的位置
    :return:
    """
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        # print('hello')
        if j < high and li[j+1] > li[j]:
            j += 1
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp
# li = [2,9,7,8,5,0,1,6,4,3]
# sift(li,0,len(li)-1)
# print(li)

def heap_sort(li):
    n = len(li)
    # print('jj',li)
    for i in range(n//2-1,-1,-1):
        sift(li,i,n-1)
    # print('hh',li)
    for j in range(n-1,-1,-1):
        #j表示堆最后一个元素的位置
        li[0],li[j] = li[j],li[0]
        sift(li,0,j-1)
li = list(range(1000))
random.shuffle(li)
heap_sort(li)
print(li)


