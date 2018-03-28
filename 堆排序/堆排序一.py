def sift(data,low,high):
    i = low
    j = 2 * i + 1
    tmp = data[low]
    while j <= high:
        if j < high and data[j] < data[j+1]:
            j += 1
        if tmp < data[j]:
            data[i] = data[j]
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = tmp

def heap_sort(li):
    n = len(li)
    for i in range(n//2-1,-1,-1):
        sift(li,i,n-1)
    for j in range(n-1,-1,-1):
        li[j],li[0] = li[0],li[j] #挨个出数
        sift(li,0,j-1)
import random
li = list(range(1000))
random.shuffle(li)
heap_sort(li)
print(li)

