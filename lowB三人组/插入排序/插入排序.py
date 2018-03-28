def insert_sort(li):
    for i in range(1,len(li)-1):
        # i 表示无序区的第一个数
        tmp = li[i] #摸到的牌
        j = i - 1 #j 表示有序区的最后位置
        while li[j] > tmp and j >=0:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp

import random
li = list(range(2000))
random.shuffle(li)
print(li)
print(insert_sort(li))
print(li)
