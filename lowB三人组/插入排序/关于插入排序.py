import time
def cal_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        exp_time= time.time()-start
        print(exp_time)
    return inner
"""原理：1、从无序区中，随机选取一个数，作为有序区的第一个数，
        2、循环从无序区取数，小于此数的放在此数的前边，小于则放在后边
"""

@cal_time
def insert_sort(li):
    for i in range(1,len(li)-1):
        tmp = li[i] #表示摸到将要插入队列的牌
        j = i - 1 #表示有序区的最后一个元素
        while li[j] > tmp and j >= 0:#摸到的牌与有序去的牌比较
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp #把摸到的牌插入队列

import random
li = list(range(2000))
random.shuffle(li)
print(li)
print(insert_sort(li))
print(li)
