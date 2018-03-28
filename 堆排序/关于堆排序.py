#1、先建堆
#2、挨个出数，每次都是最大的数先出

def sift(li,low,high):
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if j < high and li[j] < li[j+1]:
            j += 1
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp

def heap_sort(li):
    #建多少个堆
    n = len(li)
    for i in range(n//2-1,-1,-1):
        sift(li,i,n-1)
    #挨个出数
    for j in range(n-1,-1,-1):
        li[j],li[0] = li[0],li[j]
        sift(li,0,j-1)

import random
li = list(range(10000))
random.shuffle(li)
heap_sort(li)
print(li)